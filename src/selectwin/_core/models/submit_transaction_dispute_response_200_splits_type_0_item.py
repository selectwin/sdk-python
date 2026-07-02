from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

T = TypeVar("T", bound="SubmitTransactionDisputeResponse200SplitsType0Item")


@_attrs_define
class SubmitTransactionDisputeResponse200SplitsType0Item:
    """
    Attributes:
        id (None | str):
        recipient (None | str):
        receivable (None | str):
        amount (int):
        gross_amount (int):
        percentage (float | None | str):
        description (None | str):
        charge_processing_fee (bool | None):
        updated_at (None | str):
        created_at (None | str):
    """

    id: None | str
    recipient: None | str
    receivable: None | str
    amount: int
    gross_amount: int
    percentage: float | None | str
    description: None | str
    charge_processing_fee: bool | None
    updated_at: None | str
    created_at: None | str

    def to_dict(self) -> dict[str, Any]:
        id: None | str
        id = self.id

        recipient: None | str
        recipient = self.recipient

        receivable: None | str
        receivable = self.receivable

        amount = self.amount

        gross_amount = self.gross_amount

        percentage: float | None | str
        percentage = self.percentage

        description: None | str
        description = self.description

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
                "receivable": receivable,
                "amount": amount,
                "grossAmount": gross_amount,
                "percentage": percentage,
                "description": description,
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

        def _parse_receivable(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        receivable = _parse_receivable(d.pop("receivable"))

        amount = d.pop("amount")

        gross_amount = d.pop("grossAmount")

        def _parse_percentage(data: object) -> float | None | str:
            if data is None:
                return data
            return cast(float | None | str, data)

        percentage = _parse_percentage(d.pop("percentage"))

        def _parse_description(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        description = _parse_description(d.pop("description"))

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

        submit_transaction_dispute_response_200_splits_type_0_item = cls(
            id=id,
            recipient=recipient,
            receivable=receivable,
            amount=amount,
            gross_amount=gross_amount,
            percentage=percentage,
            description=description,
            charge_processing_fee=charge_processing_fee,
            updated_at=updated_at,
            created_at=created_at,
        )

        return submit_transaction_dispute_response_200_splits_type_0_item
