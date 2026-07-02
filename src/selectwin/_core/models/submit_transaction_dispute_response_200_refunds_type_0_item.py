from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

T = TypeVar("T", bound="SubmitTransactionDisputeResponse200RefundsType0Item")


@_attrs_define
class SubmitTransactionDisputeResponse200RefundsType0Item:
    """
    Attributes:
        id (str): Public identifier (void_/trf_/trr_…)
        description (None | str):
        receipt_id (float | None | str):
        amount (int):
        category (None | str):
        observations (None | str):
        updated_at (None | str):
        created_at (None | str):
    """

    id: str
    description: None | str
    receipt_id: float | None | str
    amount: int
    category: None | str
    observations: None | str
    updated_at: None | str
    created_at: None | str

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        description: None | str
        description = self.description

        receipt_id: float | None | str
        receipt_id = self.receipt_id

        amount = self.amount

        category: None | str
        category = self.category

        observations: None | str
        observations = self.observations

        updated_at: None | str
        updated_at = self.updated_at

        created_at: None | str
        created_at = self.created_at

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "id": id,
                "description": description,
                "receiptId": receipt_id,
                "amount": amount,
                "category": category,
                "observations": observations,
                "updatedAt": updated_at,
                "createdAt": created_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        def _parse_description(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        description = _parse_description(d.pop("description"))

        def _parse_receipt_id(data: object) -> float | None | str:
            if data is None:
                return data
            return cast(float | None | str, data)

        receipt_id = _parse_receipt_id(d.pop("receiptId"))

        amount = d.pop("amount")

        def _parse_category(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        category = _parse_category(d.pop("category"))

        def _parse_observations(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        observations = _parse_observations(d.pop("observations"))

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

        submit_transaction_dispute_response_200_refunds_type_0_item = cls(
            id=id,
            description=description,
            receipt_id=receipt_id,
            amount=amount,
            category=category,
            observations=observations,
            updated_at=updated_at,
            created_at=created_at,
        )

        return submit_transaction_dispute_response_200_refunds_type_0_item
