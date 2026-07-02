from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.create_transaction_body_payment_card_expiration_year import (
        CreateTransactionBodyPaymentCardExpirationYear,
    )


T = TypeVar("T", bound="CreateTransactionBodyPaymentCard")


@_attrs_define
class CreateTransactionBodyPaymentCard:
    """
    Attributes:
        id (str | Unset): Public identifier (card_…)
        holder_name (str | Unset):
        expiration_month (int | Unset):
        expiration_year (CreateTransactionBodyPaymentCardExpirationYear | Unset):
        numbering (str | Unset):
        security_code (str | Unset):
    """

    id: str | Unset = UNSET
    holder_name: str | Unset = UNSET
    expiration_month: int | Unset = UNSET
    expiration_year: CreateTransactionBodyPaymentCardExpirationYear | Unset = UNSET
    numbering: str | Unset = UNSET
    security_code: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        holder_name = self.holder_name

        expiration_month = self.expiration_month

        expiration_year: dict[str, Any] | Unset = UNSET
        if not isinstance(self.expiration_year, Unset):
            expiration_year = self.expiration_year.to_dict()

        numbering = self.numbering

        security_code = self.security_code

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if holder_name is not UNSET:
            field_dict["holderName"] = holder_name
        if expiration_month is not UNSET:
            field_dict["expirationMonth"] = expiration_month
        if expiration_year is not UNSET:
            field_dict["expirationYear"] = expiration_year
        if numbering is not UNSET:
            field_dict["numbering"] = numbering
        if security_code is not UNSET:
            field_dict["securityCode"] = security_code

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.create_transaction_body_payment_card_expiration_year import (
            CreateTransactionBodyPaymentCardExpirationYear,
        )

        d = dict(src_dict)
        id = d.pop("id", UNSET)

        holder_name = d.pop("holderName", UNSET)

        expiration_month = d.pop("expirationMonth", UNSET)

        _expiration_year = d.pop("expirationYear", UNSET)
        expiration_year: CreateTransactionBodyPaymentCardExpirationYear | Unset
        if isinstance(_expiration_year, Unset):
            expiration_year = UNSET
        else:
            expiration_year = CreateTransactionBodyPaymentCardExpirationYear.from_dict(
                _expiration_year
            )

        numbering = d.pop("numbering", UNSET)

        security_code = d.pop("securityCode", UNSET)

        create_transaction_body_payment_card = cls(
            id=id,
            holder_name=holder_name,
            expiration_month=expiration_month,
            expiration_year=expiration_year,
            numbering=numbering,
            security_code=security_code,
        )

        return create_transaction_body_payment_card
