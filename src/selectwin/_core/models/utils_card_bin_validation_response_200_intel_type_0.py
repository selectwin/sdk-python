from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

T = TypeVar("T", bound="UtilsCardBinValidationResponse200IntelType0")


@_attrs_define
class UtilsCardBinValidationResponse200IntelType0:
    """
    Attributes:
        scheme (None | str):
        type_ (None | str):
        category (None | str):
        bank (None | str):
        country (None | str):
    """

    scheme: None | str
    type_: None | str
    category: None | str
    bank: None | str
    country: None | str

    def to_dict(self) -> dict[str, Any]:
        scheme: None | str
        scheme = self.scheme

        type_: None | str
        type_ = self.type_

        category: None | str
        category = self.category

        bank: None | str
        bank = self.bank

        country: None | str
        country = self.country

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "scheme": scheme,
                "type": type_,
                "category": category,
                "bank": bank,
                "country": country,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_scheme(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        scheme = _parse_scheme(d.pop("scheme"))

        def _parse_type_(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        type_ = _parse_type_(d.pop("type"))

        def _parse_category(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        category = _parse_category(d.pop("category"))

        def _parse_bank(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        bank = _parse_bank(d.pop("bank"))

        def _parse_country(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        country = _parse_country(d.pop("country"))

        utils_card_bin_validation_response_200_intel_type_0 = cls(
            scheme=scheme,
            type_=type_,
            category=category,
            bank=bank,
            country=country,
        )

        return utils_card_bin_validation_response_200_intel_type_0
