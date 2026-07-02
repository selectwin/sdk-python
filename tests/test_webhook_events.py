from selectwin import WEBHOOK_EVENT_TYPES, is_webhook_event_type
from selectwin import webhook_events as we


def test_catalog_is_complete_and_unique():
    # Tracks the spec's event enum (regen on scripts/sync_core.py).
    assert len(WEBHOOK_EVENT_TYPES) == 72
    assert len(set(WEBHOOK_EVENT_TYPES)) == len(WEBHOOK_EVENT_TYPES)
    for t in ("transaction.approved", "subscription.paused", "checkout.session.completed", "webhook.ping"):
        assert t in WEBHOOK_EVENT_TYPES


def test_guard():
    assert is_webhook_event_type("transaction.approved") is True
    assert is_webhook_event_type("customer.address.deleted") is True
    assert is_webhook_event_type("nope.nope") is False
    assert is_webhook_event_type(123) is False


def test_per_resource_group_literals_exist():
    # The webhook.* group is renamed to avoid clashing with the master union name.
    for name in ("WebhookEventType", "TransactionEventType", "CheckoutEventType", "WebhookEndpointEventType"):
        assert hasattr(we, name)
