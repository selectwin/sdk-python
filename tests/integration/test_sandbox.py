"""Sandbox integration tests — hit the REAL Selectwin sandbox API.

Self-gated: skipped unless a sandbox key is present, so ``pytest`` stays offline
by default. Provide a **sandbox** key (prefix ``sk_test_``):

    SELECTWIN_SANDBOX_KEY=sk_test_... pytest -m integration
    # SELECTWIN_API_KEY is also honoured, but only if it starts with sk_test_.
    # SELECTWIN_BASE_URL optionally overrides the host.
"""

from __future__ import annotations

import os
import uuid

import pytest

from selectwin import AsyncSelectwin, AuthenticationError, NotFoundError, SelectwinError, Selectwin


def _resolve_key():
    explicit = (os.getenv("SELECTWIN_SANDBOX_KEY") or "").strip()
    if explicit:
        return explicit
    generic = (os.getenv("SELECTWIN_API_KEY") or "").strip()
    return generic if generic.startswith("sk_test_") else None


KEY = _resolve_key()
BASE = (os.getenv("SELECTWIN_BASE_URL") or "").strip() or None

pytestmark = [
    pytest.mark.integration,
    pytest.mark.skipif(not KEY, reason="set SELECTWIN_SANDBOX_KEY to run sandbox integration tests"),
]


def _kwargs(**extra):
    kw = dict(max_retries=1, timeout=30.0, user_agent="selectwin-python-integration-tests", **extra)
    if BASE:
        kw["base_url"] = BASE
    return kw


def _unique_email():
    return f"sdk-it-{uuid.uuid4().hex[:12]}@sandbox.selectwin.test"


def test_read_only_smoke_lists_customers():
    sw = Selectwin(KEY, **_kwargs())
    page = sw.customers.list(limit=2).first()
    assert isinstance(getattr(page, "data", None), list)
    assert isinstance(getattr(page, "has_more", None), bool)
    sw.close()


def test_auto_pagination_respects_cap():
    sw = Selectwin(KEY, **_kwargs())
    some = sw.customers.list(limit=1).to_list(max=3)
    assert isinstance(some, list) and len(some) <= 3
    sw.close()


def test_invalid_key_maps_to_authentication_error():
    sw = Selectwin("sk_test_this_key_is_not_valid_000", **_kwargs(max_retries=0))
    with pytest.raises(SelectwinError) as ei:
        sw.customers.list(limit=1).first()
    assert isinstance(ei.value, AuthenticationError)
    sw.close()


def test_create_retrieve_delete_round_trip():
    sw = Selectwin(KEY, **_kwargs())
    email = _unique_email()
    created = sw.customers.create(
        {"firstName": "SDK", "lastName": "Integration", "email": email, "metadata": {"sdkIntegrationTest": True}}
    )
    try:
        assert created.id
        assert created.email == email
        fetched = sw.customers.retrieve(created.id)
        assert fetched.id == created.id
    finally:
        sw.customers.delete(created.id)
    with pytest.raises(NotFoundError):
        sw.customers.retrieve(created.id)
    sw.close()


async def test_async_read_only_smoke():
    async with AsyncSelectwin(KEY, **_kwargs()) as sw:
        page = await sw.customers.list(limit=1).first()
        assert isinstance(getattr(page, "data", None), list)
