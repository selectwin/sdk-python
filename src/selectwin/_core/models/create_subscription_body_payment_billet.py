from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateSubscriptionBodyPaymentBillet")


@_attrs_define
class CreateSubscriptionBodyPaymentBillet:
    """
    Attributes:
        expires_in_days (int | Unset):
    """

    expires_in_days: int | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        expires_in_days = self.expires_in_days

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if expires_in_days is not UNSET:
            field_dict["expiresInDays"] = expires_in_days

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        expires_in_days = d.pop("expiresInDays", UNSET)

        create_subscription_body_payment_billet = cls(
            expires_in_days=expires_in_days,
        )

        return create_subscription_body_payment_billet
