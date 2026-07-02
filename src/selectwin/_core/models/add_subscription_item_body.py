from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.add_subscription_item_body_metadata import (
        AddSubscriptionItemBodyMetadata,
    )


T = TypeVar("T", bound="AddSubscriptionItemBody")


@_attrs_define
class AddSubscriptionItemBody:
    """
    Attributes:
        variant_id (str): Public identifier (var_/prv_…)
        quantity (int | Unset):  Default: 1.
        description (str | Unset):
        external_reference (str | Unset):
        metadata (AddSubscriptionItemBodyMetadata | Unset):
    """

    variant_id: str
    quantity: int | Unset = 1
    description: str | Unset = UNSET
    external_reference: str | Unset = UNSET
    metadata: AddSubscriptionItemBodyMetadata | Unset = UNSET

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
        from ..models.add_subscription_item_body_metadata import (
            AddSubscriptionItemBodyMetadata,
        )

        d = dict(src_dict)
        variant_id = d.pop("variantId")

        quantity = d.pop("quantity", UNSET)

        description = d.pop("description", UNSET)

        external_reference = d.pop("externalReference", UNSET)

        _metadata = d.pop("metadata", UNSET)
        metadata: AddSubscriptionItemBodyMetadata | Unset
        if isinstance(_metadata, Unset):
            metadata = UNSET
        else:
            metadata = AddSubscriptionItemBodyMetadata.from_dict(_metadata)

        add_subscription_item_body = cls(
            variant_id=variant_id,
            quantity=quantity,
            description=description,
            external_reference=external_reference,
            metadata=metadata,
        )

        return add_subscription_item_body
