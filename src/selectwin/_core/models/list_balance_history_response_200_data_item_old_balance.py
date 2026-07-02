from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="ListBalanceHistoryResponse200DataItemOldBalance")


@_attrs_define
class ListBalanceHistoryResponse200DataItemOldBalance:
    """
    Attributes:
        available_balance (int):
        pending_balance (int):
        blocked_balance (int):
        refunded_balance (int):
    """

    available_balance: int
    pending_balance: int
    blocked_balance: int
    refunded_balance: int

    def to_dict(self) -> dict[str, Any]:
        available_balance = self.available_balance

        pending_balance = self.pending_balance

        blocked_balance = self.blocked_balance

        refunded_balance = self.refunded_balance

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "availableBalance": available_balance,
                "pendingBalance": pending_balance,
                "blockedBalance": blocked_balance,
                "refundedBalance": refunded_balance,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        available_balance = d.pop("availableBalance")

        pending_balance = d.pop("pendingBalance")

        blocked_balance = d.pop("blockedBalance")

        refunded_balance = d.pop("refundedBalance")

        list_balance_history_response_200_data_item_old_balance = cls(
            available_balance=available_balance,
            pending_balance=pending_balance,
            blocked_balance=blocked_balance,
            refunded_balance=refunded_balance,
        )

        return list_balance_history_response_200_data_item_old_balance
