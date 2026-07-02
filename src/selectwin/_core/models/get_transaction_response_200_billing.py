from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.get_transaction_response_200_billing_address import (
        GetTransactionResponse200BillingAddress,
    )


T = TypeVar("T", bound="GetTransactionResponse200Billing")


@_attrs_define
class GetTransactionResponse200Billing:
    """
    Attributes:
        address (GetTransactionResponse200BillingAddress):
    """

    address: GetTransactionResponse200BillingAddress

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
        from ..models.get_transaction_response_200_billing_address import (
            GetTransactionResponse200BillingAddress,
        )

        d = dict(src_dict)
        address = GetTransactionResponse200BillingAddress.from_dict(d.pop("address"))

        get_transaction_response_200_billing = cls(
            address=address,
        )

        return get_transaction_response_200_billing
