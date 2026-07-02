from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.list_customers_response_200_data_item_document_type_0_type import (
    ListCustomersResponse200DataItemDocumentType0Type,
)

T = TypeVar("T", bound="ListCustomersResponse200DataItemDocumentType0")


@_attrs_define
class ListCustomersResponse200DataItemDocumentType0:
    """
    Attributes:
        type_ (ListCustomersResponse200DataItemDocumentType0Type):
        number (None | str):
    """

    type_: ListCustomersResponse200DataItemDocumentType0Type
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
        type_ = ListCustomersResponse200DataItemDocumentType0Type(d.pop("type"))

        def _parse_number(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        number = _parse_number(d.pop("number"))

        list_customers_response_200_data_item_document_type_0 = cls(
            type_=type_,
            number=number,
        )

        return list_customers_response_200_data_item_document_type_0
