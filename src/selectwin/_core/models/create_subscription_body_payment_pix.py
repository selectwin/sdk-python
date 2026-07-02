from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateSubscriptionBodyPaymentPix")


@_attrs_define
class CreateSubscriptionBodyPaymentPix:
    """
    Attributes:
        expires_in_minutes (int | Unset):
    """

    expires_in_minutes: int | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        expires_in_minutes = self.expires_in_minutes

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if expires_in_minutes is not UNSET:
            field_dict["expiresInMinutes"] = expires_in_minutes

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        expires_in_minutes = d.pop("expiresInMinutes", UNSET)

        create_subscription_body_payment_pix = cls(
            expires_in_minutes=expires_in_minutes,
        )

        return create_subscription_body_payment_pix
