from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="SimulateInstallmentResponse200Original")


@_attrs_define
class SimulateInstallmentResponse200Original:
    """
    Attributes:
        cents (int):
        decimal (float):
    """

    cents: int
    decimal: float

    def to_dict(self) -> dict[str, Any]:
        cents = self.cents

        decimal = self.decimal

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "cents": cents,
                "decimal": decimal,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        cents = d.pop("cents")

        decimal = d.pop("decimal")

        simulate_installment_response_200_original = cls(
            cents=cents,
            decimal=decimal,
        )

        return simulate_installment_response_200_original
