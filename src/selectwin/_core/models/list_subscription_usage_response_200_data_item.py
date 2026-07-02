from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

T = TypeVar("T", bound="ListSubscriptionUsageResponse200DataItem")


@_attrs_define
class ListSubscriptionUsageResponse200DataItem:
    """
    Attributes:
        id (str): Public identifier (usg_…)
        item_id (None | str): Public identifier (sit_/item_…)
        meter_event_name (None | str):
        quantity (int):
        action (str):
        occurred_at (str):
        created_at (str):
    """

    id: str
    item_id: None | str
    meter_event_name: None | str
    quantity: int
    action: str
    occurred_at: str
    created_at: str

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        item_id: None | str
        item_id = self.item_id

        meter_event_name: None | str
        meter_event_name = self.meter_event_name

        quantity = self.quantity

        action = self.action

        occurred_at = self.occurred_at

        created_at = self.created_at

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "id": id,
                "itemId": item_id,
                "meterEventName": meter_event_name,
                "quantity": quantity,
                "action": action,
                "occurredAt": occurred_at,
                "createdAt": created_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        def _parse_item_id(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        item_id = _parse_item_id(d.pop("itemId"))

        def _parse_meter_event_name(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        meter_event_name = _parse_meter_event_name(d.pop("meterEventName"))

        quantity = d.pop("quantity")

        action = d.pop("action")

        occurred_at = d.pop("occurredAt")

        created_at = d.pop("createdAt")

        list_subscription_usage_response_200_data_item = cls(
            id=id,
            item_id=item_id,
            meter_event_name=meter_event_name,
            quantity=quantity,
            action=action,
            occurred_at=occurred_at,
            created_at=created_at,
        )

        return list_subscription_usage_response_200_data_item
