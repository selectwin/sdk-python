from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="UpdateCustomerBodyTelephone")


@_attrs_define
class UpdateCustomerBodyTelephone:
    """
    Attributes:
        country_code (str | Unset):
        area_code (str | Unset):
        number (str | Unset):
        line (str | Unset):
    """

    country_code: str | Unset = UNSET
    area_code: str | Unset = UNSET
    number: str | Unset = UNSET
    line: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        country_code = self.country_code

        area_code = self.area_code

        number = self.number

        line = self.line

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if country_code is not UNSET:
            field_dict["countryCode"] = country_code
        if area_code is not UNSET:
            field_dict["areaCode"] = area_code
        if number is not UNSET:
            field_dict["number"] = number
        if line is not UNSET:
            field_dict["line"] = line

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        country_code = d.pop("countryCode", UNSET)

        area_code = d.pop("areaCode", UNSET)

        number = d.pop("number", UNSET)

        line = d.pop("line", UNSET)

        update_customer_body_telephone = cls(
            country_code=country_code,
            area_code=area_code,
            number=number,
            line=line,
        )

        return update_customer_body_telephone
