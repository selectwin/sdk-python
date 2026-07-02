from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..models.add_subscription_split_body_type import AddSubscriptionSplitBodyType

T = TypeVar("T", bound="AddSubscriptionSplitBody")


@_attrs_define
class AddSubscriptionSplitBody:
    """
    Attributes:
        recipient (str): Public identifier (prefix_value)
        type_ (AddSubscriptionSplitBodyType):
        value (float):
    """

    recipient: str
    type_: AddSubscriptionSplitBodyType
    value: float

    def to_dict(self) -> dict[str, Any]:
        recipient = self.recipient

        type_ = self.type_.value

        value = self.value

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "recipient": recipient,
                "type": type_,
                "value": value,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        recipient = d.pop("recipient")

        type_ = AddSubscriptionSplitBodyType(d.pop("type"))

        value = d.pop("value")

        add_subscription_split_body = cls(
            recipient=recipient,
            type_=type_,
            value=value,
        )

        return add_subscription_split_body
