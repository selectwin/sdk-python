from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

T = TypeVar("T", bound="GetSubscriptionCycleUsageResponse200AggregatedByItemItem")


@_attrs_define
class GetSubscriptionCycleUsageResponse200AggregatedByItemItem:
    """
    Attributes:
        item_id (str): Public identifier (sit_/item_…)
        name (None | str):
        meter_event_name (None | str):
        usage (float):
        line_amount (float):
    """

    item_id: str
    name: None | str
    meter_event_name: None | str
    usage: float
    line_amount: float

    def to_dict(self) -> dict[str, Any]:
        item_id = self.item_id

        name: None | str
        name = self.name

        meter_event_name: None | str
        meter_event_name = self.meter_event_name

        usage = self.usage

        line_amount = self.line_amount

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "itemId": item_id,
                "name": name,
                "meterEventName": meter_event_name,
                "usage": usage,
                "lineAmount": line_amount,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        item_id = d.pop("itemId")

        def _parse_name(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        name = _parse_name(d.pop("name"))

        def _parse_meter_event_name(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        meter_event_name = _parse_meter_event_name(d.pop("meterEventName"))

        usage = d.pop("usage")

        line_amount = d.pop("lineAmount")

        get_subscription_cycle_usage_response_200_aggregated_by_item_item = cls(
            item_id=item_id,
            name=name,
            meter_event_name=meter_event_name,
            usage=usage,
            line_amount=line_amount,
        )

        return get_subscription_cycle_usage_response_200_aggregated_by_item_item
