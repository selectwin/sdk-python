from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateProductBodyVariantsItemPricingTiersItem")


@_attrs_define
class CreateProductBodyVariantsItemPricingTiersItem:
    """
    Attributes:
        unit_price (int):
        up_to (int | None | Unset):
        flat_price (int | None | Unset):
    """

    unit_price: int
    up_to: int | None | Unset = UNSET
    flat_price: int | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        unit_price = self.unit_price

        up_to: int | None | Unset
        if isinstance(self.up_to, Unset):
            up_to = UNSET
        else:
            up_to = self.up_to

        flat_price: int | None | Unset
        if isinstance(self.flat_price, Unset):
            flat_price = UNSET
        else:
            flat_price = self.flat_price

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "unitPrice": unit_price,
            }
        )
        if up_to is not UNSET:
            field_dict["upTo"] = up_to
        if flat_price is not UNSET:
            field_dict["flatPrice"] = flat_price

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        unit_price = d.pop("unitPrice")

        def _parse_up_to(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        up_to = _parse_up_to(d.pop("upTo", UNSET))

        def _parse_flat_price(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        flat_price = _parse_flat_price(d.pop("flatPrice", UNSET))

        create_product_body_variants_item_pricing_tiers_item = cls(
            unit_price=unit_price,
            up_to=up_to,
            flat_price=flat_price,
        )

        return create_product_body_variants_item_pricing_tiers_item
