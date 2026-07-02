from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.create_transaction_response_201_billing_address import (
        CreateTransactionResponse201BillingAddress,
    )


T = TypeVar("T", bound="CreateTransactionResponse201Billing")


@_attrs_define
class CreateTransactionResponse201Billing:
    """
    Attributes:
        address (CreateTransactionResponse201BillingAddress):
    """

    address: CreateTransactionResponse201BillingAddress

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
        from ..models.create_transaction_response_201_billing_address import (
            CreateTransactionResponse201BillingAddress,
        )

        d = dict(src_dict)
        address = CreateTransactionResponse201BillingAddress.from_dict(d.pop("address"))

        create_transaction_response_201_billing = cls(
            address=address,
        )

        return create_transaction_response_201_billing
