from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.update_checkout_session_response_200_line_items_item_metadata_type_0 import (
        UpdateCheckoutSessionResponse200LineItemsItemMetadataType0,
    )


T = TypeVar("T", bound="UpdateCheckoutSessionResponse200LineItemsItem")


@_attrs_define
class UpdateCheckoutSessionResponse200LineItemsItem:
    """
    Attributes:
        id (None | str):
        name (None | str):
        quantity (int):
        unit_price (float | None):
        currency (str):
        is_orderbump (bool):
        is_upsell (bool):
        metadata (None | UpdateCheckoutSessionResponse200LineItemsItemMetadataType0):
        external_reference (None | str):
    """

    id: None | str
    name: None | str
    quantity: int
    unit_price: float | None
    currency: str
    is_orderbump: bool
    is_upsell: bool
    metadata: None | UpdateCheckoutSessionResponse200LineItemsItemMetadataType0
    external_reference: None | str

    def to_dict(self) -> dict[str, Any]:
        from ..models.update_checkout_session_response_200_line_items_item_metadata_type_0 import (
            UpdateCheckoutSessionResponse200LineItemsItemMetadataType0,
        )

        id: None | str
        id = self.id

        name: None | str
        name = self.name

        quantity = self.quantity

        unit_price: float | None
        unit_price = self.unit_price

        currency = self.currency

        is_orderbump = self.is_orderbump

        is_upsell = self.is_upsell

        metadata: dict[str, Any] | None
        if isinstance(
            self.metadata, UpdateCheckoutSessionResponse200LineItemsItemMetadataType0
        ):
            metadata = self.metadata.to_dict()
        else:
            metadata = self.metadata

        external_reference: None | str
        external_reference = self.external_reference

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "id": id,
                "name": name,
                "quantity": quantity,
                "unitPrice": unit_price,
                "currency": currency,
                "isOrderbump": is_orderbump,
                "isUpsell": is_upsell,
                "metadata": metadata,
                "externalReference": external_reference,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.update_checkout_session_response_200_line_items_item_metadata_type_0 import (
            UpdateCheckoutSessionResponse200LineItemsItemMetadataType0,
        )

        d = dict(src_dict)

        def _parse_id(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        id = _parse_id(d.pop("id"))

        def _parse_name(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        name = _parse_name(d.pop("name"))

        quantity = d.pop("quantity")

        def _parse_unit_price(data: object) -> float | None:
            if data is None:
                return data
            return cast(float | None, data)

        unit_price = _parse_unit_price(d.pop("unitPrice"))

        currency = d.pop("currency")

        is_orderbump = d.pop("isOrderbump")

        is_upsell = d.pop("isUpsell")

        def _parse_metadata(
            data: object,
        ) -> None | UpdateCheckoutSessionResponse200LineItemsItemMetadataType0:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                metadata_type_0 = UpdateCheckoutSessionResponse200LineItemsItemMetadataType0.from_dict(
                    data
                )

                return metadata_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                None | UpdateCheckoutSessionResponse200LineItemsItemMetadataType0, data
            )

        metadata = _parse_metadata(d.pop("metadata"))

        def _parse_external_reference(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        external_reference = _parse_external_reference(d.pop("externalReference"))

        update_checkout_session_response_200_line_items_item = cls(
            id=id,
            name=name,
            quantity=quantity,
            unit_price=unit_price,
            currency=currency,
            is_orderbump=is_orderbump,
            is_upsell=is_upsell,
            metadata=metadata,
            external_reference=external_reference,
        )

        return update_checkout_session_response_200_line_items_item
