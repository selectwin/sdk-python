from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

T = TypeVar("T", bound="GetSubscriptionResponse200DiscountType0")


@_attrs_define
class GetSubscriptionResponse200DiscountType0:
    """
    Attributes:
        value (float):
        type_ (str):
        percentage_of_amount (float | None):
    """

    value: float
    type_: str
    percentage_of_amount: float | None

    def to_dict(self) -> dict[str, Any]:
        value = self.value

        type_ = self.type_

        percentage_of_amount: float | None
        percentage_of_amount = self.percentage_of_amount

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "value": value,
                "type": type_,
                "percentageOfAmount": percentage_of_amount,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        value = d.pop("value")

        type_ = d.pop("type")

        def _parse_percentage_of_amount(data: object) -> float | None:
            if data is None:
                return data
            return cast(float | None, data)

        percentage_of_amount = _parse_percentage_of_amount(d.pop("percentageOfAmount"))

        get_subscription_response_200_discount_type_0 = cls(
            value=value,
            type_=type_,
            percentage_of_amount=percentage_of_amount,
        )

        return get_subscription_response_200_discount_type_0
