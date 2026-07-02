from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..models.validate_coupon_response_200_discount_type_0_type import (
    ValidateCouponResponse200DiscountType0Type,
)

T = TypeVar("T", bound="ValidateCouponResponse200DiscountType0")


@_attrs_define
class ValidateCouponResponse200DiscountType0:
    """
    Attributes:
        type_ (ValidateCouponResponse200DiscountType0Type):
        value (int):
        percentage (float):
    """

    type_: ValidateCouponResponse200DiscountType0Type
    value: int
    percentage: float

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_.value

        value = self.value

        percentage = self.percentage

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "type": type_,
                "value": value,
                "percentage": percentage,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        type_ = ValidateCouponResponse200DiscountType0Type(d.pop("type"))

        value = d.pop("value")

        percentage = d.pop("percentage")

        validate_coupon_response_200_discount_type_0 = cls(
            type_=type_,
            value=value,
            percentage=percentage,
        )

        return validate_coupon_response_200_discount_type_0
