from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="UpdateCheckoutPaymentLinkPatchBodyItemsItem")


@_attrs_define
class UpdateCheckoutPaymentLinkPatchBodyItemsItem:
    """
    Attributes:
        id (str): Public identifier (var_/prv_…)
        quantity (int | Unset):  Default: 1.
    """

    id: str
    quantity: int | Unset = 1

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        quantity = self.quantity

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "id": id,
            }
        )
        if quantity is not UNSET:
            field_dict["quantity"] = quantity

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        quantity = d.pop("quantity", UNSET)

        update_checkout_payment_link_patch_body_items_item = cls(
            id=id,
            quantity=quantity,
        )

        return update_checkout_payment_link_patch_body_items_item
