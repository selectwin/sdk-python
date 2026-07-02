from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

T = TypeVar("T", bound="PauseSubscriptionResponse200BillingAddress")


@_attrs_define
class PauseSubscriptionResponse200BillingAddress:
    """
    Attributes:
        street (None | str):
        number (None | str):
        complement (None | str):
        district (None | str):
        city (None | str):
        state (None | str):
        country (None | str):
        postcode (None | str):
        line (None | str):
        fingerprint (None | str):
        line1 (None | str):
        line2 (None | str):
        line3 (None | str):
    """

    street: None | str
    number: None | str
    complement: None | str
    district: None | str
    city: None | str
    state: None | str
    country: None | str
    postcode: None | str
    line: None | str
    fingerprint: None | str
    line1: None | str
    line2: None | str
    line3: None | str

    def to_dict(self) -> dict[str, Any]:
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

        country: None | str
        country = self.country

        postcode: None | str
        postcode = self.postcode

        line: None | str
        line = self.line

        fingerprint: None | str
        fingerprint = self.fingerprint

        line1: None | str
        line1 = self.line1

        line2: None | str
        line2 = self.line2

        line3: None | str
        line3 = self.line3

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "street": street,
                "number": number,
                "complement": complement,
                "district": district,
                "city": city,
                "state": state,
                "country": country,
                "postcode": postcode,
                "line": line,
                "fingerprint": fingerprint,
                "line1": line1,
                "line2": line2,
                "line3": line3,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

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

        def _parse_country(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        country = _parse_country(d.pop("country"))

        def _parse_postcode(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        postcode = _parse_postcode(d.pop("postcode"))

        def _parse_line(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        line = _parse_line(d.pop("line"))

        def _parse_fingerprint(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        fingerprint = _parse_fingerprint(d.pop("fingerprint"))

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

        pause_subscription_response_200_billing_address = cls(
            street=street,
            number=number,
            complement=complement,
            district=district,
            city=city,
            state=state,
            country=country,
            postcode=postcode,
            line=line,
            fingerprint=fingerprint,
            line1=line1,
            line2=line2,
            line3=line3,
        )

        return pause_subscription_response_200_billing_address
