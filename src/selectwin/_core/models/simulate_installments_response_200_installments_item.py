from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="SimulateInstallmentsResponse200InstallmentsItem")


@_attrs_define
class SimulateInstallmentsResponse200InstallmentsItem:
    """
    Attributes:
        installment (int):
        installment_amount_cents (int):
        total_amount_cents (int):
        extra_fee (bool):
        description (str):
    """

    installment: int
    installment_amount_cents: int
    total_amount_cents: int
    extra_fee: bool
    description: str

    def to_dict(self) -> dict[str, Any]:
        installment = self.installment

        installment_amount_cents = self.installment_amount_cents

        total_amount_cents = self.total_amount_cents

        extra_fee = self.extra_fee

        description = self.description

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "installment": installment,
                "installmentAmountCents": installment_amount_cents,
                "totalAmountCents": total_amount_cents,
                "extraFee": extra_fee,
                "description": description,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        installment = d.pop("installment")

        installment_amount_cents = d.pop("installmentAmountCents")

        total_amount_cents = d.pop("totalAmountCents")

        extra_fee = d.pop("extraFee")

        description = d.pop("description")

        simulate_installments_response_200_installments_item = cls(
            installment=installment,
            installment_amount_cents=installment_amount_cents,
            total_amount_cents=total_amount_cents,
            extra_fee=extra_fee,
            description=description,
        )

        return simulate_installments_response_200_installments_item
