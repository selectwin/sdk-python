from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.create_product_response_201_type import CreateProductResponse201Type
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.create_product_response_201_images_type_0_item_type_1 import (
        CreateProductResponse201ImagesType0ItemType1,
    )
    from ..models.create_product_response_201_variants_item import (
        CreateProductResponse201VariantsItem,
    )


T = TypeVar("T", bound="CreateProductResponse201")


@_attrs_define
class CreateProductResponse201:
    """
    Attributes:
        id (str): Public identifier (prd_/pro_…)
        name (str):
        slug (None | str):
        sales_page (None | str):
        description (None | str):
        language (None | str):
        enabled (bool):
        sales_qty (int | None):
        type_ (CreateProductResponse201Type):
        category (str):
        external_reference (None | str):
        warranty_days (int):
        images (list[CreateProductResponse201ImagesType0ItemType1 | str] | None):
        created_at (str):
        updated_at (str):
        variants (list[CreateProductResponse201VariantsItem]):
        image_asset_ids (Any | Unset):
    """

    id: str
    name: str
    slug: None | str
    sales_page: None | str
    description: None | str
    language: None | str
    enabled: bool
    sales_qty: int | None
    type_: CreateProductResponse201Type
    category: str
    external_reference: None | str
    warranty_days: int
    images: list[CreateProductResponse201ImagesType0ItemType1 | str] | None
    created_at: str
    updated_at: str
    variants: list[CreateProductResponse201VariantsItem]
    image_asset_ids: Any | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.create_product_response_201_images_type_0_item_type_1 import (
            CreateProductResponse201ImagesType0ItemType1,
        )

        id = self.id

        name = self.name

        slug: None | str
        slug = self.slug

        sales_page: None | str
        sales_page = self.sales_page

        description: None | str
        description = self.description

        language: None | str
        language = self.language

        enabled = self.enabled

        sales_qty: int | None
        sales_qty = self.sales_qty

        type_ = self.type_.value

        category = self.category

        external_reference: None | str
        external_reference = self.external_reference

        warranty_days = self.warranty_days

        images: list[dict[str, Any] | str] | None
        if isinstance(self.images, list):
            images = []
            for images_type_0_item_data in self.images:
                images_type_0_item: dict[str, Any] | str
                if isinstance(
                    images_type_0_item_data,
                    CreateProductResponse201ImagesType0ItemType1,
                ):
                    images_type_0_item = images_type_0_item_data.to_dict()
                else:
                    images_type_0_item = images_type_0_item_data
                images.append(images_type_0_item)

        else:
            images = self.images

        created_at = self.created_at

        updated_at = self.updated_at

        variants = []
        for variants_item_data in self.variants:
            variants_item = variants_item_data.to_dict()
            variants.append(variants_item)

        image_asset_ids = self.image_asset_ids

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "id": id,
                "name": name,
                "slug": slug,
                "salesPage": sales_page,
                "description": description,
                "language": language,
                "enabled": enabled,
                "salesQty": sales_qty,
                "type": type_,
                "category": category,
                "externalReference": external_reference,
                "warrantyDays": warranty_days,
                "images": images,
                "createdAt": created_at,
                "updatedAt": updated_at,
                "variants": variants,
            }
        )
        if image_asset_ids is not UNSET:
            field_dict["imageAssetIds"] = image_asset_ids

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.create_product_response_201_images_type_0_item_type_1 import (
            CreateProductResponse201ImagesType0ItemType1,
        )
        from ..models.create_product_response_201_variants_item import (
            CreateProductResponse201VariantsItem,
        )

        d = dict(src_dict)
        id = d.pop("id")

        name = d.pop("name")

        def _parse_slug(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        slug = _parse_slug(d.pop("slug"))

        def _parse_sales_page(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        sales_page = _parse_sales_page(d.pop("salesPage"))

        def _parse_description(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        description = _parse_description(d.pop("description"))

        def _parse_language(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        language = _parse_language(d.pop("language"))

        enabled = d.pop("enabled")

        def _parse_sales_qty(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        sales_qty = _parse_sales_qty(d.pop("salesQty"))

        type_ = CreateProductResponse201Type(d.pop("type"))

        category = d.pop("category")

        def _parse_external_reference(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        external_reference = _parse_external_reference(d.pop("externalReference"))

        warranty_days = d.pop("warrantyDays")

        def _parse_images(
            data: object,
        ) -> list[CreateProductResponse201ImagesType0ItemType1 | str] | None:
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
                    ) -> CreateProductResponse201ImagesType0ItemType1 | str:
                        try:
                            if not isinstance(data, dict):
                                raise TypeError()
                            images_type_0_item_type_1 = (
                                CreateProductResponse201ImagesType0ItemType1.from_dict(
                                    data
                                )
                            )

                            return images_type_0_item_type_1
                        except (TypeError, ValueError, AttributeError, KeyError):
                            pass
                        return cast(
                            CreateProductResponse201ImagesType0ItemType1 | str, data
                        )

                    images_type_0_item = _parse_images_type_0_item(
                        images_type_0_item_data
                    )

                    images_type_0.append(images_type_0_item)

                return images_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                list[CreateProductResponse201ImagesType0ItemType1 | str] | None, data
            )

        images = _parse_images(d.pop("images"))

        created_at = d.pop("createdAt")

        updated_at = d.pop("updatedAt")

        variants = []
        _variants = d.pop("variants")
        for variants_item_data in _variants:
            variants_item = CreateProductResponse201VariantsItem.from_dict(
                variants_item_data
            )

            variants.append(variants_item)

        image_asset_ids = d.pop("imageAssetIds", UNSET)

        create_product_response_201 = cls(
            id=id,
            name=name,
            slug=slug,
            sales_page=sales_page,
            description=description,
            language=language,
            enabled=enabled,
            sales_qty=sales_qty,
            type_=type_,
            category=category,
            external_reference=external_reference,
            warranty_days=warranty_days,
            images=images,
            created_at=created_at,
            updated_at=updated_at,
            variants=variants,
            image_asset_ids=image_asset_ids,
        )

        return create_product_response_201
