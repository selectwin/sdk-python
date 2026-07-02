"""Typed error hierarchy — branch on the class or ``error.code``, never the message.

Every Selectwin API error returns ``{"error": {...}}``. :func:`error_from_status`
maps an HTTP status + that envelope to the right exception subclass.
"""

from __future__ import annotations

import json
from typing import Any, Optional


class SelectwinError(Exception):
    """Base class for every error raised by the SDK."""

    def __init__(
        self,
        message: str,
        *,
        code: Optional[str] = None,
        status_code: Optional[int] = None,
        request_id: Optional[str] = None,
        raw: Any = None,
    ) -> None:
        super().__init__(message)
        self.message = message
        #: Stable, machine-readable error code (``error.code``); ``None`` for
        #: transport/connection errors.
        self.code = code
        self.status_code = status_code
        self.request_id = request_id
        #: The parsed error envelope (or the underlying exception, for connection errors).
        self.raw = raw

    def __repr__(self) -> str:  # pragma: no cover - cosmetic
        parts = [f"message={self.message!r}"]
        if self.code is not None:
            parts.append(f"code={self.code!r}")
        if self.status_code is not None:
            parts.append(f"status_code={self.status_code}")
        if self.request_id is not None:
            parts.append(f"request_id={self.request_id!r}")
        return f"{type(self).__name__}({', '.join(parts)})"


class APIConnectionError(SelectwinError):
    """The request never produced a response (network error, timeout, DNS...)."""


class APIError(SelectwinError):
    """A server-side error (5xx) or an otherwise-unclassified API error."""


class AuthenticationError(SelectwinError):
    """401 — the API key/token is missing or invalid."""


class PermissionDeniedError(SelectwinError):
    """403 — authenticated but not allowed (scope, IP restriction)."""


class NotFoundError(SelectwinError):
    """404 — the resource does not exist."""


class ConflictError(SelectwinError):
    """409 — idempotency conflict (replay in progress or divergent body)."""


class ValidationError(SelectwinError):
    """400/422 — request validation failed. Per-field details in :attr:`params`."""

    def __init__(self, message: str, *, params: Any = None, **kwargs: Any) -> None:
        super().__init__(message, **kwargs)
        #: Per-field validation details (``error.params``), when provided.
        self.params = params


class CardError(SelectwinError):
    """402 — the issuer declined the charge (transactions/subscriptions)."""

    def __init__(
        self,
        message: str,
        *,
        display_message: Optional[str] = None,
        reversible: Optional[bool] = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(message, **kwargs)
        #: Buyer-facing message safe to display (``error.displayMessage``).
        self.display_message = display_message
        #: Whether the same charge can plausibly be retried (``error.reversible``).
        self.reversible = reversible


class RateLimitError(SelectwinError):
    """429 — rate limit exceeded. :attr:`retry_after` is seconds, when sent."""

    def __init__(self, message: str, *, retry_after: Optional[float] = None, **kwargs: Any) -> None:
        super().__init__(message, **kwargs)
        self.retry_after = retry_after


class SignatureVerificationError(SelectwinError):
    """A webhook signature could not be verified."""


_STATUS_MESSAGE = {
    400: "The request was invalid.",
    401: "Invalid or missing API credentials.",
    402: "The payment was declined.",
    403: "You do not have permission to perform this action.",
    404: "The requested resource was not found.",
    409: "Idempotency conflict.",
    422: "The request could not be processed.",
    429: "Too many requests.",
}


def _coerce_envelope(content: Any) -> dict:
    """Best-effort parse of the error body into a dict (accepts bytes/str/dict)."""
    if content is None:
        return {}
    if isinstance(content, dict):
        return content
    if isinstance(content, (bytes, bytearray)):
        try:
            content = content.decode("utf-8", errors="ignore")
        except Exception:  # pragma: no cover - defensive
            return {}
    if isinstance(content, str):
        try:
            parsed = json.loads(content)
            return parsed if isinstance(parsed, dict) else {}
        except Exception:
            return {}
    return {}


def error_from_status(
    status_code: int,
    content: Any = None,
    *,
    request_id: Optional[str] = None,
    retry_after: Optional[float] = None,
) -> SelectwinError:
    """Build the typed error for an HTTP ``status_code`` + response body.

    ``content`` may be raw bytes/str or an already-parsed ``{"error": {...}}`` dict.
    """
    envelope = _coerce_envelope(content)
    raw_err = envelope.get("error")
    err: dict = raw_err if isinstance(raw_err, dict) else {}
    code = err.get("code")
    message = err.get("message") or _STATUS_MESSAGE.get(status_code) or f"HTTP {status_code}"
    common: dict[str, Any] = dict(
        code=code, status_code=status_code, request_id=request_id, raw=envelope or content
    )

    if status_code == 400 or status_code == 422:
        return ValidationError(message, params=err.get("params"), **common)
    if status_code == 401:
        return AuthenticationError(message, **common)
    if status_code == 402:
        return CardError(
            message,
            display_message=err.get("displayMessage") or err.get("display_message"),
            reversible=err.get("reversible"),
            **common,
        )
    if status_code == 403:
        return PermissionDeniedError(message, **common)
    if status_code == 404:
        return NotFoundError(message, **common)
    if status_code == 409:
        return ConflictError(message, **common)
    if status_code == 429:
        return RateLimitError(message, retry_after=retry_after, **common)
    if status_code >= 500:
        return APIError(message, **common)
    return APIError(message, **common)
