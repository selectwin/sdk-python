from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.create_product_body_type import CreateProductBodyType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.create_product_body_images_item_type_1 import (
        CreateProductBodyImagesItemType1,
    )
    from ..models.create_product_body_variants_item import CreateProductBodyVariantsItem


T = TypeVar("T", bound="CreateProductBody")


@_attrs_define
class CreateProductBody:
    """
    Attributes:
        name (str):
        type_ (CreateProductBodyType):
        category (str):
        warranty_days (int):
        variants (list[CreateProductBodyVariantsItem]):
        sales_page (str | Unset):
        description (str | Unset):
        enabled (bool | Unset):  Default: True.
        language (str | Unset):  Default: 'pt-BR'.
        external_reference (str | Unset):
        images (list[CreateProductBodyImagesItemType1 | str] | Unset):
    """

    name: str
    type_: CreateProductBodyType
    category: str
    warranty_days: int
    variants: list[CreateProductBodyVariantsItem]
    sales_page: str | Unset = UNSET
    description: str | Unset = UNSET
    enabled: bool | Unset = True
    language: str | Unset = "pt-BR"
    external_reference: str | Unset = UNSET
    images: list[CreateProductBodyImagesItemType1 | str] | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.create_product_body_images_item_type_1 import (
            CreateProductBodyImagesItemType1,
        )

        name = self.name

        type_ = self.type_.value

        category = self.category

        warranty_days = self.warranty_days

        variants = []
        for variants_item_data in self.variants:
            variants_item = variants_item_data.to_dict()
            variants.append(variants_item)

        sales_page = self.sales_page

        description = self.description

        enabled = self.enabled

        language = self.language

        external_reference = self.external_reference

        images: list[dict[str, Any] | str] | Unset = UNSET
        if not isinstance(self.images, Unset):
            images = []
            for images_item_data in self.images:
                images_item: dict[str, Any] | str
                if isinstance(images_item_data, CreateProductBodyImagesItemType1):
                    images_item = images_item_data.to_dict()
                else:
                    images_item = images_item_data
                images.append(images_item)

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "name": name,
                "type": type_,
                "category": category,
                "warrantyDays": warranty_days,
                "variants": variants,
            }
        )
        if sales_page is not UNSET:
            field_dict["salesPage"] = sales_page
        if description is not UNSET:
            field_dict["description"] = description
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if language is not UNSET:
            field_dict["language"] = language
        if external_reference is not UNSET:
            field_dict["externalReference"] = external_reference
        if images is not UNSET:
            field_dict["images"] = images

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.create_product_body_images_item_type_1 import (
            CreateProductBodyImagesItemType1,
        )
        from ..models.create_product_body_variants_item import (
            CreateProductBodyVariantsItem,
        )

        d = dict(src_dict)
        name = d.pop("name")

        type_ = CreateProductBodyType(d.pop("type"))

        category = d.pop("category")

        warranty_days = d.pop("warrantyDays")

        variants = []
        _variants = d.pop("variants")
        for variants_item_data in _variants:
            variants_item = CreateProductBodyVariantsItem.from_dict(variants_item_data)

            variants.append(variants_item)

        sales_page = d.pop("salesPage", UNSET)

        description = d.pop("description", UNSET)

        enabled = d.pop("enabled", UNSET)

        language = d.pop("language", UNSET)

        external_reference = d.pop("externalReference", UNSET)

        _images = d.pop("images", UNSET)
        images: list[CreateProductBodyImagesItemType1 | str] | Unset = UNSET
        if _images is not UNSET:
            images = []
            for images_item_data in _images:

                def _parse_images_item(
                    data: object,
                ) -> CreateProductBodyImagesItemType1 | str:
                    try:
                        if not isinstance(data, dict):
                            raise TypeError()
                        images_item_type_1 = CreateProductBodyImagesItemType1.from_dict(
                            data
                        )

                        return images_item_type_1
                    except (TypeError, ValueError, AttributeError, KeyError):
                        pass
                    return cast(CreateProductBodyImagesItemType1 | str, data)

                images_item = _parse_images_item(images_item_data)

                images.append(images_item)

        create_product_body = cls(
            name=name,
            type_=type_,
            category=category,
            warranty_days=warranty_days,
            variants=variants,
            sales_page=sales_page,
            description=description,
            enabled=enabled,
            language=language,
            external_reference=external_reference,
            images=images,
        )

        return create_product_body
