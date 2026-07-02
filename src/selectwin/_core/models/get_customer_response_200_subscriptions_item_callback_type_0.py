from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="GetCustomerResponse200SubscriptionsItemCallbackType0")


@_attrs_define
class GetCustomerResponse200SubscriptionsItemCallbackType0:
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

        get_customer_response_200_subscriptions_item_callback_type_0 = cls(
            webhook_url=webhook_url,
            active=active,
        )

        return get_customer_response_200_subscriptions_item_callback_type_0
