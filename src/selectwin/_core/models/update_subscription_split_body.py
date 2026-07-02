from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..models.update_subscription_split_body_type import UpdateSubscriptionSplitBodyType

T = TypeVar("T", bound="UpdateSubscriptionSplitBody")


@_attrs_define
class UpdateSubscriptionSplitBody:
    """
    Attributes:
        type_ (UpdateSubscriptionSplitBodyType):
        value (float):
    """

    type_: UpdateSubscriptionSplitBodyType
    value: float

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_.value

        value = self.value

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "type": type_,
                "value": value,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        type_ = UpdateSubscriptionSplitBodyType(d.pop("type"))

        value = d.pop("value")

        update_subscription_split_body = cls(
            type_=type_,
            value=value,
        )

        return update_subscription_split_body
