from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_balance_response_200_merchant import GetBalanceResponse200Merchant


T = TypeVar("T", bound="GetBalanceResponse200")


@_attrs_define
class GetBalanceResponse200:
    """
    Attributes:
        available_balance (int):
        pending_balance (int):
        blocked_balance (int):
        refunded_balance (int):
        currency (str):
        warranty_balance (int):
        updated_at (str):
        merchant (GetBalanceResponse200Merchant | Unset):
    """

    available_balance: int
    pending_balance: int
    blocked_balance: int
    refunded_balance: int
    currency: str
    warranty_balance: int
    updated_at: str
    merchant: GetBalanceResponse200Merchant | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        available_balance = self.available_balance

        pending_balance = self.pending_balance

        blocked_balance = self.blocked_balance

        refunded_balance = self.refunded_balance

        currency = self.currency

        warranty_balance = self.warranty_balance

        updated_at = self.updated_at

        merchant: dict[str, Any] | Unset = UNSET
        if not isinstance(self.merchant, Unset):
            merchant = self.merchant.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "availableBalance": available_balance,
                "pendingBalance": pending_balance,
                "blockedBalance": blocked_balance,
                "refundedBalance": refunded_balance,
                "currency": currency,
                "warrantyBalance": warranty_balance,
                "updatedAt": updated_at,
            }
        )
        if merchant is not UNSET:
            field_dict["merchant"] = merchant

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_balance_response_200_merchant import (
            GetBalanceResponse200Merchant,
        )

        d = dict(src_dict)
        available_balance = d.pop("availableBalance")

        pending_balance = d.pop("pendingBalance")

        blocked_balance = d.pop("blockedBalance")

        refunded_balance = d.pop("refundedBalance")

        currency = d.pop("currency")

        warranty_balance = d.pop("warrantyBalance")

        updated_at = d.pop("updatedAt")

        _merchant = d.pop("merchant", UNSET)
        merchant: GetBalanceResponse200Merchant | Unset
        if isinstance(_merchant, Unset):
            merchant = UNSET
        else:
            merchant = GetBalanceResponse200Merchant.from_dict(_merchant)

        get_balance_response_200 = cls(
            available_balance=available_balance,
            pending_balance=pending_balance,
            blocked_balance=blocked_balance,
            refunded_balance=refunded_balance,
            currency=currency,
            warranty_balance=warranty_balance,
            updated_at=updated_at,
            merchant=merchant,
        )

        return get_balance_response_200
