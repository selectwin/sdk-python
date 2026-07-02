from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="RefundTransactionBody")


@_attrs_define
class RefundTransactionBody:
    """
    Attributes:
        amount (int | Unset):
        reason (str | Unset):
    """

    amount: int | Unset = UNSET
    reason: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        amount = self.amount

        reason = self.reason

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if amount is not UNSET:
            field_dict["amount"] = amount
        if reason is not UNSET:
            field_dict["reason"] = reason

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        amount = d.pop("amount", UNSET)

        reason = d.pop("reason", UNSET)

        refund_transaction_body = cls(
            amount=amount,
            reason=reason,
        )

        return refund_transaction_body
