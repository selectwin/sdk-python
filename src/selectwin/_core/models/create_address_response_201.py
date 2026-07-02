from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.create_address_response_201_owner_type import (
    CreateAddressResponse201OwnerType,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.create_address_response_201_links import CreateAddressResponse201Links
    from ..models.create_address_response_201_merchant import (
        CreateAddressResponse201Merchant,
    )
    from ..models.create_address_response_201_metadata_type_0 import (
        CreateAddressResponse201MetadataType0,
    )


T = TypeVar("T", bound="CreateAddressResponse201")


@_attrs_define
class CreateAddressResponse201:
    """
    Attributes:
        id (str): Public identifier (addr_/cad_/cadm_/add_…)
        owner_type (CreateAddressResponse201OwnerType):
        owner_id (str):
        street (None | str):
        number (None | str):
        complement (None | str):
        district (None | str):
        city (None | str):
        state (None | str):
        country (None | str):
        postcode (str):
        latitude (None | str):
        longitude (None | str):
        primary (bool):
        line (None | str):
        line1 (None | str):
        line2 (None | str):
        line3 (None | str):
        metadata (CreateAddressResponse201MetadataType0 | None):
        updated_at (str):
        created_at (str):
        merchant (CreateAddressResponse201Merchant | Unset):
        field_links (CreateAddressResponse201Links | Unset):
    """

    id: str
    owner_type: CreateAddressResponse201OwnerType
    owner_id: str
    street: None | str
    number: None | str
    complement: None | str
    district: None | str
    city: None | str
    state: None | str
    country: None | str
    postcode: str
    latitude: None | str
    longitude: None | str
    primary: bool
    line: None | str
    line1: None | str
    line2: None | str
    line3: None | str
    metadata: CreateAddressResponse201MetadataType0 | None
    updated_at: str
    created_at: str
    merchant: CreateAddressResponse201Merchant | Unset = UNSET
    field_links: CreateAddressResponse201Links | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.create_address_response_201_metadata_type_0 import (
            CreateAddressResponse201MetadataType0,
        )

        id = self.id

        owner_type = self.owner_type.value

        owner_id = self.owner_id

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

        postcode = self.postcode

        latitude: None | str
        latitude = self.latitude

        longitude: None | str
        longitude = self.longitude

        primary = self.primary

        line: None | str
        line = self.line

        line1: None | str
        line1 = self.line1

        line2: None | str
        line2 = self.line2

        line3: None | str
        line3 = self.line3

        metadata: dict[str, Any] | None
        if isinstance(self.metadata, CreateAddressResponse201MetadataType0):
            metadata = self.metadata.to_dict()
        else:
            metadata = self.metadata

        updated_at = self.updated_at

        created_at = self.created_at

        merchant: dict[str, Any] | Unset = UNSET
        if not isinstance(self.merchant, Unset):
            merchant = self.merchant.to_dict()

        field_links: dict[str, Any] | Unset = UNSET
        if not isinstance(self.field_links, Unset):
            field_links = self.field_links.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "id": id,
                "ownerType": owner_type,
                "ownerId": owner_id,
                "street": street,
                "number": number,
                "complement": complement,
                "district": district,
                "city": city,
                "state": state,
                "country": country,
                "postcode": postcode,
                "latitude": latitude,
                "longitude": longitude,
                "primary": primary,
                "line": line,
                "line1": line1,
                "line2": line2,
                "line3": line3,
                "metadata": metadata,
                "updatedAt": updated_at,
                "createdAt": created_at,
            }
        )
        if merchant is not UNSET:
            field_dict["merchant"] = merchant
        if field_links is not UNSET:
            field_dict["_links"] = field_links

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.create_address_response_201_links import (
            CreateAddressResponse201Links,
        )
        from ..models.create_address_response_201_merchant import (
            CreateAddressResponse201Merchant,
        )
        from ..models.create_address_response_201_metadata_type_0 import (
            CreateAddressResponse201MetadataType0,
        )

        d = dict(src_dict)
        id = d.pop("id")

        owner_type = CreateAddressResponse201OwnerType(d.pop("ownerType"))

        owner_id = d.pop("ownerId")

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

        postcode = d.pop("postcode")

        def _parse_latitude(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        latitude = _parse_latitude(d.pop("latitude"))

        def _parse_longitude(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        longitude = _parse_longitude(d.pop("longitude"))

        primary = d.pop("primary")

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

        def _parse_metadata(
            data: object,
        ) -> CreateAddressResponse201MetadataType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                metadata_type_0 = CreateAddressResponse201MetadataType0.from_dict(data)

                return metadata_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(CreateAddressResponse201MetadataType0 | None, data)

        metadata = _parse_metadata(d.pop("metadata"))

        updated_at = d.pop("updatedAt")

        created_at = d.pop("createdAt")

        _merchant = d.pop("merchant", UNSET)
        merchant: CreateAddressResponse201Merchant | Unset
        if isinstance(_merchant, Unset):
            merchant = UNSET
        else:
            merchant = CreateAddressResponse201Merchant.from_dict(_merchant)

        _field_links = d.pop("_links", UNSET)
        field_links: CreateAddressResponse201Links | Unset
        if isinstance(_field_links, Unset):
            field_links = UNSET
        else:
            field_links = CreateAddressResponse201Links.from_dict(_field_links)

        create_address_response_201 = cls(
            id=id,
            owner_type=owner_type,
            owner_id=owner_id,
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
            primary=primary,
            line=line,
            line1=line1,
            line2=line2,
            line3=line3,
            metadata=metadata,
            updated_at=updated_at,
            created_at=created_at,
            merchant=merchant,
            field_links=field_links,
        )

        return create_address_response_201
