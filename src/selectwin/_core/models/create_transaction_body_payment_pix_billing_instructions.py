from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.create_transaction_body_payment_pix_billing_instructions_discounts_item import (
        CreateTransactionBodyPaymentPixBillingInstructionsDiscountsItem,
    )
    from ..models.create_transaction_body_payment_pix_billing_instructions_interest import (
        CreateTransactionBodyPaymentPixBillingInstructionsInterest,
    )
    from ..models.create_transaction_body_payment_pix_billing_instructions_late_fee import (
        CreateTransactionBodyPaymentPixBillingInstructionsLateFee,
    )


T = TypeVar("T", bound="CreateTransactionBodyPaymentPixBillingInstructions")


@_attrs_define
class CreateTransactionBodyPaymentPixBillingInstructions:
    """
    Attributes:
        late_fee (CreateTransactionBodyPaymentPixBillingInstructionsLateFee | Unset):
        interest (CreateTransactionBodyPaymentPixBillingInstructionsInterest | Unset):
        discounts (list[CreateTransactionBodyPaymentPixBillingInstructionsDiscountsItem] | Unset):
    """

    late_fee: CreateTransactionBodyPaymentPixBillingInstructionsLateFee | Unset = UNSET
    interest: CreateTransactionBodyPaymentPixBillingInstructionsInterest | Unset = UNSET
    discounts: (
        list[CreateTransactionBodyPaymentPixBillingInstructionsDiscountsItem] | Unset
    ) = UNSET

    def to_dict(self) -> dict[str, Any]:
        late_fee: dict[str, Any] | Unset = UNSET
        if not isinstance(self.late_fee, Unset):
            late_fee = self.late_fee.to_dict()

        interest: dict[str, Any] | Unset = UNSET
        if not isinstance(self.interest, Unset):
            interest = self.interest.to_dict()

        discounts: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.discounts, Unset):
            discounts = []
            for discounts_item_data in self.discounts:
                discounts_item = discounts_item_data.to_dict()
                discounts.append(discounts_item)

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if late_fee is not UNSET:
            field_dict["lateFee"] = late_fee
        if interest is not UNSET:
            field_dict["interest"] = interest
        if discounts is not UNSET:
            field_dict["discounts"] = discounts

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.create_transaction_body_payment_pix_billing_instructions_discounts_item import (
            CreateTransactionBodyPaymentPixBillingInstructionsDiscountsItem,
        )
        from ..models.create_transaction_body_payment_pix_billing_instructions_interest import (
            CreateTransactionBodyPaymentPixBillingInstructionsInterest,
        )
        from ..models.create_transaction_body_payment_pix_billing_instructions_late_fee import (
            CreateTransactionBodyPaymentPixBillingInstructionsLateFee,
        )

        d = dict(src_dict)
        _late_fee = d.pop("lateFee", UNSET)
        late_fee: CreateTransactionBodyPaymentPixBillingInstructionsLateFee | Unset
        if isinstance(_late_fee, Unset):
            late_fee = UNSET
        else:
            late_fee = (
                CreateTransactionBodyPaymentPixBillingInstructionsLateFee.from_dict(
                    _late_fee
                )
            )

        _interest = d.pop("interest", UNSET)
        interest: CreateTransactionBodyPaymentPixBillingInstructionsInterest | Unset
        if isinstance(_interest, Unset):
            interest = UNSET
        else:
            interest = (
                CreateTransactionBodyPaymentPixBillingInstructionsInterest.from_dict(
                    _interest
                )
            )

        _discounts = d.pop("discounts", UNSET)
        discounts: (
            list[CreateTransactionBodyPaymentPixBillingInstructionsDiscountsItem]
            | Unset
        ) = UNSET
        if _discounts is not UNSET:
            discounts = []
            for discounts_item_data in _discounts:
                discounts_item = CreateTransactionBodyPaymentPixBillingInstructionsDiscountsItem.from_dict(
                    discounts_item_data
                )

                discounts.append(discounts_item)

        create_transaction_body_payment_pix_billing_instructions = cls(
            late_fee=late_fee,
            interest=interest,
            discounts=discounts,
        )

        return create_transaction_body_payment_pix_billing_instructions
