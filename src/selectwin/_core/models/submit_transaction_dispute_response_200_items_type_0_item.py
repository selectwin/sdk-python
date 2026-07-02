from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="SubmitTransactionDisputeResponse200ItemsType0Item")


@_attrs_define
class SubmitTransactionDisputeResponse200ItemsType0Item:
    """
    Attributes:
        id (str): Public identifier (item_/tri_…)
        name (str):
        unit_price (int):
        quantity (int):
        currency (None | str):
        description (None | str):
        images (list[str] | None):
        is_upsell (bool | None):
        is_orderbump (bool | None):
        variant_id (None | str):
        external_reference (None | str):
        updated_at (None | str):
        created_at (None | str):
        metadata (Any | Unset):
    """

    id: str
    name: str
    unit_price: int
    quantity: int
    currency: None | str
    description: None | str
    images: list[str] | None
    is_upsell: bool | None
    is_orderbump: bool | None
    variant_id: None | str
    external_reference: None | str
    updated_at: None | str
    created_at: None | str
    metadata: Any | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        unit_price = self.unit_price

        quantity = self.quantity

        currency: None | str
        currency = self.currency

        description: None | str
        description = self.description

        images: list[str] | None
        if isinstance(self.images, list):
            images = self.images

        else:
            images = self.images

        is_upsell: bool | None
        is_upsell = self.is_upsell

        is_orderbump: bool | None
        is_orderbump = self.is_orderbump

        variant_id: None | str
        variant_id = self.variant_id

        external_reference: None | str
        external_reference = self.external_reference

        updated_at: None | str
        updated_at = self.updated_at

        created_at: None | str
        created_at = self.created_at

        metadata = self.metadata

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "id": id,
                "name": name,
                "unitPrice": unit_price,
                "quantity": quantity,
                "currency": currency,
                "description": description,
                "images": images,
                "isUpsell": is_upsell,
                "isOrderbump": is_orderbump,
                "variantId": variant_id,
                "externalReference": external_reference,
                "updatedAt": updated_at,
                "createdAt": created_at,
            }
        )
        if metadata is not UNSET:
            field_dict["metadata"] = metadata

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        name = d.pop("name")

        unit_price = d.pop("unitPrice")

        quantity = d.pop("quantity")

        def _parse_currency(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        currency = _parse_currency(d.pop("currency"))

        def _parse_description(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        description = _parse_description(d.pop("description"))

        def _parse_images(data: object) -> list[str] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                images_type_0 = cast(list[str], data)

                return images_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None, data)

        images = _parse_images(d.pop("images"))

        def _parse_is_upsell(data: object) -> bool | None:
            if data is None:
                return data
            return cast(bool | None, data)

        is_upsell = _parse_is_upsell(d.pop("isUpsell"))

        def _parse_is_orderbump(data: object) -> bool | None:
            if data is None:
                return data
            return cast(bool | None, data)

        is_orderbump = _parse_is_orderbump(d.pop("isOrderbump"))

        def _parse_variant_id(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        variant_id = _parse_variant_id(d.pop("variantId"))

        def _parse_external_reference(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        external_reference = _parse_external_reference(d.pop("externalReference"))

        def _parse_updated_at(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        updated_at = _parse_updated_at(d.pop("updatedAt"))

        def _parse_created_at(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        created_at = _parse_created_at(d.pop("createdAt"))

        metadata = d.pop("metadata", UNSET)

        submit_transaction_dispute_response_200_items_type_0_item = cls(
            id=id,
            name=name,
            unit_price=unit_price,
            quantity=quantity,
            currency=currency,
            description=description,
            images=images,
            is_upsell=is_upsell,
            is_orderbump=is_orderbump,
            variant_id=variant_id,
            external_reference=external_reference,
            updated_at=updated_at,
            created_at=created_at,
            metadata=metadata,
        )

        return submit_transaction_dispute_response_200_items_type_0_item
