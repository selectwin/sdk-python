from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.utils_postcode_validation_response_200_address_type_0 import (
        UtilsPostcodeValidationResponse200AddressType0,
    )
    from ..models.utils_postcode_validation_response_200_merchant import (
        UtilsPostcodeValidationResponse200Merchant,
    )


T = TypeVar("T", bound="UtilsPostcodeValidationResponse200")


@_attrs_define
class UtilsPostcodeValidationResponse200:
    """
    Attributes:
        valid (bool):
        postcode (str):
        country (str):
        street (None | str):
        complement (None | str):
        district (None | str):
        city (None | str):
        state (None | str):
        address (None | UtilsPostcodeValidationResponse200AddressType0):
        merchant (UtilsPostcodeValidationResponse200Merchant | Unset):
    """

    valid: bool
    postcode: str
    country: str
    street: None | str
    complement: None | str
    district: None | str
    city: None | str
    state: None | str
    address: None | UtilsPostcodeValidationResponse200AddressType0
    merchant: UtilsPostcodeValidationResponse200Merchant | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.utils_postcode_validation_response_200_address_type_0 import (
            UtilsPostcodeValidationResponse200AddressType0,
        )

        valid = self.valid

        postcode = self.postcode

        country = self.country

        street: None | str
        street = self.street

        complement: None | str
        complement = self.complement

        district: None | str
        district = self.district

        city: None | str
        city = self.city

        state: None | str
        state = self.state

        address: dict[str, Any] | None
        if isinstance(self.address, UtilsPostcodeValidationResponse200AddressType0):
            address = self.address.to_dict()
        else:
            address = self.address

        merchant: dict[str, Any] | Unset = UNSET
        if not isinstance(self.merchant, Unset):
            merchant = self.merchant.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "valid": valid,
                "postcode": postcode,
                "country": country,
                "street": street,
                "complement": complement,
                "district": district,
                "city": city,
                "state": state,
                "address": address,
            }
        )
        if merchant is not UNSET:
            field_dict["merchant"] = merchant

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.utils_postcode_validation_response_200_address_type_0 import (
            UtilsPostcodeValidationResponse200AddressType0,
        )
        from ..models.utils_postcode_validation_response_200_merchant import (
            UtilsPostcodeValidationResponse200Merchant,
        )

        d = dict(src_dict)
        valid = d.pop("valid")

        postcode = d.pop("postcode")

        country = d.pop("country")

        def _parse_street(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        street = _parse_street(d.pop("street"))

        def _parse_complement(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        complement = _parse_complement(d.pop("complement"))

        def _parse_district(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        district = _parse_district(d.pop("district"))

        def _parse_city(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        city = _parse_city(d.pop("city"))

        def _parse_state(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        state = _parse_state(d.pop("state"))

        def _parse_address(
            data: object,
        ) -> None | UtilsPostcodeValidationResponse200AddressType0:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                address_type_0 = (
                    UtilsPostcodeValidationResponse200AddressType0.from_dict(data)
                )

                return address_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | UtilsPostcodeValidationResponse200AddressType0, data)

        address = _parse_address(d.pop("address"))

        _merchant = d.pop("merchant", UNSET)
        merchant: UtilsPostcodeValidationResponse200Merchant | Unset
        if isinstance(_merchant, Unset):
            merchant = UNSET
        else:
            merchant = UtilsPostcodeValidationResponse200Merchant.from_dict(_merchant)

        utils_postcode_validation_response_200 = cls(
            valid=valid,
            postcode=postcode,
            country=country,
            street=street,
            complement=complement,
            district=district,
            city=city,
            state=state,
            address=address,
            merchant=merchant,
        )

        return utils_postcode_validation_response_200
