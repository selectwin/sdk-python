from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="CaptureTransactionBody")


@_attrs_define
class CaptureTransactionBody:
    """
    Attributes:
        amount (int | Unset):
    """

    amount: int | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        amount = self.amount

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if amount is not UNSET:
            field_dict["amount"] = amount

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        amount = d.pop("amount", UNSET)

        capture_transaction_body = cls(
            amount=amount,
        )

        return capture_transaction_body
