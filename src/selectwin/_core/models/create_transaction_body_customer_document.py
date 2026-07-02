from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..models.create_transaction_body_customer_document_type import (
    CreateTransactionBodyCustomerDocumentType,
)

T = TypeVar("T", bound="CreateTransactionBodyCustomerDocument")


@_attrs_define
class CreateTransactionBodyCustomerDocument:
    """
    Attributes:
        type_ (CreateTransactionBodyCustomerDocumentType):
        number (str):
    """

    type_: CreateTransactionBodyCustomerDocumentType
    number: str

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_.value

        number = self.number

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "type": type_,
                "number": number,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        type_ = CreateTransactionBodyCustomerDocumentType(d.pop("type"))

        number = d.pop("number")

        create_transaction_body_customer_document = cls(
            type_=type_,
            number=number,
        )

        return create_transaction_body_customer_document
