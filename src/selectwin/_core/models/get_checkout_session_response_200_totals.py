from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="GetCheckoutSessionResponse200Totals")


@_attrs_define
class GetCheckoutSessionResponse200Totals:
    """
    Attributes:
        amount (int):
        discount (int):
        shipping (int):
        tax (int):
    """

    amount: int
    discount: int
    shipping: int
    tax: int

    def to_dict(self) -> dict[str, Any]:
        amount = self.amount

        discount = self.discount

        shipping = self.shipping

        tax = self.tax

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "amount": amount,
                "discount": discount,
                "shipping": shipping,
                "tax": tax,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        amount = d.pop("amount")

        discount = d.pop("discount")

        shipping = d.pop("shipping")

        tax = d.pop("tax")

        get_checkout_session_response_200_totals = cls(
            amount=amount,
            discount=discount,
            shipping=shipping,
            tax=tax,
        )

        return get_checkout_session_response_200_totals
