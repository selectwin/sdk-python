from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_receivable_response_200_links import GetReceivableResponse200Links
    from ..models.get_receivable_response_200_merchant import (
        GetReceivableResponse200Merchant,
    )


T = TypeVar("T", bound="GetReceivableResponse200")


@_attrs_define
class GetReceivableResponse200:
    """
    Attributes:
        id (str): Public identifier (rec_…)
        transaction_id (None | str): Public identifier (tra_/trx_…)
        recipient (None | str):
        split (None | str):
        status (str):
        amount (int):
        gross_amount (int):
        antecipation_fee (float | None):
        installment_number (int | None):
        currency (str):
        description (None | str):
        authorization_code (None | str):
        liable (bool | None):
        released (bool | None):
        expected_on (None | str):
        paid_at (None | str):
        refunded_at (None | str):
        canceled_at (None | str):
        charged_back_at (None | str):
        disputed_at (None | str):
        fraud_cheking_at (None | str):
        charge_processing_fee (bool | None):
        created_at (str):
        updated_at (str):
        merchant (GetReceivableResponse200Merchant | Unset):
        field_links (GetReceivableResponse200Links | Unset):
    """

    id: str
    transaction_id: None | str
    recipient: None | str
    split: None | str
    status: str
    amount: int
    gross_amount: int
    antecipation_fee: float | None
    installment_number: int | None
    currency: str
    description: None | str
    authorization_code: None | str
    liable: bool | None
    released: bool | None
    expected_on: None | str
    paid_at: None | str
    refunded_at: None | str
    canceled_at: None | str
    charged_back_at: None | str
    disputed_at: None | str
    fraud_cheking_at: None | str
    charge_processing_fee: bool | None
    created_at: str
    updated_at: str
    merchant: GetReceivableResponse200Merchant | Unset = UNSET
    field_links: GetReceivableResponse200Links | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        transaction_id: None | str
        transaction_id = self.transaction_id

        recipient: None | str
        recipient = self.recipient

        split: None | str
        split = self.split

        status = self.status

        amount = self.amount

        gross_amount = self.gross_amount

        antecipation_fee: float | None
        antecipation_fee = self.antecipation_fee

        installment_number: int | None
        installment_number = self.installment_number

        currency = self.currency

        description: None | str
        description = self.description

        authorization_code: None | str
        authorization_code = self.authorization_code

        liable: bool | None
        liable = self.liable

        released: bool | None
        released = self.released

        expected_on: None | str
        expected_on = self.expected_on

        paid_at: None | str
        paid_at = self.paid_at

        refunded_at: None | str
        refunded_at = self.refunded_at

        canceled_at: None | str
        canceled_at = self.canceled_at

        charged_back_at: None | str
        charged_back_at = self.charged_back_at

        disputed_at: None | str
        disputed_at = self.disputed_at

        fraud_cheking_at: None | str
        fraud_cheking_at = self.fraud_cheking_at

        charge_processing_fee: bool | None
        charge_processing_fee = self.charge_processing_fee

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
                "transactionId": transaction_id,
                "recipient": recipient,
                "split": split,
                "status": status,
                "amount": amount,
                "grossAmount": gross_amount,
                "antecipationFee": antecipation_fee,
                "installmentNumber": installment_number,
                "currency": currency,
                "description": description,
                "authorizationCode": authorization_code,
                "liable": liable,
                "released": released,
                "expectedOn": expected_on,
                "paidAt": paid_at,
                "refundedAt": refunded_at,
                "canceledAt": canceled_at,
                "chargedBackAt": charged_back_at,
                "disputedAt": disputed_at,
                "fraudChekingAt": fraud_cheking_at,
                "chargeProcessingFee": charge_processing_fee,
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
        from ..models.get_receivable_response_200_links import (
            GetReceivableResponse200Links,
        )
        from ..models.get_receivable_response_200_merchant import (
            GetReceivableResponse200Merchant,
        )

        d = dict(src_dict)
        id = d.pop("id")

        def _parse_transaction_id(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        transaction_id = _parse_transaction_id(d.pop("transactionId"))

        def _parse_recipient(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        recipient = _parse_recipient(d.pop("recipient"))

        def _parse_split(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        split = _parse_split(d.pop("split"))

        status = d.pop("status")

        amount = d.pop("amount")

        gross_amount = d.pop("grossAmount")

        def _parse_antecipation_fee(data: object) -> float | None:
            if data is None:
                return data
            return cast(float | None, data)

        antecipation_fee = _parse_antecipation_fee(d.pop("antecipationFee"))

        def _parse_installment_number(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        installment_number = _parse_installment_number(d.pop("installmentNumber"))

        currency = d.pop("currency")

        def _parse_description(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        description = _parse_description(d.pop("description"))

        def _parse_authorization_code(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        authorization_code = _parse_authorization_code(d.pop("authorizationCode"))

        def _parse_liable(data: object) -> bool | None:
            if data is None:
                return data
            return cast(bool | None, data)

        liable = _parse_liable(d.pop("liable"))

        def _parse_released(data: object) -> bool | None:
            if data is None:
                return data
            return cast(bool | None, data)

        released = _parse_released(d.pop("released"))

        def _parse_expected_on(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        expected_on = _parse_expected_on(d.pop("expectedOn"))

        def _parse_paid_at(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        paid_at = _parse_paid_at(d.pop("paidAt"))

        def _parse_refunded_at(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        refunded_at = _parse_refunded_at(d.pop("refundedAt"))

        def _parse_canceled_at(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        canceled_at = _parse_canceled_at(d.pop("canceledAt"))

        def _parse_charged_back_at(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        charged_back_at = _parse_charged_back_at(d.pop("chargedBackAt"))

        def _parse_disputed_at(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        disputed_at = _parse_disputed_at(d.pop("disputedAt"))

        def _parse_fraud_cheking_at(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        fraud_cheking_at = _parse_fraud_cheking_at(d.pop("fraudChekingAt"))

        def _parse_charge_processing_fee(data: object) -> bool | None:
            if data is None:
                return data
            return cast(bool | None, data)

        charge_processing_fee = _parse_charge_processing_fee(
            d.pop("chargeProcessingFee")
        )

        created_at = d.pop("createdAt")

        updated_at = d.pop("updatedAt")

        _merchant = d.pop("merchant", UNSET)
        merchant: GetReceivableResponse200Merchant | Unset
        if isinstance(_merchant, Unset):
            merchant = UNSET
        else:
            merchant = GetReceivableResponse200Merchant.from_dict(_merchant)

        _field_links = d.pop("_links", UNSET)
        field_links: GetReceivableResponse200Links | Unset
        if isinstance(_field_links, Unset):
            field_links = UNSET
        else:
            field_links = GetReceivableResponse200Links.from_dict(_field_links)

        get_receivable_response_200 = cls(
            id=id,
            transaction_id=transaction_id,
            recipient=recipient,
            split=split,
            status=status,
            amount=amount,
            gross_amount=gross_amount,
            antecipation_fee=antecipation_fee,
            installment_number=installment_number,
            currency=currency,
            description=description,
            authorization_code=authorization_code,
            liable=liable,
            released=released,
            expected_on=expected_on,
            paid_at=paid_at,
            refunded_at=refunded_at,
            canceled_at=canceled_at,
            charged_back_at=charged_back_at,
            disputed_at=disputed_at,
            fraud_cheking_at=fraud_cheking_at,
            charge_processing_fee=charge_processing_fee,
            created_at=created_at,
            updated_at=updated_at,
            merchant=merchant,
            field_links=field_links,
        )

        return get_receivable_response_200
