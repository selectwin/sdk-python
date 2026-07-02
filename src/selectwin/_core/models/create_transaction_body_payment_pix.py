from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.create_transaction_body_payment_pix_billing_instructions import (
        CreateTransactionBodyPaymentPixBillingInstructions,
    )


T = TypeVar("T", bound="CreateTransactionBodyPaymentPix")


@_attrs_define
class CreateTransactionBodyPaymentPix:
    """
    Attributes:
        expires_in_minutes (int | Unset):
        expires_in_days (int | Unset):
        billing_instructions (CreateTransactionBodyPaymentPixBillingInstructions | Unset):
    """

    expires_in_minutes: int | Unset = UNSET
    expires_in_days: int | Unset = UNSET
    billing_instructions: CreateTransactionBodyPaymentPixBillingInstructions | Unset = (
        UNSET
    )

    def to_dict(self) -> dict[str, Any]:
        expires_in_minutes = self.expires_in_minutes

        expires_in_days = self.expires_in_days

        billing_instructions: dict[str, Any] | Unset = UNSET
        if not isinstance(self.billing_instructions, Unset):
            billing_instructions = self.billing_instructions.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if expires_in_minutes is not UNSET:
            field_dict["expiresInMinutes"] = expires_in_minutes
        if expires_in_days is not UNSET:
            field_dict["expiresInDays"] = expires_in_days
        if billing_instructions is not UNSET:
            field_dict["billingInstructions"] = billing_instructions

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.create_transaction_body_payment_pix_billing_instructions import (
            CreateTransactionBodyPaymentPixBillingInstructions,
        )

        d = dict(src_dict)
        expires_in_minutes = d.pop("expiresInMinutes", UNSET)

        expires_in_days = d.pop("expiresInDays", UNSET)

        _billing_instructions = d.pop("billingInstructions", UNSET)
        billing_instructions: CreateTransactionBodyPaymentPixBillingInstructions | Unset
        if isinstance(_billing_instructions, Unset):
            billing_instructions = UNSET
        else:
            billing_instructions = (
                CreateTransactionBodyPaymentPixBillingInstructions.from_dict(
                    _billing_instructions
                )
            )

        create_transaction_body_payment_pix = cls(
            expires_in_minutes=expires_in_minutes,
            expires_in_days=expires_in_days,
            billing_instructions=billing_instructions,
        )

        return create_transaction_body_payment_pix
