from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..models.record_subscription_usage_body_action import (
    RecordSubscriptionUsageBodyAction,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.record_subscription_usage_body_metadata import (
        RecordSubscriptionUsageBodyMetadata,
    )


T = TypeVar("T", bound="RecordSubscriptionUsageBody")


@_attrs_define
class RecordSubscriptionUsageBody:
    """
    Attributes:
        quantity (int):
        action (RecordSubscriptionUsageBodyAction | Unset):
        occurred_at (datetime.datetime | Unset):
        idempotency_key (str | Unset):
        metadata (RecordSubscriptionUsageBodyMetadata | Unset):
    """

    quantity: int
    action: RecordSubscriptionUsageBodyAction | Unset = UNSET
    occurred_at: datetime.datetime | Unset = UNSET
    idempotency_key: str | Unset = UNSET
    metadata: RecordSubscriptionUsageBodyMetadata | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        quantity = self.quantity

        action: str | Unset = UNSET
        if not isinstance(self.action, Unset):
            action = self.action.value

        occurred_at: str | Unset = UNSET
        if not isinstance(self.occurred_at, Unset):
            occurred_at = self.occurred_at.isoformat()

        idempotency_key = self.idempotency_key

        metadata: dict[str, Any] | Unset = UNSET
        if not isinstance(self.metadata, Unset):
            metadata = self.metadata.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "quantity": quantity,
            }
        )
        if action is not UNSET:
            field_dict["action"] = action
        if occurred_at is not UNSET:
            field_dict["occurredAt"] = occurred_at
        if idempotency_key is not UNSET:
            field_dict["idempotencyKey"] = idempotency_key
        if metadata is not UNSET:
            field_dict["metadata"] = metadata

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.record_subscription_usage_body_metadata import (
            RecordSubscriptionUsageBodyMetadata,
        )

        d = dict(src_dict)
        quantity = d.pop("quantity")

        _action = d.pop("action", UNSET)
        action: RecordSubscriptionUsageBodyAction | Unset
        if isinstance(_action, Unset):
            action = UNSET
        else:
            action = RecordSubscriptionUsageBodyAction(_action)

        _occurred_at = d.pop("occurredAt", UNSET)
        occurred_at: datetime.datetime | Unset
        if isinstance(_occurred_at, Unset):
            occurred_at = UNSET
        else:
            occurred_at = datetime.datetime.fromisoformat(_occurred_at)

        idempotency_key = d.pop("idempotencyKey", UNSET)

        _metadata = d.pop("metadata", UNSET)
        metadata: RecordSubscriptionUsageBodyMetadata | Unset
        if isinstance(_metadata, Unset):
            metadata = UNSET
        else:
            metadata = RecordSubscriptionUsageBodyMetadata.from_dict(_metadata)

        record_subscription_usage_body = cls(
            quantity=quantity,
            action=action,
            occurred_at=occurred_at,
            idempotency_key=idempotency_key,
            metadata=metadata,
        )

        return record_subscription_usage_body
