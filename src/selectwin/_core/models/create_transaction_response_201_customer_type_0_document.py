from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

T = TypeVar("T", bound="CreateTransactionResponse201CustomerType0Document")


@_attrs_define
class CreateTransactionResponse201CustomerType0Document:
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

        create_transaction_response_201_customer_type_0_document = cls(
            type_=type_,
            number=number,
        )

        return create_transaction_response_201_customer_type_0_document
