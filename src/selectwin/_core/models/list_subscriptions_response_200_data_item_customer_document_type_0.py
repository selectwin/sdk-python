from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

T = TypeVar("T", bound="ListSubscriptionsResponse200DataItemCustomerDocumentType0")


@_attrs_define
class ListSubscriptionsResponse200DataItemCustomerDocumentType0:
    """
    Attributes:
        type_ (None | str):
        number (None | str):
    """

    type_: None | str
    number: None | str

    def to_dict(self) -> dict[str, Any]:
        type_: None | str
        type_ = self.type_

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

        def _parse_type_(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        type_ = _parse_type_(d.pop("type"))

        def _parse_number(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        number = _parse_number(d.pop("number"))

        list_subscriptions_response_200_data_item_customer_document_type_0 = cls(
            type_=type_,
            number=number,
        )

        return list_subscriptions_response_200_data_item_customer_document_type_0
