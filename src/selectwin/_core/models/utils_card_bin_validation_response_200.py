from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.utils_card_bin_validation_response_200_intel_type_0 import (
        UtilsCardBinValidationResponse200IntelType0,
    )
    from ..models.utils_card_bin_validation_response_200_links import (
        UtilsCardBinValidationResponse200Links,
    )
    from ..models.utils_card_bin_validation_response_200_merchant import (
        UtilsCardBinValidationResponse200Merchant,
    )


T = TypeVar("T", bound="UtilsCardBinValidationResponse200")


@_attrs_define
class UtilsCardBinValidationResponse200:
    """
    Attributes:
        valid (bool):
        bin_ (str):
        brand (str):
        length (int):
        luhn_valid (bool | None):
        intel (None | UtilsCardBinValidationResponse200IntelType0):
        merchant (UtilsCardBinValidationResponse200Merchant | Unset):
        field_links (UtilsCardBinValidationResponse200Links | Unset):
    """

    valid: bool
    bin_: str
    brand: str
    length: int
    luhn_valid: bool | None
    intel: None | UtilsCardBinValidationResponse200IntelType0
    merchant: UtilsCardBinValidationResponse200Merchant | Unset = UNSET
    field_links: UtilsCardBinValidationResponse200Links | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.utils_card_bin_validation_response_200_intel_type_0 import (
            UtilsCardBinValidationResponse200IntelType0,
        )

        valid = self.valid

        bin_ = self.bin_

        brand = self.brand

        length = self.length

        luhn_valid: bool | None
        luhn_valid = self.luhn_valid

        intel: dict[str, Any] | None
        if isinstance(self.intel, UtilsCardBinValidationResponse200IntelType0):
            intel = self.intel.to_dict()
        else:
            intel = self.intel

        merchant: dict[str, Any] | Unset = UNSET
        if not isinstance(self.merchant, Unset):
            merchant = self.merchant.to_dict()

        field_links: dict[str, Any] | Unset = UNSET
        if not isinstance(self.field_links, Unset):
            field_links = self.field_links.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "valid": valid,
                "bin": bin_,
                "brand": brand,
                "length": length,
                "luhnValid": luhn_valid,
                "intel": intel,
            }
        )
        if merchant is not UNSET:
            field_dict["merchant"] = merchant
        if field_links is not UNSET:
            field_dict["_links"] = field_links

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.utils_card_bin_validation_response_200_intel_type_0 import (
            UtilsCardBinValidationResponse200IntelType0,
        )
        from ..models.utils_card_bin_validation_response_200_links import (
            UtilsCardBinValidationResponse200Links,
        )
        from ..models.utils_card_bin_validation_response_200_merchant import (
            UtilsCardBinValidationResponse200Merchant,
        )

        d = dict(src_dict)
        valid = d.pop("valid")

        bin_ = d.pop("bin")

        brand = d.pop("brand")

        length = d.pop("length")

        def _parse_luhn_valid(data: object) -> bool | None:
            if data is None:
                return data
            return cast(bool | None, data)

        luhn_valid = _parse_luhn_valid(d.pop("luhnValid"))

        def _parse_intel(
            data: object,
        ) -> None | UtilsCardBinValidationResponse200IntelType0:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                intel_type_0 = UtilsCardBinValidationResponse200IntelType0.from_dict(
                    data
                )

                return intel_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | UtilsCardBinValidationResponse200IntelType0, data)

        intel = _parse_intel(d.pop("intel"))

        _merchant = d.pop("merchant", UNSET)
        merchant: UtilsCardBinValidationResponse200Merchant | Unset
        if isinstance(_merchant, Unset):
            merchant = UNSET
        else:
            merchant = UtilsCardBinValidationResponse200Merchant.from_dict(_merchant)

        _field_links = d.pop("_links", UNSET)
        field_links: UtilsCardBinValidationResponse200Links | Unset
        if isinstance(_field_links, Unset):
            field_links = UNSET
        else:
            field_links = UtilsCardBinValidationResponse200Links.from_dict(_field_links)

        utils_card_bin_validation_response_200 = cls(
            valid=valid,
            bin_=bin_,
            brand=brand,
            length=length,
            luhn_valid=luhn_valid,
            intel=intel,
            merchant=merchant,
            field_links=field_links,
        )

        return utils_card_bin_validation_response_200
