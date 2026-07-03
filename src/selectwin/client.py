"""The Selectwin clients — the hand-written DX shell over the generated core.

    from selectwin import Selectwin
    sw = Selectwin(api_key="sk_test_…")
    tx = sw.transactions.create({"amount": 9990, "payment": {"method": "pix", "currency": "BRL"}})

One authenticated httpx client (custom retrying transport + idempotency/error
hooks) is shared by every resource namespace, so auth, retries, idempotency and
typed-error mapping apply everywhere.
"""

from __future__ import annotations

from importlib.metadata import PackageNotFoundError
from importlib.metadata import version as _dist_version
from typing import Any, Optional

import httpx

from ._core.client import AuthenticatedClient
from .http import build_httpx_args
from .resources import NAMESPACES
from .webhooks import construct_event

try:
    # Single source of truth: the installed package metadata (from pyproject.toml).
    # Never hand-edit a version constant here — it only drifts. Falls back to a dev
    # marker when running from source without an install.
    SDK_VERSION = _dist_version("selectwin")
except PackageNotFoundError:  # pragma: no cover - source checkout, not installed
    SDK_VERSION = "0.0.0-dev"

DEFAULT_BASE_URL = "https://api.selectwin.io"


def _build_client(
    api_key: str,
    *,
    base_url: str,
    max_retries: int,
    timeout: Optional[float],
    user_agent: str,
    verify_ssl: bool,
    is_async: bool,
) -> AuthenticatedClient:
    if not api_key:
        raise ValueError("Selectwin: an API key is required (sk_test_… or sk_live_…).")
    return AuthenticatedClient(
        base_url=base_url,
        token=api_key,
        auth_header_name="selectkey",  # Selectwin auth header…
        prefix="",  # …carrying the bare key (no "Bearer ").
        headers={"User-Agent": user_agent},
        timeout=httpx.Timeout(timeout) if timeout else None,
        verify_ssl=verify_ssl,
        raise_on_unexpected_status=False,  # errors are raised by the response hook
        httpx_args=build_httpx_args(is_async=is_async, max_retries=max_retries, verify_ssl=verify_ssl),
    )


class _BaseClient:
    def __init__(
        self,
        api_key: str,
        *,
        base_url: str = DEFAULT_BASE_URL,
        max_retries: int = 2,
        timeout: Optional[float] = 60.0,
        user_agent: Optional[str] = None,
        verify_ssl: bool = True,
        _is_async: bool = False,
    ) -> None:
        self._client = _build_client(
            api_key,
            base_url=base_url,
            max_retries=max_retries,
            timeout=timeout,
            user_agent=user_agent or f"selectwin-python/{SDK_VERSION}",
            verify_ssl=verify_ssl,
            is_async=_is_async,
        )
        for attr, sync_cls, async_cls in NAMESPACES:
            setattr(self, attr, (async_cls if _is_async else sync_cls)(self._client))
        # The webhooks namespace also carries the offline verification helper.
        self.webhooks.construct_event = construct_event  # type: ignore[attr-defined]

    @property
    def http(self) -> AuthenticatedClient:
        """Escape hatch: the underlying generated ``AuthenticatedClient``."""
        return self._client


class Selectwin(_BaseClient):
    """Synchronous client. Use as a context manager or call :meth:`close`."""

    def __init__(self, api_key: str, **kwargs: Any) -> None:
        super().__init__(api_key, _is_async=False, **kwargs)

    def __enter__(self) -> "Selectwin":
        self._client.__enter__()
        return self

    def __exit__(self, *args: Any) -> None:
        self._client.__exit__(*args)

    def close(self) -> None:
        self._client.get_httpx_client().close()


class AsyncSelectwin(_BaseClient):
    """Asynchronous client. Use ``async with AsyncSelectwin(...) as sw:``."""

    def __init__(self, api_key: str, **kwargs: Any) -> None:
        super().__init__(api_key, _is_async=True, **kwargs)

    async def __aenter__(self) -> "AsyncSelectwin":
        await self._client.__aenter__()
        return self

    async def __aexit__(self, *args: Any) -> None:
        await self._client.__aexit__(*args)

    async def aclose(self) -> None:
        await self._client.get_async_httpx_client().aclose()
