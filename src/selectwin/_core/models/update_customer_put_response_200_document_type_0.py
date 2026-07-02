from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.update_customer_put_response_200_document_type_0_type import (
    UpdateCustomerPutResponse200DocumentType0Type,
)

T = TypeVar("T", bound="UpdateCustomerPutResponse200DocumentType0")


@_attrs_define
class UpdateCustomerPutResponse200DocumentType0:
    """
    Attributes:
        type_ (UpdateCustomerPutResponse200DocumentType0Type):
        number (None | str):
    """

    type_: UpdateCustomerPutResponse200DocumentType0Type
    number: None | str

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_.value

        number: None | str
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
        type_ = UpdateCustomerPutResponse200DocumentType0Type(d.pop("type"))

        def _parse_number(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        number = _parse_number(d.pop("number"))

        update_customer_put_response_200_document_type_0 = cls(
            type_=type_,
            number=number,
        )

        return update_customer_put_response_200_document_type_0
