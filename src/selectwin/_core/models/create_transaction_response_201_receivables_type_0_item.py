from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

T = TypeVar("T", bound="CreateTransactionResponse201ReceivablesType0Item")


@_attrs_define
class CreateTransactionResponse201ReceivablesType0Item:
    """
    Attributes:
        id (None | str):
        recipient (None | str):
        split (None | str):
        status (None | str):
        amount (int):
        gross_amount (int):
        anticipation_fee (int | None):
        installment_number (int | None):
        description (None | str):
        currency (None | str):
        authorization_code (None | str):
        paid_at (None | str):
        refunded_at (None | str):
        canceled_at (None | str):
        expected_on (None | str):
        liable (bool | None):
        charge_processing_fee (bool | None):
        updated_at (None | str):
        created_at (None | str):
    """

    id: None | str
    recipient: None | str
    split: None | str
    status: None | str
    amount: int
    gross_amount: int
    anticipation_fee: int | None
    installment_number: int | None
    description: None | str
    currency: None | str
    authorization_code: None | str
    paid_at: None | str
    refunded_at: None | str
    canceled_at: None | str
    expected_on: None | str
    liable: bool | None
    charge_processing_fee: bool | None
    updated_at: None | str
    created_at: None | str

    def to_dict(self) -> dict[str, Any]:
        id: None | str
        id = self.id

        recipient: None | str
        recipient = self.recipient

        split: None | str
        split = self.split

        status: None | str
        status = self.status

        amount = self.amount

        gross_amount = self.gross_amount

        anticipation_fee: int | None
        anticipation_fee = self.anticipation_fee

        installment_number: int | None
        installment_number = self.installment_number

        description: None | str
        description = self.description

        currency: None | str
        currency = self.currency

        authorization_code: None | str
        authorization_code = self.authorization_code

        paid_at: None | str
        paid_at = self.paid_at

        refunded_at: None | str
        refunded_at = self.refunded_at

        canceled_at: None | str
        canceled_at = self.canceled_at

        expected_on: None | str
        expected_on = self.expected_on

        liable: bool | None
        liable = self.liable

        charge_processing_fee: bool | None
        charge_processing_fee = self.charge_processing_fee

        updated_at: None | str
        updated_at = self.updated_at

        created_at: None | str
        created_at = self.created_at

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "id": id,
                "recipient": recipient,
                "split": split,
                "status": status,
                "amount": amount,
                "grossAmount": gross_amount,
                "anticipationFee": anticipation_fee,
                "installmentNumber": installment_number,
                "description": description,
                "currency": currency,
                "authorizationCode": authorization_code,
                "paidAt": paid_at,
                "refundedAt": refunded_at,
                "canceledAt": canceled_at,
                "expectedOn": expected_on,
                "liable": liable,
                "chargeProcessingFee": charge_processing_fee,
                "updatedAt": updated_at,
                "createdAt": created_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_id(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        id = _parse_id(d.pop("id"))

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

        def _parse_status(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        status = _parse_status(d.pop("status"))

        amount = d.pop("amount")

        gross_amount = d.pop("grossAmount")

        def _parse_anticipation_fee(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        anticipation_fee = _parse_anticipation_fee(d.pop("anticipationFee"))

        def _parse_installment_number(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        installment_number = _parse_installment_number(d.pop("installmentNumber"))

        def _parse_description(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        description = _parse_description(d.pop("description"))

        def _parse_currency(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        currency = _parse_currency(d.pop("currency"))

        def _parse_authorization_code(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        authorization_code = _parse_authorization_code(d.pop("authorizationCode"))

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

        def _parse_expected_on(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        expected_on = _parse_expected_on(d.pop("expectedOn"))

        def _parse_liable(data: object) -> bool | None:
            if data is None:
                return data
            return cast(bool | None, data)

        liable = _parse_liable(d.pop("liable"))

        def _parse_charge_processing_fee(data: object) -> bool | None:
            if data is None:
                return data
            return cast(bool | None, data)

        charge_processing_fee = _parse_charge_processing_fee(
            d.pop("chargeProcessingFee")
        )

        def _parse_updated_at(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        updated_at = _parse_updated_at(d.pop("updatedAt"))

        def _parse_created_at(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        created_at = _parse_created_at(d.pop("createdAt"))

        create_transaction_response_201_receivables_type_0_item = cls(
            id=id,
            recipient=recipient,
            split=split,
            status=status,
            amount=amount,
            gross_amount=gross_amount,
            anticipation_fee=anticipation_fee,
            installment_number=installment_number,
            description=description,
            currency=currency,
            authorization_code=authorization_code,
            paid_at=paid_at,
            refunded_at=refunded_at,
            canceled_at=canceled_at,
            expected_on=expected_on,
            liable=liable,
            charge_processing_fee=charge_processing_fee,
            updated_at=updated_at,
            created_at=created_at,
        )

        return create_transaction_response_201_receivables_type_0_item
