from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..models.create_transaction_body_payment_pix_billing_instructions_late_fee_mode import (
    CreateTransactionBodyPaymentPixBillingInstructionsLateFeeMode,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateTransactionBodyPaymentPixBillingInstructionsLateFee")


@_attrs_define
class CreateTransactionBodyPaymentPixBillingInstructionsLateFee:
    """
    Attributes:
        mode (CreateTransactionBodyPaymentPixBillingInstructionsLateFeeMode | Unset):  Default:
            CreateTransactionBodyPaymentPixBillingInstructionsLateFeeMode.FIXED.
        amount (int | Unset):
        percentage (float | Unset):
        start_days (int | Unset):
    """

    mode: CreateTransactionBodyPaymentPixBillingInstructionsLateFeeMode | Unset = (
        CreateTransactionBodyPaymentPixBillingInstructionsLateFeeMode.FIXED
    )
    amount: int | Unset = UNSET
    percentage: float | Unset = UNSET
    start_days: int | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        mode: str | Unset = UNSET
        if not isinstance(self.mode, Unset):
            mode = self.mode.value

        amount = self.amount

        percentage = self.percentage

        start_days = self.start_days

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if mode is not UNSET:
            field_dict["mode"] = mode
        if amount is not UNSET:
            field_dict["amount"] = amount
        if percentage is not UNSET:
            field_dict["percentage"] = percentage
        if start_days is not UNSET:
            field_dict["startDays"] = start_days

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _mode = d.pop("mode", UNSET)
        mode: CreateTransactionBodyPaymentPixBillingInstructionsLateFeeMode | Unset
        if isinstance(_mode, Unset):
            mode = UNSET
        else:
            mode = CreateTransactionBodyPaymentPixBillingInstructionsLateFeeMode(_mode)

        amount = d.pop("amount", UNSET)

        percentage = d.pop("percentage", UNSET)

        start_days = d.pop("startDays", UNSET)

        create_transaction_body_payment_pix_billing_instructions_late_fee = cls(
            mode=mode,
            amount=amount,
            percentage=percentage,
            start_days=start_days,
        )

        return create_transaction_body_payment_pix_billing_instructions_late_fee
