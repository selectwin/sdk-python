from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.update_product_variant_body_attributes import (
        UpdateProductVariantBodyAttributes,
    )
    from ..models.update_product_variant_body_images_item_type_1 import (
        UpdateProductVariantBodyImagesItemType1,
    )
    from ..models.update_product_variant_body_metadata import (
        UpdateProductVariantBodyMetadata,
    )
    from ..models.update_product_variant_body_pricing import (
        UpdateProductVariantBodyPricing,
    )


T = TypeVar("T", bound="UpdateProductVariantBody")


@_attrs_define
class UpdateProductVariantBody:
    """
    Attributes:
        name (str | Unset):
        description (str | Unset):
        sku (str | Unset):
        pricing (UpdateProductVariantBodyPricing | Unset):
        images (list[str | UpdateProductVariantBodyImagesItemType1] | Unset):
        metadata (UpdateProductVariantBodyMetadata | Unset):
        attributes (UpdateProductVariantBodyAttributes | Unset):
        external_reference (str | Unset):
        enabled (bool | Unset):  Default: True.
    """

    name: str | Unset = UNSET
    description: str | Unset = UNSET
    sku: str | Unset = UNSET
    pricing: UpdateProductVariantBodyPricing | Unset = UNSET
    images: list[str | UpdateProductVariantBodyImagesItemType1] | Unset = UNSET
    metadata: UpdateProductVariantBodyMetadata | Unset = UNSET
    attributes: UpdateProductVariantBodyAttributes | Unset = UNSET
    external_reference: str | Unset = UNSET
    enabled: bool | Unset = True

    def to_dict(self) -> dict[str, Any]:
        from ..models.update_product_variant_body_images_item_type_1 import (
            UpdateProductVariantBodyImagesItemType1,
        )

        name = self.name

        description = self.description

        sku = self.sku

        pricing: dict[str, Any] | Unset = UNSET
        if not isinstance(self.pricing, Unset):
            pricing = self.pricing.to_dict()

        images: list[dict[str, Any] | str] | Unset = UNSET
        if not isinstance(self.images, Unset):
            images = []
            for images_item_data in self.images:
                images_item: dict[str, Any] | str
                if isinstance(
                    images_item_data, UpdateProductVariantBodyImagesItemType1
                ):
                    images_item = images_item_data.to_dict()
                else:
                    images_item = images_item_data
                images.append(images_item)

        metadata: dict[str, Any] | Unset = UNSET
        if not isinstance(self.metadata, Unset):
            metadata = self.metadata.to_dict()

        attributes: dict[str, Any] | Unset = UNSET
        if not isinstance(self.attributes, Unset):
            attributes = self.attributes.to_dict()

        external_reference = self.external_reference

        enabled = self.enabled

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if description is not UNSET:
            field_dict["description"] = description
        if sku is not UNSET:
            field_dict["sku"] = sku
        if pricing is not UNSET:
            field_dict["pricing"] = pricing
        if images is not UNSET:
            field_dict["images"] = images
        if metadata is not UNSET:
            field_dict["metadata"] = metadata
        if attributes is not UNSET:
            field_dict["attributes"] = attributes
        if external_reference is not UNSET:
            field_dict["externalReference"] = external_reference
        if enabled is not UNSET:
            field_dict["enabled"] = enabled

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.update_product_variant_body_attributes import (
            UpdateProductVariantBodyAttributes,
        )
        from ..models.update_product_variant_body_images_item_type_1 import (
            UpdateProductVariantBodyImagesItemType1,
        )
        from ..models.update_product_variant_body_metadata import (
            UpdateProductVariantBodyMetadata,
        )
        from ..models.update_product_variant_body_pricing import (
            UpdateProductVariantBodyPricing,
        )

        d = dict(src_dict)
        name = d.pop("name", UNSET)

        description = d.pop("description", UNSET)

        sku = d.pop("sku", UNSET)

        _pricing = d.pop("pricing", UNSET)
        pricing: UpdateProductVariantBodyPricing | Unset
        if isinstance(_pricing, Unset):
            pricing = UNSET
        else:
            pricing = UpdateProductVariantBodyPricing.from_dict(_pricing)

        _images = d.pop("images", UNSET)
        images: list[str | UpdateProductVariantBodyImagesItemType1] | Unset = UNSET
        if _images is not UNSET:
            images = []
            for images_item_data in _images:

                def _parse_images_item(
                    data: object,
                ) -> str | UpdateProductVariantBodyImagesItemType1:
                    try:
                        if not isinstance(data, dict):
                            raise TypeError()
                        images_item_type_1 = (
                            UpdateProductVariantBodyImagesItemType1.from_dict(data)
                        )

                        return images_item_type_1
                    except (TypeError, ValueError, AttributeError, KeyError):
                        pass
                    return cast(str | UpdateProductVariantBodyImagesItemType1, data)

                images_item = _parse_images_item(images_item_data)

                images.append(images_item)

        _metadata = d.pop("metadata", UNSET)
        metadata: UpdateProductVariantBodyMetadata | Unset
        if isinstance(_metadata, Unset):
            metadata = UNSET
        else:
            metadata = UpdateProductVariantBodyMetadata.from_dict(_metadata)

        _attributes = d.pop("attributes", UNSET)
        attributes: UpdateProductVariantBodyAttributes | Unset
        if isinstance(_attributes, Unset):
            attributes = UNSET
        else:
            attributes = UpdateProductVariantBodyAttributes.from_dict(_attributes)

        external_reference = d.pop("externalReference", UNSET)

        enabled = d.pop("enabled", UNSET)

        update_product_variant_body = cls(
            name=name,
            description=description,
            sku=sku,
            pricing=pricing,
            images=images,
            metadata=metadata,
            attributes=attributes,
            external_reference=external_reference,
            enabled=enabled,
        )

        return update_product_variant_body
