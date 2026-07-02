from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

T = TypeVar("T", bound="GetTransactionResponse200CallbackType0")


@_attrs_define
class GetTransactionResponse200CallbackType0:
    """
    Attributes:
        webhook_url (None | str):
        active (bool | None):
    """

    webhook_url: None | str
    active: bool | None

    def to_dict(self) -> dict[str, Any]:
        webhook_url: None | str
        webhook_url = self.webhook_url

        active: bool | None
        active = self.active

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "webhookUrl": webhook_url,
                "active": active,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_webhook_url(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        webhook_url = _parse_webhook_url(d.pop("webhookUrl"))

        def _parse_active(data: object) -> bool | None:
            if data is None:
                return data
            return cast(bool | None, data)

        active = _parse_active(d.pop("active"))

        get_transaction_response_200_callback_type_0 = cls(
            webhook_url=webhook_url,
            active=active,
        )

        return get_transaction_response_200_callback_type_0
