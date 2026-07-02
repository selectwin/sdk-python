from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.submit_transaction_dispute_response_200_billing_address import (
        SubmitTransactionDisputeResponse200BillingAddress,
    )


T = TypeVar("T", bound="SubmitTransactionDisputeResponse200Billing")


@_attrs_define
class SubmitTransactionDisputeResponse200Billing:
    """
    Attributes:
        address (SubmitTransactionDisputeResponse200BillingAddress):
    """

    address: SubmitTransactionDisputeResponse200BillingAddress

    def to_dict(self) -> dict[str, Any]:
        address = self.address.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "address": address,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.submit_transaction_dispute_response_200_billing_address import (
            SubmitTransactionDisputeResponse200BillingAddress,
        )

        d = dict(src_dict)
        address = SubmitTransactionDisputeResponse200BillingAddress.from_dict(
            d.pop("address")
        )

        submit_transaction_dispute_response_200_billing = cls(
            address=address,
        )

        return submit_transaction_dispute_response_200_billing
