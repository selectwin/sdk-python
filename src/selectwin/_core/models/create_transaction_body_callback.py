from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateTransactionBodyCallback")


@_attrs_define
class CreateTransactionBodyCallback:
    """
    Attributes:
        webhook_url (str):
        active (bool | Unset):  Default: True.
    """

    webhook_url: str
    active: bool | Unset = True

    def to_dict(self) -> dict[str, Any]:
        webhook_url = self.webhook_url

        active = self.active

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "webhookUrl": webhook_url,
            }
        )
        if active is not UNSET:
            field_dict["active"] = active

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        webhook_url = d.pop("webhookUrl")

        active = d.pop("active", UNSET)

        create_transaction_body_callback = cls(
            webhook_url=webhook_url,
            active=active,
        )

        return create_transaction_body_callback
