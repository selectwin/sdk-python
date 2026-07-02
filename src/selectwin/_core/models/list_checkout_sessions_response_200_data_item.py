from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.list_checkout_sessions_response_200_data_item_object import (
    ListCheckoutSessionsResponse200DataItemObject,
)
from ..models.list_checkout_sessions_response_200_data_item_status import (
    ListCheckoutSessionsResponse200DataItemStatus,
)

T = TypeVar("T", bound="ListCheckoutSessionsResponse200DataItem")


@_attrs_define
class ListCheckoutSessionsResponse200DataItem:
    """
    Attributes:
        object_ (ListCheckoutSessionsResponse200DataItemObject):
        id (str): Public identifier (sess_/ckts_/ses_…)
        status (ListCheckoutSessionsResponse200DataItemStatus):
        source (None | str):
        total_amount (int | None):
        online (bool):
        transaction_id (None | str):
        abandoned_at (None | str):
        completed_at (None | str):
        updated_at (str):
        created_at (str):
    """

    object_: ListCheckoutSessionsResponse200DataItemObject
    id: str
    status: ListCheckoutSessionsResponse200DataItemStatus
    source: None | str
    total_amount: int | None
    online: bool
    transaction_id: None | str
    abandoned_at: None | str
    completed_at: None | str
    updated_at: str
    created_at: str

    def to_dict(self) -> dict[str, Any]:
        object_ = self.object_.value

        id = self.id

        status = self.status.value

        source: None | str
        source = self.source

        total_amount: int | None
        total_amount = self.total_amount

        online = self.online

        transaction_id: None | str
        transaction_id = self.transaction_id

        abandoned_at: None | str
        abandoned_at = self.abandoned_at

        completed_at: None | str
        completed_at = self.completed_at

        updated_at = self.updated_at

        created_at = self.created_at

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "object": object_,
                "id": id,
                "status": status,
                "source": source,
                "totalAmount": total_amount,
                "online": online,
                "transactionId": transaction_id,
                "abandonedAt": abandoned_at,
                "completedAt": completed_at,
                "updatedAt": updated_at,
                "createdAt": created_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        object_ = ListCheckoutSessionsResponse200DataItemObject(d.pop("object"))

        id = d.pop("id")

        status = ListCheckoutSessionsResponse200DataItemStatus(d.pop("status"))

        def _parse_source(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        source = _parse_source(d.pop("source"))

        def _parse_total_amount(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        total_amount = _parse_total_amount(d.pop("totalAmount"))

        online = d.pop("online")

        def _parse_transaction_id(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        transaction_id = _parse_transaction_id(d.pop("transactionId"))

        def _parse_abandoned_at(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        abandoned_at = _parse_abandoned_at(d.pop("abandonedAt"))

        def _parse_completed_at(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        completed_at = _parse_completed_at(d.pop("completedAt"))

        updated_at = d.pop("updatedAt")

        created_at = d.pop("createdAt")

        list_checkout_sessions_response_200_data_item = cls(
            object_=object_,
            id=id,
            status=status,
            source=source,
            total_amount=total_amount,
            online=online,
            transaction_id=transaction_id,
            abandoned_at=abandoned_at,
            completed_at=completed_at,
            updated_at=updated_at,
            created_at=created_at,
        )

        return list_checkout_sessions_response_200_data_item
