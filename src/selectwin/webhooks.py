"""Webhook signature verification.

Selectwin signs each delivery with ``X-Selectwin-Signature: sha256=<hex>`` — an
HMAC-SHA256 of the RAW request body using the endpoint secret (``whsec_...``). An
optional replay-proof scheme is sent in ``X-Selectwin-Signature-v1: t=<unix>,v1=<hex>``
where the signed message is ``<t>.<rawBody>``.

You MUST pass the raw body (bytes/str exactly as received) — re-serialising the
JSON (key order / spacing) breaks verification.
"""

from __future__ import annotations

import hashlib
import hmac
import json
import time
from typing import Any, Optional, Union

from .errors import SignatureVerificationError

Body = Union[str, bytes, bytearray]


class _Payload:
    __slots__ = ("object", "_raw")

    def __init__(self, raw: Any) -> None:
        self._raw = raw if isinstance(raw, dict) else {}
        self.object = self._raw.get("object")

    def __getitem__(self, key: str) -> Any:
        return self._raw[key]


class SelectwinEvent:
    """A verified webhook event (see the Event Catalog for ``type`` values)."""

    __slots__ = ("id", "type", "source", "payload", "correlation_id", "account", "created_at", "updated_at", "_raw")

    def __init__(self, raw: dict) -> None:
        self._raw = raw
        self.id = raw.get("id")
        self.type = raw.get("type")
        self.source = raw.get("source")
        self.payload = _Payload(raw.get("payload"))
        self.correlation_id = raw.get("correlationId", raw.get("correlation_id"))
        self.account = raw.get("account")
        self.created_at = raw.get("createdAt", raw.get("created_at"))
        self.updated_at = raw.get("updatedAt", raw.get("updated_at"))

    def __getitem__(self, key: str) -> Any:
        return self._raw[key]

    def get(self, key: str, default: Any = None) -> Any:
        return self._raw.get(key, default)

    def __repr__(self) -> str:  # pragma: no cover - cosmetic
        return f"SelectwinEvent(id={self.id!r}, type={self.type!r})"


def _to_bytes(body: Body) -> bytes:
    if isinstance(body, str):
        return body.encode("utf-8")
    return bytes(body)


def _hmac_hex(secret: str, data: bytes) -> str:
    return hmac.new(secret.encode("utf-8"), data, hashlib.sha256).hexdigest()


def _parse_v1(header: str) -> dict:
    out: dict = {}
    for part in header.split(","):
        if "=" in part:
            key, _, value = part.partition("=")
            out[key.strip()] = value.strip()
    return out


def construct_event(
    raw_body: Body,
    signature_header: Optional[str],
    secret: str,
    *,
    signature_v1: Optional[str] = None,
    tolerance: Optional[int] = None,
    now: Optional[Any] = None,
) -> SelectwinEvent:
    """Verify the signature and return the parsed event.

    Raises :class:`SignatureVerificationError` if the signature is missing or invalid.

    ``signature_v1`` (the ``X-Selectwin-Signature-v1`` header) additionally verifies
    the replay-proof scheme; pass ``tolerance`` (seconds) to reject stale timestamps.
    """
    if not secret:
        raise SignatureVerificationError("Missing webhook secret")
    if not signature_header:
        raise SignatureVerificationError("Missing X-Selectwin-Signature header")

    body = _to_bytes(raw_body)
    received = signature_header[len("sha256=") :] if signature_header.startswith("sha256=") else signature_header
    expected = _hmac_hex(secret, body)
    if not hmac.compare_digest(received, expected):
        raise SignatureVerificationError("Webhook signature verification failed")

    if signature_v1:
        parsed = _parse_v1(signature_v1)
        t, v1 = parsed.get("t"), parsed.get("v1")
        if t and v1:
            expected_v1 = _hmac_hex(secret, f"{t}.".encode("utf-8") + body)
            if not hmac.compare_digest(v1, expected_v1):
                raise SignatureVerificationError("Webhook v1 signature verification failed")
            if tolerance is not None:
                clock = now() if callable(now) else time.time()
                if abs(int(clock) - int(t)) > tolerance:
                    raise SignatureVerificationError("Webhook timestamp is outside the tolerance window")

    try:
        parsed_body = json.loads(body.decode("utf-8"))
    except Exception:
        raise SignatureVerificationError("Webhook payload is not valid JSON")
    if not isinstance(parsed_body, dict):
        raise SignatureVerificationError("Webhook payload is not a JSON object")
    return SelectwinEvent(parsed_body)
