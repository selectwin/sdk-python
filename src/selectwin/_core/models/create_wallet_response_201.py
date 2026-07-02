from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.create_wallet_response_201_links import CreateWalletResponse201Links
    from ..models.create_wallet_response_201_merchant import (
        CreateWalletResponse201Merchant,
    )


T = TypeVar("T", bound="CreateWalletResponse201")


@_attrs_define
class CreateWalletResponse201:
    """
    Attributes:
        id (str): Public identifier (wall_…)
        name (str):
        holder_name (str):
        bank_name (None | str):
        bank_code (None | str):
        routing_number (None | str):
        account_number (None | str):
        account_type (str):
        pix_key (None | str):
        primary (bool):
        enabled (bool):
        created_at (str):
        updated_at (str):
        merchant (CreateWalletResponse201Merchant | Unset):
        field_links (CreateWalletResponse201Links | Unset):
    """

    id: str
    name: str
    holder_name: str
    bank_name: None | str
    bank_code: None | str
    routing_number: None | str
    account_number: None | str
    account_type: str
    pix_key: None | str
    primary: bool
    enabled: bool
    created_at: str
    updated_at: str
    merchant: CreateWalletResponse201Merchant | Unset = UNSET
    field_links: CreateWalletResponse201Links | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        holder_name = self.holder_name

        bank_name: None | str
        bank_name = self.bank_name

        bank_code: None | str
        bank_code = self.bank_code

        routing_number: None | str
        routing_number = self.routing_number

        account_number: None | str
        account_number = self.account_number

        account_type = self.account_type

        pix_key: None | str
        pix_key = self.pix_key

        primary = self.primary

        enabled = self.enabled

        created_at = self.created_at

        updated_at = self.updated_at

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
                "name": name,
                "holderName": holder_name,
                "bankName": bank_name,
                "bankCode": bank_code,
                "routingNumber": routing_number,
                "accountNumber": account_number,
                "accountType": account_type,
                "pixKey": pix_key,
                "primary": primary,
                "enabled": enabled,
                "createdAt": created_at,
                "updatedAt": updated_at,
            }
        )
        if merchant is not UNSET:
            field_dict["merchant"] = merchant
        if field_links is not UNSET:
            field_dict["_links"] = field_links

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.create_wallet_response_201_links import (
            CreateWalletResponse201Links,
        )
        from ..models.create_wallet_response_201_merchant import (
            CreateWalletResponse201Merchant,
        )

        d = dict(src_dict)
        id = d.pop("id")

        name = d.pop("name")

        holder_name = d.pop("holderName")

        def _parse_bank_name(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        bank_name = _parse_bank_name(d.pop("bankName"))

        def _parse_bank_code(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        bank_code = _parse_bank_code(d.pop("bankCode"))

        def _parse_routing_number(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        routing_number = _parse_routing_number(d.pop("routingNumber"))

        def _parse_account_number(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        account_number = _parse_account_number(d.pop("accountNumber"))

        account_type = d.pop("accountType")

        def _parse_pix_key(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        pix_key = _parse_pix_key(d.pop("pixKey"))

        primary = d.pop("primary")

        enabled = d.pop("enabled")

        created_at = d.pop("createdAt")

        updated_at = d.pop("updatedAt")

        _merchant = d.pop("merchant", UNSET)
        merchant: CreateWalletResponse201Merchant | Unset
        if isinstance(_merchant, Unset):
            merchant = UNSET
        else:
            merchant = CreateWalletResponse201Merchant.from_dict(_merchant)

        _field_links = d.pop("_links", UNSET)
        field_links: CreateWalletResponse201Links | Unset
        if isinstance(_field_links, Unset):
            field_links = UNSET
        else:
            field_links = CreateWalletResponse201Links.from_dict(_field_links)

        create_wallet_response_201 = cls(
            id=id,
            name=name,
            holder_name=holder_name,
            bank_name=bank_name,
            bank_code=bank_code,
            routing_number=routing_number,
            account_number=account_number,
            account_type=account_type,
            pix_key=pix_key,
            primary=primary,
            enabled=enabled,
            created_at=created_at,
            updated_at=updated_at,
            merchant=merchant,
            field_links=field_links,
        )

        return create_wallet_response_201
