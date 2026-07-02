from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="ListSubscriptionItemsResponse200LinksAdditionalProperty")


@_attrs_define
class ListSubscriptionItemsResponse200LinksAdditionalProperty:
    """
    Attributes:
        href (str):
        method (str):
        description (str):
    """

    href: str
    method: str
    description: str

    def to_dict(self) -> dict[str, Any]:
        href = self.href

        method = self.method

        description = self.description

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "href": href,
                "method": method,
                "description": description,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        href = d.pop("href")

        method = d.pop("method")

        description = d.pop("description")

        list_subscription_items_response_200_links_additional_property = cls(
            href=href,
            method=method,
            description=description,
        )

        return list_subscription_items_response_200_links_additional_property
