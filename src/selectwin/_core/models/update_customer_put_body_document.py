from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..models.update_customer_put_body_document_type import (
    UpdateCustomerPutBodyDocumentType,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="UpdateCustomerPutBodyDocument")


@_attrs_define
class UpdateCustomerPutBodyDocument:
    """
    Attributes:
        type_ (UpdateCustomerPutBodyDocumentType | Unset):
        number (str | Unset):
    """

    type_: UpdateCustomerPutBodyDocumentType | Unset = UNSET
    number: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        number = self.number

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if type_ is not UNSET:
            field_dict["type"] = type_
        if number is not UNSET:
            field_dict["number"] = number

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _type_ = d.pop("type", UNSET)
        type_: UpdateCustomerPutBodyDocumentType | Unset
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = UpdateCustomerPutBodyDocumentType(_type_)

        number = d.pop("number", UNSET)

        update_customer_put_body_document = cls(
            type_=type_,
            number=number,
        )

        return update_customer_put_body_document
