from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.create_card_response_201_links_additional_property import (
        CreateCardResponse201LinksAdditionalProperty,
    )


T = TypeVar("T", bound="CreateCardResponse201Links")


@_attrs_define
class CreateCardResponse201Links:
    """ """

    additional_properties: dict[str, CreateCardResponse201LinksAdditionalProperty] = (
        _attrs_field(init=False, factory=dict)
    )

    def to_dict(self) -> dict[str, Any]:

        field_dict: dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            field_dict[prop_name] = prop.to_dict()

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.create_card_response_201_links_additional_property import (
            CreateCardResponse201LinksAdditionalProperty,
        )

        d = dict(src_dict)
        create_card_response_201_links = cls()

        additional_properties = {}
        for prop_name, prop_dict in d.items():
            additional_property = (
                CreateCardResponse201LinksAdditionalProperty.from_dict(prop_dict)
            )

            additional_properties[prop_name] = additional_property

        create_card_response_201_links.additional_properties = additional_properties
        return create_card_response_201_links

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> CreateCardResponse201LinksAdditionalProperty:
        return self.additional_properties[key]

    def __setitem__(
        self, key: str, value: CreateCardResponse201LinksAdditionalProperty
    ) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
