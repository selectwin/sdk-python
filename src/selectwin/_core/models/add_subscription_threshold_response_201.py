from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.add_subscription_threshold_response_201_kind import (
    AddSubscriptionThresholdResponse201Kind,
)

T = TypeVar("T", bound="AddSubscriptionThresholdResponse201")


@_attrs_define
class AddSubscriptionThresholdResponse201:
    """
    Attributes:
        id (str): Public identifier (sbt_…)
        subscription_id (str): Public identifier (subs_/sub_…)
        item_id (None | str): Public identifier (sit_/item_…)
        kind (AddSubscriptionThresholdResponse201Kind):
        value (int):
        enabled (bool):
    """

    id: str
    subscription_id: str
    item_id: None | str
    kind: AddSubscriptionThresholdResponse201Kind
    value: int
    enabled: bool

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        subscription_id = self.subscription_id

        item_id: None | str
        item_id = self.item_id

        kind = self.kind.value

        value = self.value

        enabled = self.enabled

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "id": id,
                "subscriptionId": subscription_id,
                "itemId": item_id,
                "kind": kind,
                "value": value,
                "enabled": enabled,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        subscription_id = d.pop("subscriptionId")

        def _parse_item_id(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        item_id = _parse_item_id(d.pop("itemId"))

        kind = AddSubscriptionThresholdResponse201Kind(d.pop("kind"))

        value = d.pop("value")

        enabled = d.pop("enabled")

        add_subscription_threshold_response_201 = cls(
            id=id,
            subscription_id=subscription_id,
            item_id=item_id,
            kind=kind,
            value=value,
            enabled=enabled,
        )

        return add_subscription_threshold_response_201
