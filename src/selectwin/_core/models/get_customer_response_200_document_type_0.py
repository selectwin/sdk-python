from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.get_customer_response_200_document_type_0_type import (
    GetCustomerResponse200DocumentType0Type,
)

T = TypeVar("T", bound="GetCustomerResponse200DocumentType0")


@_attrs_define
class GetCustomerResponse200DocumentType0:
    """
    Attributes:
        type_ (GetCustomerResponse200DocumentType0Type):
        number (None | str):
    """

    type_: GetCustomerResponse200DocumentType0Type
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
        type_ = GetCustomerResponse200DocumentType0Type(d.pop("type"))

        def _parse_number(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        number = _parse_number(d.pop("number"))

        get_customer_response_200_document_type_0 = cls(
            type_=type_,
            number=number,
        )

        return get_customer_response_200_document_type_0
