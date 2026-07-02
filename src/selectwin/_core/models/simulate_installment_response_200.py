from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..models.simulate_installment_response_200_resource import (
    SimulateInstallmentResponse200Resource,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.simulate_installment_response_200_amount import (
        SimulateInstallmentResponse200Amount,
    )
    from ..models.simulate_installment_response_200_links import (
        SimulateInstallmentResponse200Links,
    )
    from ..models.simulate_installment_response_200_merchant import (
        SimulateInstallmentResponse200Merchant,
    )
    from ..models.simulate_installment_response_200_original import (
        SimulateInstallmentResponse200Original,
    )
    from ..models.simulate_installment_response_200_total_fees import (
        SimulateInstallmentResponse200TotalFees,
    )


T = TypeVar("T", bound="SimulateInstallmentResponse200")


@_attrs_define
class SimulateInstallmentResponse200:
    """
    Attributes:
        resource (SimulateInstallmentResponse200Resource):
        is_custom (bool):
        amount (SimulateInstallmentResponse200Amount):
        original (SimulateInstallmentResponse200Original):
        total_fees (SimulateInstallmentResponse200TotalFees):
        field_links (SimulateInstallmentResponse200Links):
        merchant (SimulateInstallmentResponse200Merchant | Unset):
    """

    resource: SimulateInstallmentResponse200Resource
    is_custom: bool
    amount: SimulateInstallmentResponse200Amount
    original: SimulateInstallmentResponse200Original
    total_fees: SimulateInstallmentResponse200TotalFees
    field_links: SimulateInstallmentResponse200Links
    merchant: SimulateInstallmentResponse200Merchant | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        resource = self.resource.value

        is_custom = self.is_custom

        amount = self.amount.to_dict()

        original = self.original.to_dict()

        total_fees = self.total_fees.to_dict()

        field_links = self.field_links.to_dict()

        merchant: dict[str, Any] | Unset = UNSET
        if not isinstance(self.merchant, Unset):
            merchant = self.merchant.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "resource": resource,
                "isCustom": is_custom,
                "amount": amount,
                "original": original,
                "totalFees": total_fees,
                "_links": field_links,
            }
        )
        if merchant is not UNSET:
            field_dict["merchant"] = merchant

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.simulate_installment_response_200_amount import (
            SimulateInstallmentResponse200Amount,
        )
        from ..models.simulate_installment_response_200_links import (
            SimulateInstallmentResponse200Links,
        )
        from ..models.simulate_installment_response_200_merchant import (
            SimulateInstallmentResponse200Merchant,
        )
        from ..models.simulate_installment_response_200_original import (
            SimulateInstallmentResponse200Original,
        )
        from ..models.simulate_installment_response_200_total_fees import (
            SimulateInstallmentResponse200TotalFees,
        )

        d = dict(src_dict)
        resource = SimulateInstallmentResponse200Resource(d.pop("resource"))

        is_custom = d.pop("isCustom")

        amount = SimulateInstallmentResponse200Amount.from_dict(d.pop("amount"))

        original = SimulateInstallmentResponse200Original.from_dict(d.pop("original"))

        total_fees = SimulateInstallmentResponse200TotalFees.from_dict(
            d.pop("totalFees")
        )

        field_links = SimulateInstallmentResponse200Links.from_dict(d.pop("_links"))

        _merchant = d.pop("merchant", UNSET)
        merchant: SimulateInstallmentResponse200Merchant | Unset
        if isinstance(_merchant, Unset):
            merchant = UNSET
        else:
            merchant = SimulateInstallmentResponse200Merchant.from_dict(_merchant)

        simulate_installment_response_200 = cls(
            resource=resource,
            is_custom=is_custom,
            amount=amount,
            original=original,
            total_fees=total_fees,
            field_links=field_links,
            merchant=merchant,
        )

        return simulate_installment_response_200
