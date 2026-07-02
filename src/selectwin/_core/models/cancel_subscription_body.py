from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="CancelSubscriptionBody")


@_attrs_define
class CancelSubscriptionBody:
    """
    Attributes:
        reason (str | Unset):
        immediately (bool | Unset):
    """

    reason: str | Unset = UNSET
    immediately: bool | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        reason = self.reason

        immediately = self.immediately

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if reason is not UNSET:
            field_dict["reason"] = reason
        if immediately is not UNSET:
            field_dict["immediately"] = immediately

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        reason = d.pop("reason", UNSET)

        immediately = d.pop("immediately", UNSET)

        cancel_subscription_body = cls(
            reason=reason,
            immediately=immediately,
        )

        return cancel_subscription_body
