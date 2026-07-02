from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

T = TypeVar("T", bound="GetTransactionResponse200TimelineItem")


@_attrs_define
class GetTransactionResponse200TimelineItem:
    """
    Attributes:
        id (None | str):
        message (None | str):
        details (None | str):
        type_ (None | str):
        updated_at (None | str):
        created_at (None | str):
    """

    id: None | str
    message: None | str
    details: None | str
    type_: None | str
    updated_at: None | str
    created_at: None | str

    def to_dict(self) -> dict[str, Any]:
        id: None | str
        id = self.id

        message: None | str
        message = self.message

        details: None | str
        details = self.details

        type_: None | str
        type_ = self.type_

        updated_at: None | str
        updated_at = self.updated_at

        created_at: None | str
        created_at = self.created_at

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "id": id,
                "message": message,
                "details": details,
                "type": type_,
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

        def _parse_message(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        message = _parse_message(d.pop("message"))

        def _parse_details(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        details = _parse_details(d.pop("details"))

        def _parse_type_(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        type_ = _parse_type_(d.pop("type"))

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

        get_transaction_response_200_timeline_item = cls(
            id=id,
            message=message,
            details=details,
            type_=type_,
            updated_at=updated_at,
            created_at=created_at,
        )

        return get_transaction_response_200_timeline_item
