from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.simulate_payment_methods_response_200_resource import (
    SimulatePaymentMethodsResponse200Resource,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.simulate_payment_methods_response_200_amount import (
        SimulatePaymentMethodsResponse200Amount,
    )
    from ..models.simulate_payment_methods_response_200_links import (
        SimulatePaymentMethodsResponse200Links,
    )
    from ..models.simulate_payment_methods_response_200_merchant import (
        SimulatePaymentMethodsResponse200Merchant,
    )
    from ..models.simulate_payment_methods_response_200_original import (
        SimulatePaymentMethodsResponse200Original,
    )
    from ..models.simulate_payment_methods_response_200_total_fees import (
        SimulatePaymentMethodsResponse200TotalFees,
    )


T = TypeVar("T", bound="SimulatePaymentMethodsResponse200")


@_attrs_define
class SimulatePaymentMethodsResponse200:
    """
    Attributes:
        plan_id (None | str):
        resource (SimulatePaymentMethodsResponse200Resource):
        is_custom (bool):
        amount (SimulatePaymentMethodsResponse200Amount):
        original (SimulatePaymentMethodsResponse200Original):
        total_fees (SimulatePaymentMethodsResponse200TotalFees):
        field_links (SimulatePaymentMethodsResponse200Links):
        merchant (SimulatePaymentMethodsResponse200Merchant | Unset):
    """

    plan_id: None | str
    resource: SimulatePaymentMethodsResponse200Resource
    is_custom: bool
    amount: SimulatePaymentMethodsResponse200Amount
    original: SimulatePaymentMethodsResponse200Original
    total_fees: SimulatePaymentMethodsResponse200TotalFees
    field_links: SimulatePaymentMethodsResponse200Links
    merchant: SimulatePaymentMethodsResponse200Merchant | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        plan_id: None | str
        plan_id = self.plan_id

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
                "planId": plan_id,
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
        from ..models.simulate_payment_methods_response_200_amount import (
            SimulatePaymentMethodsResponse200Amount,
        )
        from ..models.simulate_payment_methods_response_200_links import (
            SimulatePaymentMethodsResponse200Links,
        )
        from ..models.simulate_payment_methods_response_200_merchant import (
            SimulatePaymentMethodsResponse200Merchant,
        )
        from ..models.simulate_payment_methods_response_200_original import (
            SimulatePaymentMethodsResponse200Original,
        )
        from ..models.simulate_payment_methods_response_200_total_fees import (
            SimulatePaymentMethodsResponse200TotalFees,
        )

        d = dict(src_dict)

        def _parse_plan_id(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        plan_id = _parse_plan_id(d.pop("planId"))

        resource = SimulatePaymentMethodsResponse200Resource(d.pop("resource"))

        is_custom = d.pop("isCustom")

        amount = SimulatePaymentMethodsResponse200Amount.from_dict(d.pop("amount"))

        original = SimulatePaymentMethodsResponse200Original.from_dict(
            d.pop("original")
        )

        total_fees = SimulatePaymentMethodsResponse200TotalFees.from_dict(
            d.pop("totalFees")
        )

        field_links = SimulatePaymentMethodsResponse200Links.from_dict(d.pop("_links"))

        _merchant = d.pop("merchant", UNSET)
        merchant: SimulatePaymentMethodsResponse200Merchant | Unset
        if isinstance(_merchant, Unset):
            merchant = UNSET
        else:
            merchant = SimulatePaymentMethodsResponse200Merchant.from_dict(_merchant)

        simulate_payment_methods_response_200 = cls(
            plan_id=plan_id,
            resource=resource,
            is_custom=is_custom,
            amount=amount,
            original=original,
            total_fees=total_fees,
            field_links=field_links,
            merchant=merchant,
        )

        return simulate_payment_methods_response_200
