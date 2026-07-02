from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..models.update_product_variant_body_pricing_transform_quantity_round import (
    UpdateProductVariantBodyPricingTransformQuantityRound,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="UpdateProductVariantBodyPricingTransformQuantity")


@_attrs_define
class UpdateProductVariantBodyPricingTransformQuantity:
    """
    Attributes:
        divide_by (int):
        round_ (UpdateProductVariantBodyPricingTransformQuantityRound | Unset):  Default:
            UpdateProductVariantBodyPricingTransformQuantityRound.UP.
    """

    divide_by: int
    round_: UpdateProductVariantBodyPricingTransformQuantityRound | Unset = (
        UpdateProductVariantBodyPricingTransformQuantityRound.UP
    )

    def to_dict(self) -> dict[str, Any]:
        divide_by = self.divide_by

        round_: str | Unset = UNSET
        if not isinstance(self.round_, Unset):
            round_ = self.round_.value

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "divideBy": divide_by,
            }
        )
        if round_ is not UNSET:
            field_dict["round"] = round_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        divide_by = d.pop("divideBy")

        _round_ = d.pop("round", UNSET)
        round_: UpdateProductVariantBodyPricingTransformQuantityRound | Unset
        if isinstance(_round_, Unset):
            round_ = UNSET
        else:
            round_ = UpdateProductVariantBodyPricingTransformQuantityRound(_round_)

        update_product_variant_body_pricing_transform_quantity = cls(
            divide_by=divide_by,
            round_=round_,
        )

        return update_product_variant_body_pricing_transform_quantity
