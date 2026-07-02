"""Official Selectwin Python SDK.

A generated core (openapi-python-client, httpx sync + async) plus a hand-written
DX shell: typed client, typed errors, auto-retries, idempotency, sync/async
pagination and webhook signature verification.
"""

from __future__ import annotations

from .client import AsyncSelectwin, Selectwin, SDK_VERSION
from .errors import (
    APIConnectionError,
    APIError,
    AuthenticationError,
    CardError,
    ConflictError,
    NotFoundError,
    PermissionDeniedError,
    RateLimitError,
    SelectwinError,
    SignatureVerificationError,
    ValidationError,
    error_from_status,
)
from .pagination import AsyncPager, SyncPager
from .webhook_events import WEBHOOK_EVENT_TYPES, WebhookEventType, is_webhook_event_type
from .webhooks import SelectwinEvent, construct_event

__version__ = SDK_VERSION

__all__ = [
    "__version__",
    # clients
    "Selectwin",
    "AsyncSelectwin",
    # errors
    "SelectwinError",
    "APIConnectionError",
    "APIError",
    "AuthenticationError",
    "PermissionDeniedError",
    "NotFoundError",
    "ConflictError",
    "ValidationError",
    "CardError",
    "RateLimitError",
    "SignatureVerificationError",
    "error_from_status",
    # pagination
    "SyncPager",
    "AsyncPager",
    # webhooks
    "construct_event",
    "SelectwinEvent",
    # webhook event catalog
    "WEBHOOK_EVENT_TYPES",
    "WebhookEventType",
    "is_webhook_event_type",
]
