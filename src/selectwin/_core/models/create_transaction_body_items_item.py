from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.create_transaction_body_items_item_metadata import (
        CreateTransactionBodyItemsItemMetadata,
    )
    from ..models.create_transaction_body_items_item_pricing import (
        CreateTransactionBodyItemsItemPricing,
    )


T = TypeVar("T", bound="CreateTransactionBodyItemsItem")


@_attrs_define
class CreateTransactionBodyItemsItem:
    """
    Attributes:
        name (str):
        unit_price (int):
        quantity (int):
        description (str | Unset):
        currency (str | Unset): ISO 4217 currency code
        pricing (CreateTransactionBodyItemsItemPricing | Unset):
        variant_id (str | Unset): Public identifier (prefix_value)
        images (list[str] | Unset):
        external_reference (str | Unset):
        metadata (CreateTransactionBodyItemsItemMetadata | Unset):
    """

    name: str
    unit_price: int
    quantity: int
    description: str | Unset = UNSET
    currency: str | Unset = UNSET
    pricing: CreateTransactionBodyItemsItemPricing | Unset = UNSET
    variant_id: str | Unset = UNSET
    images: list[str] | Unset = UNSET
    external_reference: str | Unset = UNSET
    metadata: CreateTransactionBodyItemsItemMetadata | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        unit_price = self.unit_price

        quantity = self.quantity

        description = self.description

        currency = self.currency

        pricing: dict[str, Any] | Unset = UNSET
        if not isinstance(self.pricing, Unset):
            pricing = self.pricing.to_dict()

        variant_id = self.variant_id

        images: list[str] | Unset = UNSET
        if not isinstance(self.images, Unset):
            images = self.images

        external_reference = self.external_reference

        metadata: dict[str, Any] | Unset = UNSET
        if not isinstance(self.metadata, Unset):
            metadata = self.metadata.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "name": name,
                "unitPrice": unit_price,
                "quantity": quantity,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if currency is not UNSET:
            field_dict["currency"] = currency
        if pricing is not UNSET:
            field_dict["pricing"] = pricing
        if variant_id is not UNSET:
            field_dict["variantId"] = variant_id
        if images is not UNSET:
            field_dict["images"] = images
        if external_reference is not UNSET:
            field_dict["externalReference"] = external_reference
        if metadata is not UNSET:
            field_dict["metadata"] = metadata

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.create_transaction_body_items_item_metadata import (
            CreateTransactionBodyItemsItemMetadata,
        )
        from ..models.create_transaction_body_items_item_pricing import (
            CreateTransactionBodyItemsItemPricing,
        )

        d = dict(src_dict)
        name = d.pop("name")

        unit_price = d.pop("unitPrice")

        quantity = d.pop("quantity")

        description = d.pop("description", UNSET)

        currency = d.pop("currency", UNSET)

        _pricing = d.pop("pricing", UNSET)
        pricing: CreateTransactionBodyItemsItemPricing | Unset
        if isinstance(_pricing, Unset):
            pricing = UNSET
        else:
            pricing = CreateTransactionBodyItemsItemPricing.from_dict(_pricing)

        variant_id = d.pop("variantId", UNSET)

        images = cast(list[str], d.pop("images", UNSET))

        external_reference = d.pop("externalReference", UNSET)

        _metadata = d.pop("metadata", UNSET)
        metadata: CreateTransactionBodyItemsItemMetadata | Unset
        if isinstance(_metadata, Unset):
            metadata = UNSET
        else:
            metadata = CreateTransactionBodyItemsItemMetadata.from_dict(_metadata)

        create_transaction_body_items_item = cls(
            name=name,
            unit_price=unit_price,
            quantity=quantity,
            description=description,
            currency=currency,
            pricing=pricing,
            variant_id=variant_id,
            images=images,
            external_reference=external_reference,
            metadata=metadata,
        )

        return create_transaction_body_items_item
