# selectwin (Python)

Official **Selectwin** Python SDK — payments (credit card, PIX, boleto),
subscriptions, wallets, webhooks and more. Sync **and** async, fully typed.

> Status: **early / work in progress** (`0.1.0`). Generated core (openapi-python-client,
> httpx sync+async) + a hand-written DX shell (typed errors, retries, idempotency,
> pagination, webhook verification).

```bash
pip install selectwin
```

## Quickstart

```python
import os
from selectwin import Selectwin, CardError

sw = Selectwin(api_key=os.environ["SELECTWIN_API_KEY"])  # sk_test_… / sk_live_…

# Create a PIX transaction (amounts in cents)
tx = sw.transactions.create({"amount": 9990, "payment": {"method": "pix", "currency": "BRL"}})

# id / id+body aliases
one = sw.transactions.retrieve("tra_…")
sw.subscriptions.pause("subs_…")

# Typed errors — branch on the class / error.code, never the message
try:
    sw.transactions.create({...})
except CardError as e:
    print(e.display_message, e.reversible)  # buyer-facing + retryable
```

### Async

```python
import asyncio
from selectwin import AsyncSelectwin

async def main():
    async with AsyncSelectwin(api_key="sk_test_…") as sw:
        tx = await sw.transactions.create({"amount": 9990, "payment": {"method": "pix", "currency": "BRL"}})
        async for t in sw.transactions.list(limit=100):
            ...

asyncio.run(main())
```

### Pagination

Top-level `list()` methods return a pager that is both a page fetcher and an iterator:

```python
# sync — stream every transaction across all pages
for tx in sw.transactions.list(limit=100):
    ...

first_page = sw.transactions.list(limit=20).first()   # a page object (.data, .has_more, …)
some = sw.customers.list().to_list(max=500)            # collect, optionally capped

# async
async for tx in sw.transactions.list(limit=100):
    ...
```

The full generated API (every `operation_id`) is always reachable via `.raw`:

```python
from selectwin._core.api.transactions import create_transaction
# or the bound escape hatch:
sw.transactions.raw  # the generated module for this resource
```

### Webhooks

```python
# raw_body MUST be the exact bytes/str received (do not re-serialize)
event = sw.webhooks.construct_event(
    raw_body,
    request.headers["x-selectwin-signature"],
    os.environ["SELECTWIN_WEBHOOK_SECRET"],  # whsec_…
)
if event.type == "transaction.approved":
    obj = event.payload.object
```

`WEBHOOK_EVENT_TYPES` (the authoritative catalog) and `is_webhook_event_type()` are
exported for validation; `WebhookEventType` is a `typing.Literal` of every event type.

## What the SDK adds over the raw generated client

The package is a **generated core** (openapi-python-client, from the OpenAPI v2.0.0
spec) + a **hand-written DX shell**:

- **Typed clients** — `Selectwin(api_key=…)` (sync) and `AsyncSelectwin(api_key=…)`
  (async context manager) exposing `sw.transactions`, `sw.subscriptions`, `sw.customers`, …
- **Concise aliases** per resource (`create` / `retrieve` / `update` / `list` /
  `delete` + custom verbs), accepting a dict or the generated body model; `.raw` exposes
  the full generated surface.
- **Typed errors** by HTTP status / `error.code`: `CardError` (402, `display_message`/
  `reversible`), `ValidationError` (`params`), `RateLimitError` (`retry_after`),
  `AuthenticationError`, `PermissionDeniedError`, `NotFoundError`, `ConflictError`,
  `APIError`, `APIConnectionError`.
- **Auto-retries** (429/5xx/network) with exponential backoff, honouring `Retry-After`.
- **Idempotency** — an `X-Idempotency-Key` is added to every mutation (override per call).
- **Safe paths** — a path parameter of `.` or `..` is refused before the request is built (it would reach another
  endpoint); redirects are not followed.
- **Timeouts** and one shared, pre-authenticated `httpx` client per SDK client.
- **Auto-pagination** — sync (`for …`) and async (`async for …`) iterators, `.first()`,
  `.to_list(max=…)`, `.pages()`.
- **Webhook verification** — `construct_event` (HMAC-SHA256 of the raw body, constant-time).

Auth is the `SelectKey` header; the environment (sandbox/production) is resolved from the
key prefix (`sk_test_` / `sk_live_`).

## Architecture

```
src/selectwin/
  _core/            # openapi-python-client output — DO NOT edit; synced from selectwin-sdks
  resources.py      # GENERATED resource namespaces (sync + async) — DO NOT edit
  webhook_events.py # GENERATED webhook Event Catalog (types + guard) — DO NOT edit
  errors.py         # typed error hierarchy
  http.py           # httpx transport (retries/timeout) + hooks (idempotency, UA) + error mapping
  pagination.py     # SyncPager / AsyncPager
  webhooks.py       # construct_event (signature verification)
  client.py         # Selectwin / AsyncSelectwin — wire auth + the custom httpx client
```

Cross-cutting concerns are injected **once** into the httpx client shared by the generated
core, so every endpoint inherits them and new endpoints work automatically on regen.

## Development

```bash
pip install -e ".[dev]"
python scripts/sync_core.py          # copy the generated core from selectwin-sdks + regen
python scripts/gen_resources.py      # regenerate src/selectwin/resources.py
python scripts/gen_webhook_events.py # regenerate src/selectwin/webhook_events.py
pytest                               # unit suite
pytest -m integration                # sandbox suite (needs SELECTWIN_SANDBOX_KEY; see tests/integration)
mypy src/selectwin                   # type-check the DX shell
```

## Roadmap

- Publish to PyPI (Trusted Publishing / OIDC) once the API stabilises; CI on PRs.
