from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.create_product_body_variants_item_attributes import (
        CreateProductBodyVariantsItemAttributes,
    )
    from ..models.create_product_body_variants_item_images_item_type_1 import (
        CreateProductBodyVariantsItemImagesItemType1,
    )
    from ..models.create_product_body_variants_item_metadata import (
        CreateProductBodyVariantsItemMetadata,
    )
    from ..models.create_product_body_variants_item_pricing import (
        CreateProductBodyVariantsItemPricing,
    )


T = TypeVar("T", bound="CreateProductBodyVariantsItem")


@_attrs_define
class CreateProductBodyVariantsItem:
    """
    Attributes:
        name (str):
        pricing (CreateProductBodyVariantsItemPricing):
        description (str | Unset):
        sku (str | Unset):
        images (list[CreateProductBodyVariantsItemImagesItemType1 | str] | Unset):
        metadata (CreateProductBodyVariantsItemMetadata | Unset):
        attributes (CreateProductBodyVariantsItemAttributes | Unset):
        external_reference (str | Unset):
        enabled (bool | Unset):  Default: True.
    """

    name: str
    pricing: CreateProductBodyVariantsItemPricing
    description: str | Unset = UNSET
    sku: str | Unset = UNSET
    images: list[CreateProductBodyVariantsItemImagesItemType1 | str] | Unset = UNSET
    metadata: CreateProductBodyVariantsItemMetadata | Unset = UNSET
    attributes: CreateProductBodyVariantsItemAttributes | Unset = UNSET
    external_reference: str | Unset = UNSET
    enabled: bool | Unset = True

    def to_dict(self) -> dict[str, Any]:
        from ..models.create_product_body_variants_item_images_item_type_1 import (
            CreateProductBodyVariantsItemImagesItemType1,
        )

        name = self.name

        pricing = self.pricing.to_dict()

        description = self.description

        sku = self.sku

        images: list[dict[str, Any] | str] | Unset = UNSET
        if not isinstance(self.images, Unset):
            images = []
            for images_item_data in self.images:
                images_item: dict[str, Any] | str
                if isinstance(
                    images_item_data, CreateProductBodyVariantsItemImagesItemType1
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

        field_dict.update(
            {
                "name": name,
                "pricing": pricing,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if sku is not UNSET:
            field_dict["sku"] = sku
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
        from ..models.create_product_body_variants_item_attributes import (
            CreateProductBodyVariantsItemAttributes,
        )
        from ..models.create_product_body_variants_item_images_item_type_1 import (
            CreateProductBodyVariantsItemImagesItemType1,
        )
        from ..models.create_product_body_variants_item_metadata import (
            CreateProductBodyVariantsItemMetadata,
        )
        from ..models.create_product_body_variants_item_pricing import (
            CreateProductBodyVariantsItemPricing,
        )

        d = dict(src_dict)
        name = d.pop("name")

        pricing = CreateProductBodyVariantsItemPricing.from_dict(d.pop("pricing"))

        description = d.pop("description", UNSET)

        sku = d.pop("sku", UNSET)

        _images = d.pop("images", UNSET)
        images: list[CreateProductBodyVariantsItemImagesItemType1 | str] | Unset = UNSET
        if _images is not UNSET:
            images = []
            for images_item_data in _images:

                def _parse_images_item(
                    data: object,
                ) -> CreateProductBodyVariantsItemImagesItemType1 | str:
                    try:
                        if not isinstance(data, dict):
                            raise TypeError()
                        images_item_type_1 = (
                            CreateProductBodyVariantsItemImagesItemType1.from_dict(data)
                        )

                        return images_item_type_1
                    except (TypeError, ValueError, AttributeError, KeyError):
                        pass
                    return cast(
                        CreateProductBodyVariantsItemImagesItemType1 | str, data
                    )

                images_item = _parse_images_item(images_item_data)

                images.append(images_item)

        _metadata = d.pop("metadata", UNSET)
        metadata: CreateProductBodyVariantsItemMetadata | Unset
        if isinstance(_metadata, Unset):
            metadata = UNSET
        else:
            metadata = CreateProductBodyVariantsItemMetadata.from_dict(_metadata)

        _attributes = d.pop("attributes", UNSET)
        attributes: CreateProductBodyVariantsItemAttributes | Unset
        if isinstance(_attributes, Unset):
            attributes = UNSET
        else:
            attributes = CreateProductBodyVariantsItemAttributes.from_dict(_attributes)

        external_reference = d.pop("externalReference", UNSET)

        enabled = d.pop("enabled", UNSET)

        create_product_body_variants_item = cls(
            name=name,
            pricing=pricing,
            description=description,
            sku=sku,
            images=images,
            metadata=metadata,
            attributes=attributes,
            external_reference=external_reference,
            enabled=enabled,
        )

        return create_product_body_variants_item
