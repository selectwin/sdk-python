from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

T = TypeVar("T", bound="UtilsCorporateDocumentCheckResponse200AddressType0")


@_attrs_define
class UtilsCorporateDocumentCheckResponse200AddressType0:
    """
    Attributes:
        postcode (None | str):
        street (None | str):
        number (None | str):
        complement (None | str):
        district (None | str):
        city (None | str):
        state (None | str):
        country (str):
    """

    postcode: None | str
    street: None | str
    number: None | str
    complement: None | str
    district: None | str
    city: None | str
    state: None | str
    country: str

    def to_dict(self) -> dict[str, Any]:
        postcode: None | str
        postcode = self.postcode

        street: None | str
        street = self.street

        number: None | str
        number = self.number

        complement: None | str
        complement = self.complement

        district: None | str
        district = self.district

        city: None | str
        city = self.city

        state: None | str
        state = self.state

        country = self.country

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "postcode": postcode,
                "street": street,
                "number": number,
                "complement": complement,
                "district": district,
                "city": city,
                "state": state,
                "country": country,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_postcode(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        postcode = _parse_postcode(d.pop("postcode"))

        def _parse_street(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        street = _parse_street(d.pop("street"))

        def _parse_number(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        number = _parse_number(d.pop("number"))

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

        country = d.pop("country")

        utils_corporate_document_check_response_200_address_type_0 = cls(
            postcode=postcode,
            street=street,
            number=number,
            complement=complement,
            district=district,
            city=city,
            state=state,
            country=country,
        )

        return utils_corporate_document_check_response_200_address_type_0
