from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="ValidateCouponBody")


@_attrs_define
class ValidateCouponBody:
    """
    Attributes:
        code (str):
        amount (int):
        item_count (int | Unset):
        item_ids (list[str] | Unset):
        customer_id (str | Unset): Public identifier (cus_…)
    """

    code: str
    amount: int
    item_count: int | Unset = UNSET
    item_ids: list[str] | Unset = UNSET
    customer_id: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        code = self.code

        amount = self.amount

        item_count = self.item_count

        item_ids: list[str] | Unset = UNSET
        if not isinstance(self.item_ids, Unset):
            item_ids = self.item_ids

        customer_id = self.customer_id

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "code": code,
                "amount": amount,
            }
        )
        if item_count is not UNSET:
            field_dict["itemCount"] = item_count
        if item_ids is not UNSET:
            field_dict["itemIds"] = item_ids
        if customer_id is not UNSET:
            field_dict["customerId"] = customer_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        code = d.pop("code")

        amount = d.pop("amount")

        item_count = d.pop("itemCount", UNSET)

        item_ids = cast(list[str], d.pop("itemIds", UNSET))

        customer_id = d.pop("customerId", UNSET)

        validate_coupon_body = cls(
            code=code,
            amount=amount,
            item_count=item_count,
            item_ids=item_ids,
            customer_id=customer_id,
        )

        return validate_coupon_body
