from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..models.create_transaction_body_payment_pix_billing_instructions_discounts_item_mode import (
    CreateTransactionBodyPaymentPixBillingInstructionsDiscountsItemMode,
)
from ..types import UNSET, Unset

T = TypeVar(
    "T", bound="CreateTransactionBodyPaymentPixBillingInstructionsDiscountsItem"
)


@_attrs_define
class CreateTransactionBodyPaymentPixBillingInstructionsDiscountsItem:
    """
    Attributes:
        mode (CreateTransactionBodyPaymentPixBillingInstructionsDiscountsItemMode | Unset):  Default:
            CreateTransactionBodyPaymentPixBillingInstructionsDiscountsItemMode.FIXED.
        amount (int | Unset):
        percentage (float | Unset):
        days_before_due (int | Unset):  Default: 0.
    """

    mode: (
        CreateTransactionBodyPaymentPixBillingInstructionsDiscountsItemMode | Unset
    ) = CreateTransactionBodyPaymentPixBillingInstructionsDiscountsItemMode.FIXED
    amount: int | Unset = UNSET
    percentage: float | Unset = UNSET
    days_before_due: int | Unset = 0

    def to_dict(self) -> dict[str, Any]:
        mode: str | Unset = UNSET
        if not isinstance(self.mode, Unset):
            mode = self.mode.value

        amount = self.amount

        percentage = self.percentage

        days_before_due = self.days_before_due

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if mode is not UNSET:
            field_dict["mode"] = mode
        if amount is not UNSET:
            field_dict["amount"] = amount
        if percentage is not UNSET:
            field_dict["percentage"] = percentage
        if days_before_due is not UNSET:
            field_dict["daysBeforeDue"] = days_before_due

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _mode = d.pop("mode", UNSET)
        mode: (
            CreateTransactionBodyPaymentPixBillingInstructionsDiscountsItemMode | Unset
        )
        if isinstance(_mode, Unset):
            mode = UNSET
        else:
            mode = CreateTransactionBodyPaymentPixBillingInstructionsDiscountsItemMode(
                _mode
            )

        amount = d.pop("amount", UNSET)

        percentage = d.pop("percentage", UNSET)

        days_before_due = d.pop("daysBeforeDue", UNSET)

        create_transaction_body_payment_pix_billing_instructions_discounts_item = cls(
            mode=mode,
            amount=amount,
            percentage=percentage,
            days_before_due=days_before_due,
        )

        return create_transaction_body_payment_pix_billing_instructions_discounts_item
