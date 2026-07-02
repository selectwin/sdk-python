from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.create_subscription_body_items_item_metadata import (
        CreateSubscriptionBodyItemsItemMetadata,
    )


T = TypeVar("T", bound="CreateSubscriptionBodyItemsItem")


@_attrs_define
class CreateSubscriptionBodyItemsItem:
    """
    Attributes:
        variant_id (str): Public identifier (var_/prv_…)
        quantity (int | Unset):  Default: 1.
        description (str | Unset):
        external_reference (str | Unset):
        metadata (CreateSubscriptionBodyItemsItemMetadata | Unset):
    """

    variant_id: str
    quantity: int | Unset = 1
    description: str | Unset = UNSET
    external_reference: str | Unset = UNSET
    metadata: CreateSubscriptionBodyItemsItemMetadata | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        variant_id = self.variant_id

        quantity = self.quantity

        description = self.description

        external_reference = self.external_reference

        metadata: dict[str, Any] | Unset = UNSET
        if not isinstance(self.metadata, Unset):
            metadata = self.metadata.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "variantId": variant_id,
            }
        )
        if quantity is not UNSET:
            field_dict["quantity"] = quantity
        if description is not UNSET:
            field_dict["description"] = description
        if external_reference is not UNSET:
            field_dict["externalReference"] = external_reference
        if metadata is not UNSET:
            field_dict["metadata"] = metadata

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.create_subscription_body_items_item_metadata import (
            CreateSubscriptionBodyItemsItemMetadata,
        )

        d = dict(src_dict)
        variant_id = d.pop("variantId")

        quantity = d.pop("quantity", UNSET)

        description = d.pop("description", UNSET)

        external_reference = d.pop("externalReference", UNSET)

        _metadata = d.pop("metadata", UNSET)
        metadata: CreateSubscriptionBodyItemsItemMetadata | Unset
        if isinstance(_metadata, Unset):
            metadata = UNSET
        else:
            metadata = CreateSubscriptionBodyItemsItemMetadata.from_dict(_metadata)

        create_subscription_body_items_item = cls(
            variant_id=variant_id,
            quantity=quantity,
            description=description,
            external_reference=external_reference,
            metadata=metadata,
        )

        return create_subscription_body_items_item
