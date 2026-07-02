from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..models.create_transaction_body_splits_item_type import (
    CreateTransactionBodySplitsItemType,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateTransactionBodySplitsItem")


@_attrs_define
class CreateTransactionBodySplitsItem:
    """
    Attributes:
        recipient_id (str | Unset): Public identifier (prefix_value)
        recipient (str | Unset): Public identifier (prefix_value)
        amount_cents (int | Unset):
        type_ (CreateTransactionBodySplitsItemType | Unset):
        value (float | Unset):
    """

    recipient_id: str | Unset = UNSET
    recipient: str | Unset = UNSET
    amount_cents: int | Unset = UNSET
    type_: CreateTransactionBodySplitsItemType | Unset = UNSET
    value: float | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        recipient_id = self.recipient_id

        recipient = self.recipient

        amount_cents = self.amount_cents

        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        value = self.value

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if recipient_id is not UNSET:
            field_dict["recipientId"] = recipient_id
        if recipient is not UNSET:
            field_dict["recipient"] = recipient
        if amount_cents is not UNSET:
            field_dict["amountCents"] = amount_cents
        if type_ is not UNSET:
            field_dict["type"] = type_
        if value is not UNSET:
            field_dict["value"] = value

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        recipient_id = d.pop("recipientId", UNSET)

        recipient = d.pop("recipient", UNSET)

        amount_cents = d.pop("amountCents", UNSET)

        _type_ = d.pop("type", UNSET)
        type_: CreateTransactionBodySplitsItemType | Unset
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = CreateTransactionBodySplitsItemType(_type_)

        value = d.pop("value", UNSET)

        create_transaction_body_splits_item = cls(
            recipient_id=recipient_id,
            recipient=recipient,
            amount_cents=amount_cents,
            type_=type_,
            value=value,
        )

        return create_transaction_body_splits_item
