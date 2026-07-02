from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_card_response_200_links import GetCardResponse200Links
    from ..models.get_card_response_200_merchant import GetCardResponse200Merchant


T = TypeVar("T", bound="GetCardResponse200")


@_attrs_define
class GetCardResponse200:
    """
    Attributes:
        id (str): Public identifier (card_…)
        holder_name (None | str):
        brand (str):
        first_digits (str):
        last_digits (str):
        expiration_month (str):
        expiration_year (str):
        primary (bool):
        active (bool):
        valid (bool):
        verified (bool):
        associated (bool):
        updated_at (str):
        created_at (str):
        merchant (GetCardResponse200Merchant | Unset):
        field_links (GetCardResponse200Links | Unset):
    """

    id: str
    holder_name: None | str
    brand: str
    first_digits: str
    last_digits: str
    expiration_month: str
    expiration_year: str
    primary: bool
    active: bool
    valid: bool
    verified: bool
    associated: bool
    updated_at: str
    created_at: str
    merchant: GetCardResponse200Merchant | Unset = UNSET
    field_links: GetCardResponse200Links | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        holder_name: None | str
        holder_name = self.holder_name

        brand = self.brand

        first_digits = self.first_digits

        last_digits = self.last_digits

        expiration_month = self.expiration_month

        expiration_year = self.expiration_year

        primary = self.primary

        active = self.active

        valid = self.valid

        verified = self.verified

        associated = self.associated

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
                "holderName": holder_name,
                "brand": brand,
                "firstDigits": first_digits,
                "lastDigits": last_digits,
                "expirationMonth": expiration_month,
                "expirationYear": expiration_year,
                "primary": primary,
                "active": active,
                "valid": valid,
                "verified": verified,
                "associated": associated,
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
        from ..models.get_card_response_200_links import GetCardResponse200Links
        from ..models.get_card_response_200_merchant import GetCardResponse200Merchant

        d = dict(src_dict)
        id = d.pop("id")

        def _parse_holder_name(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        holder_name = _parse_holder_name(d.pop("holderName"))

        brand = d.pop("brand")

        first_digits = d.pop("firstDigits")

        last_digits = d.pop("lastDigits")

        expiration_month = d.pop("expirationMonth")

        expiration_year = d.pop("expirationYear")

        primary = d.pop("primary")

        active = d.pop("active")

        valid = d.pop("valid")

        verified = d.pop("verified")

        associated = d.pop("associated")

        updated_at = d.pop("updatedAt")

        created_at = d.pop("createdAt")

        _merchant = d.pop("merchant", UNSET)
        merchant: GetCardResponse200Merchant | Unset
        if isinstance(_merchant, Unset):
            merchant = UNSET
        else:
            merchant = GetCardResponse200Merchant.from_dict(_merchant)

        _field_links = d.pop("_links", UNSET)
        field_links: GetCardResponse200Links | Unset
        if isinstance(_field_links, Unset):
            field_links = UNSET
        else:
            field_links = GetCardResponse200Links.from_dict(_field_links)

        get_card_response_200 = cls(
            id=id,
            holder_name=holder_name,
            brand=brand,
            first_digits=first_digits,
            last_digits=last_digits,
            expiration_month=expiration_month,
            expiration_year=expiration_year,
            primary=primary,
            active=active,
            valid=valid,
            verified=verified,
            associated=associated,
            updated_at=updated_at,
            created_at=created_at,
            merchant=merchant,
            field_links=field_links,
        )

        return get_card_response_200
