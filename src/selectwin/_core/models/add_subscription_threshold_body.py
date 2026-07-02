from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..models.add_subscription_threshold_body_kind import (
    AddSubscriptionThresholdBodyKind,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="AddSubscriptionThresholdBody")


@_attrs_define
class AddSubscriptionThresholdBody:
    """
    Attributes:
        kind (AddSubscriptionThresholdBodyKind):
        value (int):
        item_id (str | Unset): Public identifier (sit_/item_…)
        enabled (bool | Unset):
    """

    kind: AddSubscriptionThresholdBodyKind
    value: int
    item_id: str | Unset = UNSET
    enabled: bool | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        kind = self.kind.value

        value = self.value

        item_id = self.item_id

        enabled = self.enabled

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "kind": kind,
                "value": value,
            }
        )
        if item_id is not UNSET:
            field_dict["itemId"] = item_id
        if enabled is not UNSET:
            field_dict["enabled"] = enabled

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        kind = AddSubscriptionThresholdBodyKind(d.pop("kind"))

        value = d.pop("value")

        item_id = d.pop("itemId", UNSET)

        enabled = d.pop("enabled", UNSET)

        add_subscription_threshold_body = cls(
            kind=kind,
            value=value,
            item_id=item_id,
            enabled=enabled,
        )

        return add_subscription_threshold_body
