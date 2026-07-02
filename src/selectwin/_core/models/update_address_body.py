from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.update_address_body_metadata import UpdateAddressBodyMetadata


T = TypeVar("T", bound="UpdateAddressBody")


@_attrs_define
class UpdateAddressBody:
    """
    Attributes:
        street (str | Unset):
        number (str | Unset):
        complement (str | Unset):
        district (str | Unset):
        city (str | Unset):
        state (str | Unset):
        country (str | Unset):
        postcode (str | Unset):
        latitude (str | Unset):
        longitude (str | Unset):
        metadata (UpdateAddressBodyMetadata | Unset):
        primary (bool | Unset):
    """

    street: str | Unset = UNSET
    number: str | Unset = UNSET
    complement: str | Unset = UNSET
    district: str | Unset = UNSET
    city: str | Unset = UNSET
    state: str | Unset = UNSET
    country: str | Unset = UNSET
    postcode: str | Unset = UNSET
    latitude: str | Unset = UNSET
    longitude: str | Unset = UNSET
    metadata: UpdateAddressBodyMetadata | Unset = UNSET
    primary: bool | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        street = self.street

        number = self.number

        complement = self.complement

        district = self.district

        city = self.city

        state = self.state

        country = self.country

        postcode = self.postcode

        latitude = self.latitude

        longitude = self.longitude

        metadata: dict[str, Any] | Unset = UNSET
        if not isinstance(self.metadata, Unset):
            metadata = self.metadata.to_dict()

        primary = self.primary

        field_dict: dict[str, Any] = {}

        field_dict.update({})
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
        if postcode is not UNSET:
            field_dict["postcode"] = postcode
        if latitude is not UNSET:
            field_dict["latitude"] = latitude
        if longitude is not UNSET:
            field_dict["longitude"] = longitude
        if metadata is not UNSET:
            field_dict["metadata"] = metadata
        if primary is not UNSET:
            field_dict["primary"] = primary

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.update_address_body_metadata import UpdateAddressBodyMetadata

        d = dict(src_dict)
        street = d.pop("street", UNSET)

        number = d.pop("number", UNSET)

        complement = d.pop("complement", UNSET)

        district = d.pop("district", UNSET)

        city = d.pop("city", UNSET)

        state = d.pop("state", UNSET)

        country = d.pop("country", UNSET)

        postcode = d.pop("postcode", UNSET)

        latitude = d.pop("latitude", UNSET)

        longitude = d.pop("longitude", UNSET)

        _metadata = d.pop("metadata", UNSET)
        metadata: UpdateAddressBodyMetadata | Unset
        if isinstance(_metadata, Unset):
            metadata = UNSET
        else:
            metadata = UpdateAddressBodyMetadata.from_dict(_metadata)

        primary = d.pop("primary", UNSET)

        update_address_body = cls(
            street=street,
            number=number,
            complement=complement,
            district=district,
            city=city,
            state=state,
            country=country,
            postcode=postcode,
            latitude=latitude,
            longitude=longitude,
            metadata=metadata,
            primary=primary,
        )

        return update_address_body
