from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.create_card_body_expiration_year import CreateCardBodyExpirationYear


T = TypeVar("T", bound="CreateCardBody")


@_attrs_define
class CreateCardBody:
    """
    Attributes:
        customer_id (str): Public identifier (cus_…)
        holder_name (str):
        expiration_month (int):
        expiration_year (CreateCardBodyExpirationYear):
        numbering (str):
        security_code (str):
        primary (bool | Unset):
    """

    customer_id: str
    holder_name: str
    expiration_month: int
    expiration_year: CreateCardBodyExpirationYear
    numbering: str
    security_code: str
    primary: bool | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        customer_id = self.customer_id

        holder_name = self.holder_name

        expiration_month = self.expiration_month

        expiration_year = self.expiration_year.to_dict()

        numbering = self.numbering

        security_code = self.security_code

        primary = self.primary

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "customerId": customer_id,
                "holderName": holder_name,
                "expirationMonth": expiration_month,
                "expirationYear": expiration_year,
                "numbering": numbering,
                "securityCode": security_code,
            }
        )
        if primary is not UNSET:
            field_dict["primary"] = primary

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.create_card_body_expiration_year import (
            CreateCardBodyExpirationYear,
        )

        d = dict(src_dict)
        customer_id = d.pop("customerId")

        holder_name = d.pop("holderName")

        expiration_month = d.pop("expirationMonth")

        expiration_year = CreateCardBodyExpirationYear.from_dict(
            d.pop("expirationYear")
        )

        numbering = d.pop("numbering")

        security_code = d.pop("securityCode")

        primary = d.pop("primary", UNSET)

        create_card_body = cls(
            customer_id=customer_id,
            holder_name=holder_name,
            expiration_month=expiration_month,
            expiration_year=expiration_year,
            numbering=numbering,
            security_code=security_code,
            primary=primary,
        )

        return create_card_body
