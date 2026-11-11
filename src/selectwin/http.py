"""Cross-cutting HTTP concerns, injected once into the httpx client used by the
generated core so every endpoint inherits them with no per-endpoint code:

  - a retrying transport (429/5xx/network) with exponential backoff honouring
    ``Retry-After``;
  - a request hook stamping ``X-Idempotency-Key`` on mutations (+ ``User-Agent``);
  - a response hook mapping non-2xx responses to typed :mod:`selectwin.errors`.
"""

from __future__ import annotations

import asyncio
import random
import re
import time
import uuid
from typing import Any, Dict, Optional

import httpx

from .errors import APIConnectionError, ValidationError, error_from_status

MUTATING = {"POST", "PUT", "PATCH", "DELETE"}
# Retry only where a retry can plausibly help. NOT 409 (idempotency conflict).
RETRYABLE_STATUS = {429, 500, 502, 503, 504}


def _retry_after_seconds(value: Optional[str]) -> Optional[float]:
    if not value:
        return None
    try:
        return float(value)
    except (TypeError, ValueError):
        return None


def _backoff(attempt: int, retry_after: Optional[str]) -> float:
    secs = _retry_after_seconds(retry_after)
    if secs is not None:
        return min(secs, 20.0)
    return min(0.5 * (2 ** attempt), 8.0) + random.uniform(0, 0.25)


class RetryTransport(httpx.BaseTransport):
    """Sync transport wrapper that retries 429/5xx and network errors."""

    def __init__(self, wrapped: httpx.BaseTransport, max_retries: int) -> None:
        self._wrapped = wrapped
        self._max = max(0, max_retries)

    def handle_request(self, request: httpx.Request) -> httpx.Response:
        attempt = 0
        while True:
            try:
                response = self._wrapped.handle_request(request)
            except httpx.TransportError:
                if attempt < self._max:
                    time.sleep(_backoff(attempt, None))
                    attempt += 1
                    continue
                raise
            if response.status_code in RETRYABLE_STATUS and attempt < self._max:
                retry_after = response.headers.get("retry-after")
                response.close()
                time.sleep(_backoff(attempt, retry_after))
                attempt += 1
                continue
            return response

    def close(self) -> None:
        self._wrapped.close()


class AsyncRetryTransport(httpx.AsyncBaseTransport):
    """Async transport wrapper that retries 429/5xx and network errors."""

    def __init__(self, wrapped: httpx.AsyncBaseTransport, max_retries: int) -> None:
        self._wrapped = wrapped
        self._max = max(0, max_retries)

    async def handle_async_request(self, request: httpx.Request) -> httpx.Response:
        attempt = 0
        while True:
            try:
                response = await self._wrapped.handle_async_request(request)
            except httpx.TransportError:
                if attempt < self._max:
                    await asyncio.sleep(_backoff(attempt, None))
                    attempt += 1
                    continue
                raise
            if response.status_code in RETRYABLE_STATUS and attempt < self._max:
                retry_after = response.headers.get("retry-after")
                await response.aclose()
                await asyncio.sleep(_backoff(attempt, retry_after))
                attempt += 1
                continue
            return response

    async def aclose(self) -> None:
        await self._wrapped.aclose()


def _idempotency(request: httpx.Request) -> None:
    if request.method.upper() in MUTATING and "X-Idempotency-Key" not in request.headers:
        request.headers["X-Idempotency-Key"] = uuid.uuid4().hex


def _raise_typed(response: httpx.Response) -> None:
    if response.status_code < 400:
        return
    request_id = response.headers.get("x-request-id")
    retry_after = _retry_after_seconds(response.headers.get("retry-after"))
    raise error_from_status(
        response.status_code,
        response.content,
        request_id=request_id,
        retry_after=retry_after,
    )


def _sync_request_hook(request: httpx.Request) -> None:
    _idempotency(request)


def _sync_response_hook(response: httpx.Response) -> None:
    if response.status_code >= 400:
        response.read()
        _raise_typed(response)


async def _async_request_hook(request: httpx.Request) -> None:
    _idempotency(request)


async def _async_response_hook(response: httpx.Response) -> None:
    if response.status_code >= 400:
        await response.aread()
        _raise_typed(response)


_DOT_SEGMENT = re.compile(r"^(?:\.|%2e){1,2}$", re.IGNORECASE)


def has_dot_segment(url: str) -> bool:
    """Does this URL (or relative path) carry a ``.`` or ``..`` path segment? Checked on the raw string."""
    path = re.sub(r"^[a-z][a-z0-9+.-]*://[^/?#]*", "", url, flags=re.IGNORECASE)
    path = re.split(r"[?#]", path, maxsplit=1)[0]
    return any(_DOT_SEGMENT.match(segment) for segment in path.split("/"))


def guard_dot_segments(client: Any) -> Any:
    """Refuse a ``.``/``..`` path segment before httpx builds the request (security sweep 31, S-1).

    The generated core quotes each ID with ``quote(..., safe="")``, which leaves dots alone, and httpx RESOLVES dot
    segments while building the request: ``variants.delete("prd_1", "..")`` left as DELETE /v1/products/prd_1 —
    another operation, with the key. A hook or transport only ever sees the resolved URL, so the check wraps
    ``build_request`` itself, where the generated core's relative path is still raw. No Selectwin ID is ``.``/``..``.
    """
    build = client.build_request

    def build_request(method: str, url: Any, *args: Any, **kwargs: Any) -> httpx.Request:
        if isinstance(url, str) and has_dot_segment(url):
            raise ValidationError(
                'Selectwin: a path parameter cannot be "." or ".." (the request would reach another endpoint).'
            )
        return build(method, url, *args, **kwargs)

    client.build_request = build_request
    return client


def build_httpx_args(
    *,
    is_async: bool,
    max_retries: int,
    verify_ssl: bool = True,
) -> Dict[str, Any]:
    """Return the ``httpx_args`` dict to hand to the generated ``AuthenticatedClient``.

    Wires the retrying transport + idempotency/error hooks. The generated client
    adds the ``selectkey`` auth header and merges these into its httpx client.
    """
    if is_async:
        transport: Any = AsyncRetryTransport(httpx.AsyncHTTPTransport(verify=verify_ssl), max_retries)
        hooks = {"request": [_async_request_hook], "response": [_async_response_hook]}
    else:
        transport = RetryTransport(httpx.HTTPTransport(verify=verify_ssl), max_retries)
        hooks = {"request": [_sync_request_hook], "response": [_sync_response_hook]}
    return {"transport": transport, "event_hooks": hooks}


__all__ = [
    "APIConnectionError",
    "RetryTransport",
    "AsyncRetryTransport",
    "build_httpx_args",
]
