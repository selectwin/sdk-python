from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.get_product_response_200_variants_item_attributes_type_0 import (
        GetProductResponse200VariantsItemAttributesType0,
    )
    from ..models.get_product_response_200_variants_item_images_type_0_item_type_1 import (
        GetProductResponse200VariantsItemImagesType0ItemType1,
    )
    from ..models.get_product_response_200_variants_item_metadata_type_0 import (
        GetProductResponse200VariantsItemMetadataType0,
    )
    from ..models.get_product_response_200_variants_item_pricing import (
        GetProductResponse200VariantsItemPricing,
    )


T = TypeVar("T", bound="GetProductResponse200VariantsItem")


@_attrs_define
class GetProductResponse200VariantsItem:
    """
    Attributes:
        id (str): Public identifier (var_/prv_…)
        product_id (str): Public identifier (prd_/pro_…)
        name (None | str):
        slug (None | str):
        description (None | str):
        sku (None | str):
        primary (bool):
        enabled (bool):
        pricing (GetProductResponse200VariantsItemPricing):
        images (list[GetProductResponse200VariantsItemImagesType0ItemType1 | str] | None):
        metadata (GetProductResponse200VariantsItemMetadataType0 | None):
        attributes (GetProductResponse200VariantsItemAttributesType0 | None):
        external_reference (None | str):
        checkout_url (None | str):
        created_at (str):
        updated_at (str):
    """

    id: str
    product_id: str
    name: None | str
    slug: None | str
    description: None | str
    sku: None | str
    primary: bool
    enabled: bool
    pricing: GetProductResponse200VariantsItemPricing
    images: list[GetProductResponse200VariantsItemImagesType0ItemType1 | str] | None
    metadata: GetProductResponse200VariantsItemMetadataType0 | None
    attributes: GetProductResponse200VariantsItemAttributesType0 | None
    external_reference: None | str
    checkout_url: None | str
    created_at: str
    updated_at: str

    def to_dict(self) -> dict[str, Any]:
        from ..models.get_product_response_200_variants_item_attributes_type_0 import (
            GetProductResponse200VariantsItemAttributesType0,
        )
        from ..models.get_product_response_200_variants_item_images_type_0_item_type_1 import (
            GetProductResponse200VariantsItemImagesType0ItemType1,
        )
        from ..models.get_product_response_200_variants_item_metadata_type_0 import (
            GetProductResponse200VariantsItemMetadataType0,
        )

        id = self.id

        product_id = self.product_id

        name: None | str
        name = self.name

        slug: None | str
        slug = self.slug

        description: None | str
        description = self.description

        sku: None | str
        sku = self.sku

        primary = self.primary

        enabled = self.enabled

        pricing = self.pricing.to_dict()

        images: list[dict[str, Any] | str] | None
        if isinstance(self.images, list):
            images = []
            for images_type_0_item_data in self.images:
                images_type_0_item: dict[str, Any] | str
                if isinstance(
                    images_type_0_item_data,
                    GetProductResponse200VariantsItemImagesType0ItemType1,
                ):
                    images_type_0_item = images_type_0_item_data.to_dict()
                else:
                    images_type_0_item = images_type_0_item_data
                images.append(images_type_0_item)

        else:
            images = self.images

        metadata: dict[str, Any] | None
        if isinstance(self.metadata, GetProductResponse200VariantsItemMetadataType0):
            metadata = self.metadata.to_dict()
        else:
            metadata = self.metadata

        attributes: dict[str, Any] | None
        if isinstance(
            self.attributes, GetProductResponse200VariantsItemAttributesType0
        ):
            attributes = self.attributes.to_dict()
        else:
            attributes = self.attributes

        external_reference: None | str
        external_reference = self.external_reference

        checkout_url: None | str
        checkout_url = self.checkout_url

        created_at = self.created_at

        updated_at = self.updated_at

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "id": id,
                "productId": product_id,
                "name": name,
                "slug": slug,
                "description": description,
                "sku": sku,
                "primary": primary,
                "enabled": enabled,
                "pricing": pricing,
                "images": images,
                "metadata": metadata,
                "attributes": attributes,
                "externalReference": external_reference,
                "checkoutUrl": checkout_url,
                "createdAt": created_at,
                "updatedAt": updated_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_product_response_200_variants_item_attributes_type_0 import (
            GetProductResponse200VariantsItemAttributesType0,
        )
        from ..models.get_product_response_200_variants_item_images_type_0_item_type_1 import (
            GetProductResponse200VariantsItemImagesType0ItemType1,
        )
        from ..models.get_product_response_200_variants_item_metadata_type_0 import (
            GetProductResponse200VariantsItemMetadataType0,
        )
        from ..models.get_product_response_200_variants_item_pricing import (
            GetProductResponse200VariantsItemPricing,
        )

        d = dict(src_dict)
        id = d.pop("id")

        product_id = d.pop("productId")

        def _parse_name(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        name = _parse_name(d.pop("name"))

        def _parse_slug(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        slug = _parse_slug(d.pop("slug"))

        def _parse_description(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        description = _parse_description(d.pop("description"))

        def _parse_sku(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        sku = _parse_sku(d.pop("sku"))

        primary = d.pop("primary")

        enabled = d.pop("enabled")

        pricing = GetProductResponse200VariantsItemPricing.from_dict(d.pop("pricing"))

        def _parse_images(
            data: object,
        ) -> list[GetProductResponse200VariantsItemImagesType0ItemType1 | str] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                images_type_0 = []
                _images_type_0 = data
                for images_type_0_item_data in _images_type_0:

                    def _parse_images_type_0_item(
                        data: object,
                    ) -> GetProductResponse200VariantsItemImagesType0ItemType1 | str:
                        try:
                            if not isinstance(data, dict):
                                raise TypeError()
                            images_type_0_item_type_1 = GetProductResponse200VariantsItemImagesType0ItemType1.from_dict(
                                data
                            )

                            return images_type_0_item_type_1
                        except (TypeError, ValueError, AttributeError, KeyError):
                            pass
                        return cast(
                            GetProductResponse200VariantsItemImagesType0ItemType1 | str,
                            data,
                        )

                    images_type_0_item = _parse_images_type_0_item(
                        images_type_0_item_data
                    )

                    images_type_0.append(images_type_0_item)

                return images_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                list[GetProductResponse200VariantsItemImagesType0ItemType1 | str]
                | None,
                data,
            )

        images = _parse_images(d.pop("images"))

        def _parse_metadata(
            data: object,
        ) -> GetProductResponse200VariantsItemMetadataType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                metadata_type_0 = (
                    GetProductResponse200VariantsItemMetadataType0.from_dict(data)
                )

                return metadata_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(GetProductResponse200VariantsItemMetadataType0 | None, data)

        metadata = _parse_metadata(d.pop("metadata"))

        def _parse_attributes(
            data: object,
        ) -> GetProductResponse200VariantsItemAttributesType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                attributes_type_0 = (
                    GetProductResponse200VariantsItemAttributesType0.from_dict(data)
                )

                return attributes_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(GetProductResponse200VariantsItemAttributesType0 | None, data)

        attributes = _parse_attributes(d.pop("attributes"))

        def _parse_external_reference(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        external_reference = _parse_external_reference(d.pop("externalReference"))

        def _parse_checkout_url(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        checkout_url = _parse_checkout_url(d.pop("checkoutUrl"))

        created_at = d.pop("createdAt")

        updated_at = d.pop("updatedAt")

        get_product_response_200_variants_item = cls(
            id=id,
            product_id=product_id,
            name=name,
            slug=slug,
            description=description,
            sku=sku,
            primary=primary,
            enabled=enabled,
            pricing=pricing,
            images=images,
            metadata=metadata,
            attributes=attributes,
            external_reference=external_reference,
            checkout_url=checkout_url,
            created_at=created_at,
            updated_at=updated_at,
        )

        return get_product_response_200_variants_item
