from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.update_subscription_item_put_response_200_images_type_0_item_type_1 import (
        UpdateSubscriptionItemPutResponse200ImagesType0ItemType1,
    )
    from ..models.update_subscription_item_put_response_200_links import (
        UpdateSubscriptionItemPutResponse200Links,
    )
    from ..models.update_subscription_item_put_response_200_merchant import (
        UpdateSubscriptionItemPutResponse200Merchant,
    )
    from ..models.update_subscription_item_put_response_200_metadata_type_0 import (
        UpdateSubscriptionItemPutResponse200MetadataType0,
    )


T = TypeVar("T", bound="UpdateSubscriptionItemPutResponse200")


@_attrs_define
class UpdateSubscriptionItemPutResponse200:
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
        images (list[str | UpdateSubscriptionItemPutResponse200ImagesType0ItemType1] | None):
        metadata (None | UpdateSubscriptionItemPutResponse200MetadataType0):
        external_reference (None | str):
        updated_at (str):
        created_at (str):
        merchant (UpdateSubscriptionItemPutResponse200Merchant | Unset):
        field_links (UpdateSubscriptionItemPutResponse200Links | Unset):
    """

    id: str
    name: str
    description: None | str
    enabled: bool
    pricing_schema: str
    unit_price: int
    quantity: int
    currency: str
    images: list[str | UpdateSubscriptionItemPutResponse200ImagesType0ItemType1] | None
    metadata: None | UpdateSubscriptionItemPutResponse200MetadataType0
    external_reference: None | str
    updated_at: str
    created_at: str
    merchant: UpdateSubscriptionItemPutResponse200Merchant | Unset = UNSET
    field_links: UpdateSubscriptionItemPutResponse200Links | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.update_subscription_item_put_response_200_images_type_0_item_type_1 import (
            UpdateSubscriptionItemPutResponse200ImagesType0ItemType1,
        )
        from ..models.update_subscription_item_put_response_200_metadata_type_0 import (
            UpdateSubscriptionItemPutResponse200MetadataType0,
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
                    UpdateSubscriptionItemPutResponse200ImagesType0ItemType1,
                ):
                    images_type_0_item = images_type_0_item_data.to_dict()
                else:
                    images_type_0_item = images_type_0_item_data
                images.append(images_type_0_item)

        else:
            images = self.images

        metadata: dict[str, Any] | None
        if isinstance(self.metadata, UpdateSubscriptionItemPutResponse200MetadataType0):
            metadata = self.metadata.to_dict()
        else:
            metadata = self.metadata

        external_reference: None | str
        external_reference = self.external_reference

        updated_at = self.updated_at

        created_at = self.created_at

        merchant: dict[str, Any] | Unset = UNSET
        if not isinstance(self.merchant, Unset):
            merchant = self.merchant.to_dict()

        field_links: dict[str, Any] | Unset = UNSET
        if not isinstance(self.field_links, Unset):
            field_links = self.field_links.to_dict()

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
        if merchant is not UNSET:
            field_dict["merchant"] = merchant
        if field_links is not UNSET:
            field_dict["_links"] = field_links

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.update_subscription_item_put_response_200_images_type_0_item_type_1 import (
            UpdateSubscriptionItemPutResponse200ImagesType0ItemType1,
        )
        from ..models.update_subscription_item_put_response_200_links import (
            UpdateSubscriptionItemPutResponse200Links,
        )
        from ..models.update_subscription_item_put_response_200_merchant import (
            UpdateSubscriptionItemPutResponse200Merchant,
        )
        from ..models.update_subscription_item_put_response_200_metadata_type_0 import (
            UpdateSubscriptionItemPutResponse200MetadataType0,
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
            list[str | UpdateSubscriptionItemPutResponse200ImagesType0ItemType1] | None
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
                    ) -> str | UpdateSubscriptionItemPutResponse200ImagesType0ItemType1:
                        try:
                            if not isinstance(data, dict):
                                raise TypeError()
                            images_type_0_item_type_1 = UpdateSubscriptionItemPutResponse200ImagesType0ItemType1.from_dict(
                                data
                            )

                            return images_type_0_item_type_1
                        except (TypeError, ValueError, AttributeError, KeyError):
                            pass
                        return cast(
                            str
                            | UpdateSubscriptionItemPutResponse200ImagesType0ItemType1,
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
                list[str | UpdateSubscriptionItemPutResponse200ImagesType0ItemType1]
                | None,
                data,
            )

        images = _parse_images(d.pop("images"))

        def _parse_metadata(
            data: object,
        ) -> None | UpdateSubscriptionItemPutResponse200MetadataType0:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                metadata_type_0 = (
                    UpdateSubscriptionItemPutResponse200MetadataType0.from_dict(data)
                )

                return metadata_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | UpdateSubscriptionItemPutResponse200MetadataType0, data)

        metadata = _parse_metadata(d.pop("metadata"))

        def _parse_external_reference(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        external_reference = _parse_external_reference(d.pop("externalReference"))

        updated_at = d.pop("updatedAt")

        created_at = d.pop("createdAt")

        _merchant = d.pop("merchant", UNSET)
        merchant: UpdateSubscriptionItemPutResponse200Merchant | Unset
        if isinstance(_merchant, Unset):
            merchant = UNSET
        else:
            merchant = UpdateSubscriptionItemPutResponse200Merchant.from_dict(_merchant)

        _field_links = d.pop("_links", UNSET)
        field_links: UpdateSubscriptionItemPutResponse200Links | Unset
        if isinstance(_field_links, Unset):
            field_links = UNSET
        else:
            field_links = UpdateSubscriptionItemPutResponse200Links.from_dict(
                _field_links
            )

        update_subscription_item_put_response_200 = cls(
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
            merchant=merchant,
            field_links=field_links,
        )

        return update_subscription_item_put_response_200
