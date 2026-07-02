from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="CreateWithdrawalBody")


@_attrs_define
class CreateWithdrawalBody:
    """
    Attributes:
        amount (int):
        wallet_id (str): Public identifier (wall_…)
    """

    amount: int
    wallet_id: str

    def to_dict(self) -> dict[str, Any]:
        amount = self.amount

        wallet_id = self.wallet_id

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "amount": amount,
                "walletId": wallet_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        amount = d.pop("amount")

        wallet_id = d.pop("walletId")

        create_withdrawal_body = cls(
            amount=amount,
            wallet_id=wallet_id,
        )

        return create_withdrawal_body
