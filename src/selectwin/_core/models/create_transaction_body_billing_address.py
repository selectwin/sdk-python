from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateTransactionBodyBillingAddress")


@_attrs_define
class CreateTransactionBodyBillingAddress:
    """
    Attributes:
        id (str | Unset): Public identifier (prefix_value)
        postcode (str | Unset):
        street (str | Unset):
        number (str | Unset):
        complement (str | Unset):
        district (str | Unset):
        city (str | Unset):
        state (str | Unset):
        country (str | Unset):
    """

    id: str | Unset = UNSET
    postcode: str | Unset = UNSET
    street: str | Unset = UNSET
    number: str | Unset = UNSET
    complement: str | Unset = UNSET
    district: str | Unset = UNSET
    city: str | Unset = UNSET
    state: str | Unset = UNSET
    country: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        postcode = self.postcode

        street = self.street

        number = self.number

        complement = self.complement

        district = self.district

        city = self.city

        state = self.state

        country = self.country

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if postcode is not UNSET:
            field_dict["postcode"] = postcode
        if street is not UNSET:
            field_dict["street"] = street
        if number is not UNSET:
            field_dict["number"] = number
        if complement is not UNSET:
            field_dict["complement"] = complement
        if district is not UNSET:
            field_dict["district"] = district
        if city is not UNSET:
            field_dict["city"] = city
        if state is not UNSET:
            field_dict["state"] = state
        if country is not UNSET:
            field_dict["country"] = country

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        postcode = d.pop("postcode", UNSET)

        street = d.pop("street", UNSET)

        number = d.pop("number", UNSET)

        complement = d.pop("complement", UNSET)

        district = d.pop("district", UNSET)

        city = d.pop("city", UNSET)

        state = d.pop("state", UNSET)

        country = d.pop("country", UNSET)

        create_transaction_body_billing_address = cls(
            id=id,
            postcode=postcode,
            street=street,
            number=number,
            complement=complement,
            district=district,
            city=city,
            state=state,
            country=country,
        )

        return create_transaction_body_billing_address
