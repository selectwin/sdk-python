from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..models.update_subscription_split_put_body_type import (
    UpdateSubscriptionSplitPutBodyType,
)

T = TypeVar("T", bound="UpdateSubscriptionSplitPutBody")


@_attrs_define
class UpdateSubscriptionSplitPutBody:
    """
    Attributes:
        type_ (UpdateSubscriptionSplitPutBodyType):
        value (float):
    """

    type_: UpdateSubscriptionSplitPutBodyType
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
        type_ = UpdateSubscriptionSplitPutBodyType(d.pop("type"))

        value = d.pop("value")

        update_subscription_split_put_body = cls(
            type_=type_,
            value=value,
        )

        return update_subscription_split_put_body
