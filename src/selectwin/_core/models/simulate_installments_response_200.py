from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.simulate_installments_response_200_resource import (
    SimulateInstallmentsResponse200Resource,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.simulate_installments_response_200_installments_item import (
        SimulateInstallmentsResponse200InstallmentsItem,
    )
    from ..models.simulate_installments_response_200_links import (
        SimulateInstallmentsResponse200Links,
    )
    from ..models.simulate_installments_response_200_merchant import (
        SimulateInstallmentsResponse200Merchant,
    )


T = TypeVar("T", bound="SimulateInstallmentsResponse200")


@_attrs_define
class SimulateInstallmentsResponse200:
    """
    Attributes:
        plan_id (None | str):
        resource (SimulateInstallmentsResponse200Resource):
        installments (list[SimulateInstallmentsResponse200InstallmentsItem]):
        field_links (SimulateInstallmentsResponse200Links):
        merchant (SimulateInstallmentsResponse200Merchant | Unset):
    """

    plan_id: None | str
    resource: SimulateInstallmentsResponse200Resource
    installments: list[SimulateInstallmentsResponse200InstallmentsItem]
    field_links: SimulateInstallmentsResponse200Links
    merchant: SimulateInstallmentsResponse200Merchant | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        plan_id: None | str
        plan_id = self.plan_id

        resource = self.resource.value

        installments = []
        for installments_item_data in self.installments:
            installments_item = installments_item_data.to_dict()
            installments.append(installments_item)

        field_links = self.field_links.to_dict()

        merchant: dict[str, Any] | Unset = UNSET
        if not isinstance(self.merchant, Unset):
            merchant = self.merchant.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "planId": plan_id,
                "resource": resource,
                "installments": installments,
                "_links": field_links,
            }
        )
        if merchant is not UNSET:
            field_dict["merchant"] = merchant

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.simulate_installments_response_200_installments_item import (
            SimulateInstallmentsResponse200InstallmentsItem,
        )
        from ..models.simulate_installments_response_200_links import (
            SimulateInstallmentsResponse200Links,
        )
        from ..models.simulate_installments_response_200_merchant import (
            SimulateInstallmentsResponse200Merchant,
        )

        d = dict(src_dict)

        def _parse_plan_id(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        plan_id = _parse_plan_id(d.pop("planId"))

        resource = SimulateInstallmentsResponse200Resource(d.pop("resource"))

        installments = []
        _installments = d.pop("installments")
        for installments_item_data in _installments:
            installments_item = (
                SimulateInstallmentsResponse200InstallmentsItem.from_dict(
                    installments_item_data
                )
            )

            installments.append(installments_item)

        field_links = SimulateInstallmentsResponse200Links.from_dict(d.pop("_links"))

        _merchant = d.pop("merchant", UNSET)
        merchant: SimulateInstallmentsResponse200Merchant | Unset
        if isinstance(_merchant, Unset):
            merchant = UNSET
        else:
            merchant = SimulateInstallmentsResponse200Merchant.from_dict(_merchant)

        simulate_installments_response_200 = cls(
            plan_id=plan_id,
            resource=resource,
            installments=installments,
            field_links=field_links,
            merchant=merchant,
        )

        return simulate_installments_response_200
