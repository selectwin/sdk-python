from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="CreateSubscriptionBodyFreeTrial")


@_attrs_define
class CreateSubscriptionBodyFreeTrial:
    """
    Attributes:
        enabled (bool):
        days (int):
    """

    enabled: bool
    days: int

    def to_dict(self) -> dict[str, Any]:
        enabled = self.enabled

        days = self.days

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "enabled": enabled,
                "days": days,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        enabled = d.pop("enabled")

        days = d.pop("days")

        create_subscription_body_free_trial = cls(
            enabled=enabled,
            days=days,
        )

        return create_subscription_body_free_trial
