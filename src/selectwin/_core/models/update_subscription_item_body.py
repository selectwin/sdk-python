from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="UpdateSubscriptionItemBody")


@_attrs_define
class UpdateSubscriptionItemBody:
    """
    Attributes:
        quantity (int):
    """

    quantity: int

    def to_dict(self) -> dict[str, Any]:
        quantity = self.quantity

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "quantity": quantity,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        quantity = d.pop("quantity")

        update_subscription_item_body = cls(
            quantity=quantity,
        )

        return update_subscription_item_body
