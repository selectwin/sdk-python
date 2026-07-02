"""Runtime helpers shared by the generated resources (stable; hand-written)."""

from __future__ import annotations

from typing import Any, Awaitable, Callable, TypeVar

import httpx

from .errors import APIConnectionError, SelectwinError

T = TypeVar("T")


def call(fn: Callable[..., T], /, **kwargs: Any) -> T:
    """Invoke a generated ``sync`` op, normalising transport failures.

    Typed API errors are raised by the response hook and pass through untouched;
    only genuine connection failures are wrapped as :class:`APIConnectionError`.
    """
    try:
        return fn(**kwargs)
    except SelectwinError:
        raise
    except httpx.HTTPError as exc:  # network/timeout after retries
        raise APIConnectionError(f"Request to Selectwin failed: {exc}", raw=exc) from exc


async def acall(fn: Callable[..., Awaitable[T]], /, **kwargs: Any) -> T:
    """Async counterpart of :func:`call`."""
    try:
        return await fn(**kwargs)
    except SelectwinError:
        raise
    except httpx.HTTPError as exc:
        raise APIConnectionError(f"Request to Selectwin failed: {exc}", raw=exc) from exc


def as_model(value: Any, model_cls: Any) -> Any:
    """Coerce a plain ``dict`` request body into its generated model (via ``from_dict``)."""
    if isinstance(value, dict):
        return model_cls.from_dict(value)
    return value
