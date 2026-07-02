from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.remove_subscription_split_response_200_splits_item_links_additional_property import (
        RemoveSubscriptionSplitResponse200SplitsItemLinksAdditionalProperty,
    )


T = TypeVar("T", bound="RemoveSubscriptionSplitResponse200SplitsItemLinks")


@_attrs_define
class RemoveSubscriptionSplitResponse200SplitsItemLinks:
    """ """

    additional_properties: dict[
        str, RemoveSubscriptionSplitResponse200SplitsItemLinksAdditionalProperty
    ] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:

        field_dict: dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            field_dict[prop_name] = prop.to_dict()

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.remove_subscription_split_response_200_splits_item_links_additional_property import (
            RemoveSubscriptionSplitResponse200SplitsItemLinksAdditionalProperty,
        )

        d = dict(src_dict)
        remove_subscription_split_response_200_splits_item_links = cls()

        additional_properties = {}
        for prop_name, prop_dict in d.items():
            additional_property = RemoveSubscriptionSplitResponse200SplitsItemLinksAdditionalProperty.from_dict(
                prop_dict
            )

            additional_properties[prop_name] = additional_property

        remove_subscription_split_response_200_splits_item_links.additional_properties = additional_properties
        return remove_subscription_split_response_200_splits_item_links

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(
        self, key: str
    ) -> RemoveSubscriptionSplitResponse200SplitsItemLinksAdditionalProperty:
        return self.additional_properties[key]

    def __setitem__(
        self,
        key: str,
        value: RemoveSubscriptionSplitResponse200SplitsItemLinksAdditionalProperty,
    ) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
