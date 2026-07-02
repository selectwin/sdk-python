from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.list_webhook_dispatches_response_200_data_item_status import (
    ListWebhookDispatchesResponse200DataItemStatus,
)

T = TypeVar("T", bound="ListWebhookDispatchesResponse200DataItem")


@_attrs_define
class ListWebhookDispatchesResponse200DataItem:
    """
    Attributes:
        id (str): Public identifier (wdi_…)
        event_id (None | str): Public identifier (wbh_…)
        endpoint_id (None | str): Public identifier (wbe_/wbh_…)
        endpoint (str):
        status (ListWebhookDispatchesResponse200DataItemStatus):
        attempts (int):
        response_status_code (int | None):
        response_time (int | None):
        next_attempt_at (None | str):
        last_attempt_at (None | str):
        success_at (None | str):
        created_at (str):
    """

    id: str
    event_id: None | str
    endpoint_id: None | str
    endpoint: str
    status: ListWebhookDispatchesResponse200DataItemStatus
    attempts: int
    response_status_code: int | None
    response_time: int | None
    next_attempt_at: None | str
    last_attempt_at: None | str
    success_at: None | str
    created_at: str

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        event_id: None | str
        event_id = self.event_id

        endpoint_id: None | str
        endpoint_id = self.endpoint_id

        endpoint = self.endpoint

        status = self.status.value

        attempts = self.attempts

        response_status_code: int | None
        response_status_code = self.response_status_code

        response_time: int | None
        response_time = self.response_time

        next_attempt_at: None | str
        next_attempt_at = self.next_attempt_at

        last_attempt_at: None | str
        last_attempt_at = self.last_attempt_at

        success_at: None | str
        success_at = self.success_at

        created_at = self.created_at

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "id": id,
                "eventId": event_id,
                "endpointId": endpoint_id,
                "endpoint": endpoint,
                "status": status,
                "attempts": attempts,
                "responseStatusCode": response_status_code,
                "responseTime": response_time,
                "nextAttemptAt": next_attempt_at,
                "lastAttemptAt": last_attempt_at,
                "successAt": success_at,
                "createdAt": created_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        def _parse_event_id(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        event_id = _parse_event_id(d.pop("eventId"))

        def _parse_endpoint_id(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        endpoint_id = _parse_endpoint_id(d.pop("endpointId"))

        endpoint = d.pop("endpoint")

        status = ListWebhookDispatchesResponse200DataItemStatus(d.pop("status"))

        attempts = d.pop("attempts")

        def _parse_response_status_code(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        response_status_code = _parse_response_status_code(d.pop("responseStatusCode"))

        def _parse_response_time(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        response_time = _parse_response_time(d.pop("responseTime"))

        def _parse_next_attempt_at(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        next_attempt_at = _parse_next_attempt_at(d.pop("nextAttemptAt"))

        def _parse_last_attempt_at(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        last_attempt_at = _parse_last_attempt_at(d.pop("lastAttemptAt"))

        def _parse_success_at(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        success_at = _parse_success_at(d.pop("successAt"))

        created_at = d.pop("createdAt")

        list_webhook_dispatches_response_200_data_item = cls(
            id=id,
            event_id=event_id,
            endpoint_id=endpoint_id,
            endpoint=endpoint,
            status=status,
            attempts=attempts,
            response_status_code=response_status_code,
            response_time=response_time,
            next_attempt_at=next_attempt_at,
            last_attempt_at=last_attempt_at,
            success_at=success_at,
            created_at=created_at,
        )

        return list_webhook_dispatches_response_200_data_item
