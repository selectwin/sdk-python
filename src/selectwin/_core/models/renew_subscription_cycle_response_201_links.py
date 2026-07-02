from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.renew_subscription_cycle_response_201_links_additional_property import (
        RenewSubscriptionCycleResponse201LinksAdditionalProperty,
    )


T = TypeVar("T", bound="RenewSubscriptionCycleResponse201Links")


@_attrs_define
class RenewSubscriptionCycleResponse201Links:
    """ """

    additional_properties: dict[
        str, RenewSubscriptionCycleResponse201LinksAdditionalProperty
    ] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:

        field_dict: dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            field_dict[prop_name] = prop.to_dict()

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.renew_subscription_cycle_response_201_links_additional_property import (
            RenewSubscriptionCycleResponse201LinksAdditionalProperty,
        )

        d = dict(src_dict)
        renew_subscription_cycle_response_201_links = cls()

        additional_properties = {}
        for prop_name, prop_dict in d.items():
            additional_property = (
                RenewSubscriptionCycleResponse201LinksAdditionalProperty.from_dict(
                    prop_dict
                )
            )

            additional_properties[prop_name] = additional_property

        renew_subscription_cycle_response_201_links.additional_properties = (
            additional_properties
        )
        return renew_subscription_cycle_response_201_links

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(
        self, key: str
    ) -> RenewSubscriptionCycleResponse201LinksAdditionalProperty:
        return self.additional_properties[key]

    def __setitem__(
        self, key: str, value: RenewSubscriptionCycleResponse201LinksAdditionalProperty
    ) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
