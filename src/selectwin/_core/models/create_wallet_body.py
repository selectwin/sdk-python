from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateWalletBody")


@_attrs_define
class CreateWalletBody:
    """
    Attributes:
        name (str):
        bank_code (str):
        routing_number (str):
        account_number (str):
        primary (bool | Unset):
    """

    name: str
    bank_code: str
    routing_number: str
    account_number: str
    primary: bool | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        bank_code = self.bank_code

        routing_number = self.routing_number

        account_number = self.account_number

        primary = self.primary

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "name": name,
                "bankCode": bank_code,
                "routingNumber": routing_number,
                "accountNumber": account_number,
            }
        )
        if primary is not UNSET:
            field_dict["primary"] = primary

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        bank_code = d.pop("bankCode")

        routing_number = d.pop("routingNumber")

        account_number = d.pop("accountNumber")

        primary = d.pop("primary", UNSET)

        create_wallet_body = cls(
            name=name,
            bank_code=bank_code,
            routing_number=routing_number,
            account_number=account_number,
            primary=primary,
        )

        return create_wallet_body
