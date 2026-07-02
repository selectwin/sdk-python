from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="CreateSubscriptionResponse201CallbackType0")


@_attrs_define
class CreateSubscriptionResponse201CallbackType0:
    """
    Attributes:
        webhook_url (str):
        active (bool):
    """

    webhook_url: str
    active: bool

    def to_dict(self) -> dict[str, Any]:
        webhook_url = self.webhook_url

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
        webhook_url = d.pop("webhookUrl")

        active = d.pop("active")

        create_subscription_response_201_callback_type_0 = cls(
            webhook_url=webhook_url,
            active=active,
        )

        return create_subscription_response_201_callback_type_0
