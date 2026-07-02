from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.resume_subscription_response_200_items_item_images_type_0_item_type_1 import (
        ResumeSubscriptionResponse200ItemsItemImagesType0ItemType1,
    )
    from ..models.resume_subscription_response_200_items_item_metadata_type_0 import (
        ResumeSubscriptionResponse200ItemsItemMetadataType0,
    )


T = TypeVar("T", bound="ResumeSubscriptionResponse200ItemsItem")


@_attrs_define
class ResumeSubscriptionResponse200ItemsItem:
    """
    Attributes:
        id (str): Public identifier (sit_/item_…)
        name (str):
        description (None | str):
        enabled (bool):
        pricing_schema (str):
        unit_price (int):
        quantity (int):
        currency (str):
        images (list[ResumeSubscriptionResponse200ItemsItemImagesType0ItemType1 | str] | None):
        metadata (None | ResumeSubscriptionResponse200ItemsItemMetadataType0):
        external_reference (None | str):
        updated_at (str):
        created_at (str):
    """

    id: str
    name: str
    description: None | str
    enabled: bool
    pricing_schema: str
    unit_price: int
    quantity: int
    currency: str
    images: (
        list[ResumeSubscriptionResponse200ItemsItemImagesType0ItemType1 | str] | None
    )
    metadata: None | ResumeSubscriptionResponse200ItemsItemMetadataType0
    external_reference: None | str
    updated_at: str
    created_at: str

    def to_dict(self) -> dict[str, Any]:
        from ..models.resume_subscription_response_200_items_item_images_type_0_item_type_1 import (
            ResumeSubscriptionResponse200ItemsItemImagesType0ItemType1,
        )
        from ..models.resume_subscription_response_200_items_item_metadata_type_0 import (
            ResumeSubscriptionResponse200ItemsItemMetadataType0,
        )

        id = self.id

        name = self.name

        description: None | str
        description = self.description

        enabled = self.enabled

        pricing_schema = self.pricing_schema

        unit_price = self.unit_price

        quantity = self.quantity

        currency = self.currency

        images: list[dict[str, Any] | str] | None
        if isinstance(self.images, list):
            images = []
            for images_type_0_item_data in self.images:
                images_type_0_item: dict[str, Any] | str
                if isinstance(
                    images_type_0_item_data,
                    ResumeSubscriptionResponse200ItemsItemImagesType0ItemType1,
                ):
                    images_type_0_item = images_type_0_item_data.to_dict()
                else:
                    images_type_0_item = images_type_0_item_data
                images.append(images_type_0_item)

        else:
            images = self.images

        metadata: dict[str, Any] | None
        if isinstance(
            self.metadata, ResumeSubscriptionResponse200ItemsItemMetadataType0
        ):
            metadata = self.metadata.to_dict()
        else:
            metadata = self.metadata

        external_reference: None | str
        external_reference = self.external_reference

        updated_at = self.updated_at

        created_at = self.created_at

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "id": id,
                "name": name,
                "description": description,
                "enabled": enabled,
                "pricingSchema": pricing_schema,
                "unitPrice": unit_price,
                "quantity": quantity,
                "currency": currency,
                "images": images,
                "metadata": metadata,
                "externalReference": external_reference,
                "updatedAt": updated_at,
                "createdAt": created_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.resume_subscription_response_200_items_item_images_type_0_item_type_1 import (
            ResumeSubscriptionResponse200ItemsItemImagesType0ItemType1,
        )
        from ..models.resume_subscription_response_200_items_item_metadata_type_0 import (
            ResumeSubscriptionResponse200ItemsItemMetadataType0,
        )

        d = dict(src_dict)
        id = d.pop("id")

        name = d.pop("name")

        def _parse_description(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        description = _parse_description(d.pop("description"))

        enabled = d.pop("enabled")

        pricing_schema = d.pop("pricingSchema")

        unit_price = d.pop("unitPrice")

        quantity = d.pop("quantity")

        currency = d.pop("currency")

        def _parse_images(
            data: object,
        ) -> (
            list[ResumeSubscriptionResponse200ItemsItemImagesType0ItemType1 | str]
            | None
        ):
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
                    ) -> (
                        ResumeSubscriptionResponse200ItemsItemImagesType0ItemType1 | str
                    ):
                        try:
                            if not isinstance(data, dict):
                                raise TypeError()
                            images_type_0_item_type_1 = ResumeSubscriptionResponse200ItemsItemImagesType0ItemType1.from_dict(
                                data
                            )

                            return images_type_0_item_type_1
                        except (TypeError, ValueError, AttributeError, KeyError):
                            pass
                        return cast(
                            ResumeSubscriptionResponse200ItemsItemImagesType0ItemType1
                            | str,
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
                list[ResumeSubscriptionResponse200ItemsItemImagesType0ItemType1 | str]
                | None,
                data,
            )

        images = _parse_images(d.pop("images"))

        def _parse_metadata(
            data: object,
        ) -> None | ResumeSubscriptionResponse200ItemsItemMetadataType0:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                metadata_type_0 = (
                    ResumeSubscriptionResponse200ItemsItemMetadataType0.from_dict(data)
                )

                return metadata_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                None | ResumeSubscriptionResponse200ItemsItemMetadataType0, data
            )

        metadata = _parse_metadata(d.pop("metadata"))

        def _parse_external_reference(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        external_reference = _parse_external_reference(d.pop("externalReference"))

        updated_at = d.pop("updatedAt")

        created_at = d.pop("createdAt")

        resume_subscription_response_200_items_item = cls(
            id=id,
            name=name,
            description=description,
            enabled=enabled,
            pricing_schema=pricing_schema,
            unit_price=unit_price,
            quantity=quantity,
            currency=currency,
            images=images,
            metadata=metadata,
            external_reference=external_reference,
            updated_at=updated_at,
            created_at=created_at,
        )

        return resume_subscription_response_200_items_item
