from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..models.create_subscription_body_customer_document_type import (
    CreateSubscriptionBodyCustomerDocumentType,
)

T = TypeVar("T", bound="CreateSubscriptionBodyCustomerDocument")


@_attrs_define
class CreateSubscriptionBodyCustomerDocument:
    """
    Attributes:
        type_ (CreateSubscriptionBodyCustomerDocumentType):
        number (str):
    """

    type_: CreateSubscriptionBodyCustomerDocumentType
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
        type_ = CreateSubscriptionBodyCustomerDocumentType(d.pop("type"))

        number = d.pop("number")

        create_subscription_body_customer_document = cls(
            type_=type_,
            number=number,
        )

        return create_subscription_body_customer_document
