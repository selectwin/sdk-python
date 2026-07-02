from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

T = TypeVar("T", bound="UtilsPostcodeValidationResponse200AddressType0")


@_attrs_define
class UtilsPostcodeValidationResponse200AddressType0:
    """
    Attributes:
        postcode (str):
        street (None | str):
        complement (None | str):
        district (None | str):
        city (str):
        state (str):
    """

    postcode: str
    street: None | str
    complement: None | str
    district: None | str
    city: str
    state: str

    def to_dict(self) -> dict[str, Any]:
        postcode = self.postcode

        street: None | str
        street = self.street

        complement: None | str
        complement = self.complement

        district: None | str
        district = self.district

        city = self.city

        state = self.state

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "postcode": postcode,
                "street": street,
                "complement": complement,
                "district": district,
                "city": city,
                "state": state,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        postcode = d.pop("postcode")

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

        city = d.pop("city")

        state = d.pop("state")

        utils_postcode_validation_response_200_address_type_0 = cls(
            postcode=postcode,
            street=street,
            complement=complement,
            district=district,
            city=city,
            state=state,
        )

        return utils_postcode_validation_response_200_address_type_0
