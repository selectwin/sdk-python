import json

import httpx
import pytest
import respx

from selectwin import (
    APIConnectionError,
    AsyncSelectwin,
    CardError,
    NotFoundError,
    Selectwin,
)

BASE = "https://api.selectwin.io"
KEY = "sk_test_abc"
CUST = {"firstName": "A", "lastName": "B", "email": "a@b.co"}


def _ignore_parse(fn, *args, **kwargs):
    # Success-body deserialization needs the full generated model; these tests
    # assert on the REQUEST, so tolerate a minimal-body parse failure.
    try:
        return fn(*args, **kwargs)
    except (CardError, NotFoundError, APIConnectionError):
        raise
    except Exception:
        return None


@respx.mock
def test_sends_selectkey_header_and_user_agent():
    route = respx.get(f"{BASE}/v1/customers/cus_1").mock(return_value=httpx.Response(200, json={"id": "cus_1"}))
    sw = Selectwin(KEY)
    _ignore_parse(sw.customers.retrieve, "cus_1")
    req = route.calls.last.request
    assert req.method == "GET"
    assert req.headers["selectkey"] == KEY
    assert req.headers["user-agent"].startswith("selectwin-python/")


@respx.mock
def test_adds_idempotency_key_and_json_body_on_mutation():
    route = respx.post(f"{BASE}/v1/customers").mock(return_value=httpx.Response(201, json={"id": "cus_1"}))
    sw = Selectwin(KEY)
    _ignore_parse(sw.customers.create, CUST)
    req = route.calls.last.request
    assert req.headers["selectkey"] == KEY
    idem = req.headers.get("x-idempotency-key")
    assert idem and len(idem) == 32
    body = json.loads(req.content)
    assert body["email"] == "a@b.co" and body["firstName"] == "A"  # to_dict → wire camelCase


@respx.mock
def test_maps_402_to_card_error():
    respx.post(f"{BASE}/v1/customers").mock(
        return_value=httpx.Response(
            402,
            json={"error": {"code": "card_declined", "message": "no", "displayMessage": "Recusado", "reversible": True}},
        )
    )
    sw = Selectwin(KEY)
    with pytest.raises(CardError) as ei:
        sw.customers.create(CUST)
    assert ei.value.code == "card_declined"
    assert ei.value.display_message == "Recusado"
    assert ei.value.reversible is True


@respx.mock
def test_maps_404_to_not_found():
    respx.get(f"{BASE}/v1/customers/cus_x").mock(return_value=httpx.Response(404, json={"error": {"code": "not_found"}}))
    sw = Selectwin(KEY)
    with pytest.raises(NotFoundError):
        sw.customers.retrieve("cus_x")


@respx.mock
def test_retries_5xx_then_succeeds():
    route = respx.post(f"{BASE}/v1/customers").mock(
        side_effect=[httpx.Response(503), httpx.Response(201, json={"id": "cus_1"})]
    )
    sw = Selectwin(KEY)  # default max_retries=2
    _ignore_parse(sw.customers.create, CUST)
    assert route.call_count == 2  # retried once, then the 201


@respx.mock
def test_network_error_maps_to_api_connection_error():
    respx.post(f"{BASE}/v1/customers").mock(side_effect=httpx.ConnectError("boom"))
    sw = Selectwin(KEY, max_retries=0)
    with pytest.raises(APIConnectionError):
        sw.customers.create(CUST)


def test_requires_an_api_key():
    with pytest.raises(ValueError):
        Selectwin("")


@respx.mock
async def test_async_sends_auth_and_maps_error():
    respx.get(f"{BASE}/v1/customers/cus_x").mock(return_value=httpx.Response(404, json={"error": {"code": "not_found"}}))
    route = respx.post(f"{BASE}/v1/customers").mock(return_value=httpx.Response(201, json={"id": "cus_1"}))
    async with AsyncSelectwin(KEY) as sw:
        with pytest.raises(NotFoundError):
            await sw.customers.retrieve("cus_x")
        try:
            await sw.customers.create(CUST)
        except Exception:
            pass
    req = route.calls.last.request
    assert req.headers["selectkey"] == KEY
    assert "x-idempotency-key" in req.headers


# --- Security sweep 31 (S-1): a "." / ".." ID would reach another endpoint ---------------------------------------
# httpx resolves dot segments while building the request: DELETE /v1/products/prd_1/variants/.. left as
# DELETE /v1/products/prd_1 — the whole product. Refused before the request is built; nothing is sent.

from selectwin import ValidationError  # noqa: E402
from selectwin.http import has_dot_segment  # noqa: E402


@respx.mock
def test_refuses_dot_segment_path_params_before_sending():
    route = respx.route().mock(return_value=httpx.Response(204))
    sw = Selectwin(KEY, max_retries=0)
    for bad in ("..", "."):
        with pytest.raises(ValidationError):
            sw.variants.delete(product_id="prd_1", variant_id=bad)
        with pytest.raises(ValidationError):
            sw.customers.retrieve(bad)
    assert route.call_count == 0


@respx.mock
@pytest.mark.asyncio
async def test_async_refuses_dot_segment_path_params_before_sending():
    route = respx.route().mock(return_value=httpx.Response(204))
    sw = AsyncSelectwin(KEY, max_retries=0)
    with pytest.raises(ValidationError):
        await sw.variants.delete(product_id="prd_1", variant_id="..")
    assert route.call_count == 0


def test_has_dot_segment_reads_the_raw_path_only():
    for bad in ("/v1/products/prd_1/variants/..", "/v1/customers/./cards", "/v1/customers/%2E%2E", "https://h/v1/x/.%2e?q=1"):
        assert has_dot_segment(bad), bad
    for ok in ("/v1/customers/cus_1", "/v1/customers/cus_1.2", "/v1/customers/%252e%252e", "/v1/customers?q=.."):
        assert not has_dot_segment(ok), ok
