from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

T = TypeVar("T", bound="GetTransactionResponse200BillingAddress")


@_attrs_define
class GetTransactionResponse200BillingAddress:
    """
    Attributes:
        id (None | str):
        owner_id (None | str):
        owner_type (None | str):
        street (None | str):
        number (None | str):
        complement (None | str):
        district (None | str):
        city (None | str):
        state (None | str):
        postcode (None | str):
        country (None | str):
        latitude (float | None | str):
        longitude (float | None | str):
        line (None | str):
        line1 (None | str):
        line2 (None | str):
        line3 (None | str):
        updated_at (None | str):
        created_at (None | str):
    """

    id: None | str
    owner_id: None | str
    owner_type: None | str
    street: None | str
    number: None | str
    complement: None | str
    district: None | str
    city: None | str
    state: None | str
    postcode: None | str
    country: None | str
    latitude: float | None | str
    longitude: float | None | str
    line: None | str
    line1: None | str
    line2: None | str
    line3: None | str
    updated_at: None | str
    created_at: None | str

    def to_dict(self) -> dict[str, Any]:
        id: None | str
        id = self.id

        owner_id: None | str
        owner_id = self.owner_id

        owner_type: None | str
        owner_type = self.owner_type

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

        postcode: None | str
        postcode = self.postcode

        country: None | str
        country = self.country

        latitude: float | None | str
        latitude = self.latitude

        longitude: float | None | str
        longitude = self.longitude

        line: None | str
        line = self.line

        line1: None | str
        line1 = self.line1

        line2: None | str
        line2 = self.line2

        line3: None | str
        line3 = self.line3

        updated_at: None | str
        updated_at = self.updated_at

        created_at: None | str
        created_at = self.created_at

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "id": id,
                "ownerId": owner_id,
                "ownerType": owner_type,
                "street": street,
                "number": number,
                "complement": complement,
                "district": district,
                "city": city,
                "state": state,
                "postcode": postcode,
                "country": country,
                "latitude": latitude,
                "longitude": longitude,
                "line": line,
                "line1": line1,
                "line2": line2,
                "line3": line3,
                "updatedAt": updated_at,
                "createdAt": created_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_id(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        id = _parse_id(d.pop("id"))

        def _parse_owner_id(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        owner_id = _parse_owner_id(d.pop("ownerId"))

        def _parse_owner_type(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        owner_type = _parse_owner_type(d.pop("ownerType"))

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

        def _parse_postcode(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        postcode = _parse_postcode(d.pop("postcode"))

        def _parse_country(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        country = _parse_country(d.pop("country"))

        def _parse_latitude(data: object) -> float | None | str:
            if data is None:
                return data
            return cast(float | None | str, data)

        latitude = _parse_latitude(d.pop("latitude"))

        def _parse_longitude(data: object) -> float | None | str:
            if data is None:
                return data
            return cast(float | None | str, data)

        longitude = _parse_longitude(d.pop("longitude"))

        def _parse_line(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        line = _parse_line(d.pop("line"))

        def _parse_line1(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        line1 = _parse_line1(d.pop("line1"))

        def _parse_line2(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        line2 = _parse_line2(d.pop("line2"))

        def _parse_line3(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        line3 = _parse_line3(d.pop("line3"))

        def _parse_updated_at(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        updated_at = _parse_updated_at(d.pop("updatedAt"))

        def _parse_created_at(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        created_at = _parse_created_at(d.pop("createdAt"))

        get_transaction_response_200_billing_address = cls(
            id=id,
            owner_id=owner_id,
            owner_type=owner_type,
            street=street,
            number=number,
            complement=complement,
            district=district,
            city=city,
            state=state,
            postcode=postcode,
            country=country,
            latitude=latitude,
            longitude=longitude,
            line=line,
            line1=line1,
            line2=line2,
            line3=line3,
            updated_at=updated_at,
            created_at=created_at,
        )

        return get_transaction_response_200_billing_address
