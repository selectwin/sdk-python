from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateTransactionBodyItemsItemPricing")


@_attrs_define
class CreateTransactionBodyItemsItemPricing:
    """
    Attributes:
        unit_price (int | Unset):
        quantity (int | Unset):
        currency (str | Unset): ISO 4217 currency code
    """

    unit_price: int | Unset = UNSET
    quantity: int | Unset = UNSET
    currency: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        unit_price = self.unit_price

        quantity = self.quantity

        currency = self.currency

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if unit_price is not UNSET:
            field_dict["unitPrice"] = unit_price
        if quantity is not UNSET:
            field_dict["quantity"] = quantity
        if currency is not UNSET:
            field_dict["currency"] = currency

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        unit_price = d.pop("unitPrice", UNSET)

        quantity = d.pop("quantity", UNSET)

        currency = d.pop("currency", UNSET)

        create_transaction_body_items_item_pricing = cls(
            unit_price=unit_price,
            quantity=quantity,
            currency=currency,
        )

        return create_transaction_body_items_item_pricing
