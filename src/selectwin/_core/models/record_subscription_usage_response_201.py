from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

T = TypeVar("T", bound="RecordSubscriptionUsageResponse201")


@_attrs_define
class RecordSubscriptionUsageResponse201:
    """
    Attributes:
        id (str): Public identifier (usg_…)
        subscription_id (str): Public identifier (subs_/sub_…)
        item_id (str): Public identifier (sit_/item_…)
        meter_event_name (None | str):
        quantity (int):
        action (str):
        idempotent (bool):
    """

    id: str
    subscription_id: str
    item_id: str
    meter_event_name: None | str
    quantity: int
    action: str
    idempotent: bool

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        subscription_id = self.subscription_id

        item_id = self.item_id

        meter_event_name: None | str
        meter_event_name = self.meter_event_name

        quantity = self.quantity

        action = self.action

        idempotent = self.idempotent

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "id": id,
                "subscriptionId": subscription_id,
                "itemId": item_id,
                "meterEventName": meter_event_name,
                "quantity": quantity,
                "action": action,
                "idempotent": idempotent,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        subscription_id = d.pop("subscriptionId")

        item_id = d.pop("itemId")

        def _parse_meter_event_name(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        meter_event_name = _parse_meter_event_name(d.pop("meterEventName"))

        quantity = d.pop("quantity")

        action = d.pop("action")

        idempotent = d.pop("idempotent")

        record_subscription_usage_response_201 = cls(
            id=id,
            subscription_id=subscription_id,
            item_id=item_id,
            meter_event_name=meter_event_name,
            quantity=quantity,
            action=action,
            idempotent=idempotent,
        )

        return record_subscription_usage_response_201
