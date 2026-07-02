from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.get_subscription_cycle_usage_response_200_aggregated_by_item_item import (
        GetSubscriptionCycleUsageResponse200AggregatedByItemItem,
    )


T = TypeVar("T", bound="GetSubscriptionCycleUsageResponse200")


@_attrs_define
class GetSubscriptionCycleUsageResponse200:
    """
    Attributes:
        cycle_id (str): Public identifier (scy_/cycle_…)
        window_start (None | str):
        window_end (None | str):
        billed_amount (float | None):
        currency (None | str):
        aggregated_by_item (list[GetSubscriptionCycleUsageResponse200AggregatedByItemItem]):
        total_usage_amount (float):
    """

    cycle_id: str
    window_start: None | str
    window_end: None | str
    billed_amount: float | None
    currency: None | str
    aggregated_by_item: list[GetSubscriptionCycleUsageResponse200AggregatedByItemItem]
    total_usage_amount: float

    def to_dict(self) -> dict[str, Any]:
        cycle_id = self.cycle_id

        window_start: None | str
        window_start = self.window_start

        window_end: None | str
        window_end = self.window_end

        billed_amount: float | None
        billed_amount = self.billed_amount

        currency: None | str
        currency = self.currency

        aggregated_by_item = []
        for aggregated_by_item_item_data in self.aggregated_by_item:
            aggregated_by_item_item = aggregated_by_item_item_data.to_dict()
            aggregated_by_item.append(aggregated_by_item_item)

        total_usage_amount = self.total_usage_amount

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "cycleId": cycle_id,
                "windowStart": window_start,
                "windowEnd": window_end,
                "billedAmount": billed_amount,
                "currency": currency,
                "aggregatedByItem": aggregated_by_item,
                "totalUsageAmount": total_usage_amount,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_subscription_cycle_usage_response_200_aggregated_by_item_item import (
            GetSubscriptionCycleUsageResponse200AggregatedByItemItem,
        )

        d = dict(src_dict)
        cycle_id = d.pop("cycleId")

        def _parse_window_start(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        window_start = _parse_window_start(d.pop("windowStart"))

        def _parse_window_end(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        window_end = _parse_window_end(d.pop("windowEnd"))

        def _parse_billed_amount(data: object) -> float | None:
            if data is None:
                return data
            return cast(float | None, data)

        billed_amount = _parse_billed_amount(d.pop("billedAmount"))

        def _parse_currency(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        currency = _parse_currency(d.pop("currency"))

        aggregated_by_item = []
        _aggregated_by_item = d.pop("aggregatedByItem")
        for aggregated_by_item_item_data in _aggregated_by_item:
            aggregated_by_item_item = (
                GetSubscriptionCycleUsageResponse200AggregatedByItemItem.from_dict(
                    aggregated_by_item_item_data
                )
            )

            aggregated_by_item.append(aggregated_by_item_item)

        total_usage_amount = d.pop("totalUsageAmount")

        get_subscription_cycle_usage_response_200 = cls(
            cycle_id=cycle_id,
            window_start=window_start,
            window_end=window_end,
            billed_amount=billed_amount,
            currency=currency,
            aggregated_by_item=aggregated_by_item,
            total_usage_amount=total_usage_amount,
        )

        return get_subscription_cycle_usage_response_200
