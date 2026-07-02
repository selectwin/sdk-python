from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.update_product_put_body_type import UpdateProductPutBodyType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.update_product_put_body_images_item_type_1 import (
        UpdateProductPutBodyImagesItemType1,
    )


T = TypeVar("T", bound="UpdateProductPutBody")


@_attrs_define
class UpdateProductPutBody:
    """
    Attributes:
        name (str | Unset):
        sales_page (str | Unset):
        description (str | Unset):
        enabled (bool | Unset):  Default: True.
        type_ (UpdateProductPutBodyType | Unset):
        language (str | Unset):  Default: 'pt-BR'.
        category (str | Unset):
        external_reference (str | Unset):
        warranty_days (int | Unset):
        images (list[str | UpdateProductPutBodyImagesItemType1] | Unset):
    """

    name: str | Unset = UNSET
    sales_page: str | Unset = UNSET
    description: str | Unset = UNSET
    enabled: bool | Unset = True
    type_: UpdateProductPutBodyType | Unset = UNSET
    language: str | Unset = "pt-BR"
    category: str | Unset = UNSET
    external_reference: str | Unset = UNSET
    warranty_days: int | Unset = UNSET
    images: list[str | UpdateProductPutBodyImagesItemType1] | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.update_product_put_body_images_item_type_1 import (
            UpdateProductPutBodyImagesItemType1,
        )

        name = self.name

        sales_page = self.sales_page

        description = self.description

        enabled = self.enabled

        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        language = self.language

        category = self.category

        external_reference = self.external_reference

        warranty_days = self.warranty_days

        images: list[dict[str, Any] | str] | Unset = UNSET
        if not isinstance(self.images, Unset):
            images = []
            for images_item_data in self.images:
                images_item: dict[str, Any] | str
                if isinstance(images_item_data, UpdateProductPutBodyImagesItemType1):
                    images_item = images_item_data.to_dict()
                else:
                    images_item = images_item_data
                images.append(images_item)

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if sales_page is not UNSET:
            field_dict["salesPage"] = sales_page
        if description is not UNSET:
            field_dict["description"] = description
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if type_ is not UNSET:
            field_dict["type"] = type_
        if language is not UNSET:
            field_dict["language"] = language
        if category is not UNSET:
            field_dict["category"] = category
        if external_reference is not UNSET:
            field_dict["externalReference"] = external_reference
        if warranty_days is not UNSET:
            field_dict["warrantyDays"] = warranty_days
        if images is not UNSET:
            field_dict["images"] = images

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.update_product_put_body_images_item_type_1 import (
            UpdateProductPutBodyImagesItemType1,
        )

        d = dict(src_dict)
        name = d.pop("name", UNSET)

        sales_page = d.pop("salesPage", UNSET)

        description = d.pop("description", UNSET)

        enabled = d.pop("enabled", UNSET)

        _type_ = d.pop("type", UNSET)
        type_: UpdateProductPutBodyType | Unset
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = UpdateProductPutBodyType(_type_)

        language = d.pop("language", UNSET)

        category = d.pop("category", UNSET)

        external_reference = d.pop("externalReference", UNSET)

        warranty_days = d.pop("warrantyDays", UNSET)

        _images = d.pop("images", UNSET)
        images: list[str | UpdateProductPutBodyImagesItemType1] | Unset = UNSET
        if _images is not UNSET:
            images = []
            for images_item_data in _images:

                def _parse_images_item(
                    data: object,
                ) -> str | UpdateProductPutBodyImagesItemType1:
                    try:
                        if not isinstance(data, dict):
                            raise TypeError()
                        images_item_type_1 = (
                            UpdateProductPutBodyImagesItemType1.from_dict(data)
                        )

                        return images_item_type_1
                    except (TypeError, ValueError, AttributeError, KeyError):
                        pass
                    return cast(str | UpdateProductPutBodyImagesItemType1, data)

                images_item = _parse_images_item(images_item_data)

                images.append(images_item)

        update_product_put_body = cls(
            name=name,
            sales_page=sales_page,
            description=description,
            enabled=enabled,
            type_=type_,
            language=language,
            category=category,
            external_reference=external_reference,
            warranty_days=warranty_days,
            images=images,
        )

        return update_product_put_body
