from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.list_subscription_thresholds_response_200_data_item_kind import (
    ListSubscriptionThresholdsResponse200DataItemKind,
)

T = TypeVar("T", bound="ListSubscriptionThresholdsResponse200DataItem")


@_attrs_define
class ListSubscriptionThresholdsResponse200DataItem:
    """
    Attributes:
        id (str): Public identifier (sbt_…)
        kind (ListSubscriptionThresholdsResponse200DataItemKind):
        value (int):
        enabled (bool):
        item_id (None | str): Public identifier (sit_/item_…)
        created_at (str):
        updated_at (str):
    """

    id: str
    kind: ListSubscriptionThresholdsResponse200DataItemKind
    value: int
    enabled: bool
    item_id: None | str
    created_at: str
    updated_at: str

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        kind = self.kind.value

        value = self.value

        enabled = self.enabled

        item_id: None | str
        item_id = self.item_id

        created_at = self.created_at

        updated_at = self.updated_at

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "id": id,
                "kind": kind,
                "value": value,
                "enabled": enabled,
                "itemId": item_id,
                "createdAt": created_at,
                "updatedAt": updated_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        kind = ListSubscriptionThresholdsResponse200DataItemKind(d.pop("kind"))

        value = d.pop("value")

        enabled = d.pop("enabled")

        def _parse_item_id(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        item_id = _parse_item_id(d.pop("itemId"))

        created_at = d.pop("createdAt")

        updated_at = d.pop("updatedAt")

        list_subscription_thresholds_response_200_data_item = cls(
            id=id,
            kind=kind,
            value=value,
            enabled=enabled,
            item_id=item_id,
            created_at=created_at,
            updated_at=updated_at,
        )

        return list_subscription_thresholds_response_200_data_item
