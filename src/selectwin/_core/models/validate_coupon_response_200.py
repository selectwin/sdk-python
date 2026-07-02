from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.validate_coupon_response_200_discount_type_0 import (
        ValidateCouponResponse200DiscountType0,
    )


T = TypeVar("T", bound="ValidateCouponResponse200")


@_attrs_define
class ValidateCouponResponse200:
    """
    Attributes:
        valid (bool):
        reason (None | str):
        code (str):
        discount (None | ValidateCouponResponse200DiscountType0):
        original_amount (int | None):
        charged_amount (int | None):
    """

    valid: bool
    reason: None | str
    code: str
    discount: None | ValidateCouponResponse200DiscountType0
    original_amount: int | None
    charged_amount: int | None

    def to_dict(self) -> dict[str, Any]:
        from ..models.validate_coupon_response_200_discount_type_0 import (
            ValidateCouponResponse200DiscountType0,
        )

        valid = self.valid

        reason: None | str
        reason = self.reason

        code = self.code

        discount: dict[str, Any] | None
        if isinstance(self.discount, ValidateCouponResponse200DiscountType0):
            discount = self.discount.to_dict()
        else:
            discount = self.discount

        original_amount: int | None
        original_amount = self.original_amount

        charged_amount: int | None
        charged_amount = self.charged_amount

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "valid": valid,
                "reason": reason,
                "code": code,
                "discount": discount,
                "originalAmount": original_amount,
                "chargedAmount": charged_amount,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.validate_coupon_response_200_discount_type_0 import (
            ValidateCouponResponse200DiscountType0,
        )

        d = dict(src_dict)
        valid = d.pop("valid")

        def _parse_reason(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        reason = _parse_reason(d.pop("reason"))

        code = d.pop("code")

        def _parse_discount(
            data: object,
        ) -> None | ValidateCouponResponse200DiscountType0:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                discount_type_0 = ValidateCouponResponse200DiscountType0.from_dict(data)

                return discount_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | ValidateCouponResponse200DiscountType0, data)

        discount = _parse_discount(d.pop("discount"))

        def _parse_original_amount(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        original_amount = _parse_original_amount(d.pop("originalAmount"))

        def _parse_charged_amount(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        charged_amount = _parse_charged_amount(d.pop("chargedAmount"))

        validate_coupon_response_200 = cls(
            valid=valid,
            reason=reason,
            code=code,
            discount=discount,
            original_amount=original_amount,
            charged_amount=charged_amount,
        )

        return validate_coupon_response_200
