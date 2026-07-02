from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.simulate_installments_response_200_links_installment import (
        SimulateInstallmentsResponse200LinksInstallment,
    )
    from ..models.simulate_installments_response_200_links_payment_methods import (
        SimulateInstallmentsResponse200LinksPaymentMethods,
    )
    from ..models.simulate_installments_response_200_links_self import (
        SimulateInstallmentsResponse200LinksSelf,
    )


T = TypeVar("T", bound="SimulateInstallmentsResponse200Links")


@_attrs_define
class SimulateInstallmentsResponse200Links:
    """
    Attributes:
        self_ (SimulateInstallmentsResponse200LinksSelf):
        installment (SimulateInstallmentsResponse200LinksInstallment):
        payment_methods (SimulateInstallmentsResponse200LinksPaymentMethods):
    """

    self_: SimulateInstallmentsResponse200LinksSelf
    installment: SimulateInstallmentsResponse200LinksInstallment
    payment_methods: SimulateInstallmentsResponse200LinksPaymentMethods

    def to_dict(self) -> dict[str, Any]:
        self_ = self.self_.to_dict()

        installment = self.installment.to_dict()

        payment_methods = self.payment_methods.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "self": self_,
                "installment": installment,
                "paymentMethods": payment_methods,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.simulate_installments_response_200_links_installment import (
            SimulateInstallmentsResponse200LinksInstallment,
        )
        from ..models.simulate_installments_response_200_links_payment_methods import (
            SimulateInstallmentsResponse200LinksPaymentMethods,
        )
        from ..models.simulate_installments_response_200_links_self import (
            SimulateInstallmentsResponse200LinksSelf,
        )

        d = dict(src_dict)
        self_ = SimulateInstallmentsResponse200LinksSelf.from_dict(d.pop("self"))

        installment = SimulateInstallmentsResponse200LinksInstallment.from_dict(
            d.pop("installment")
        )

        payment_methods = SimulateInstallmentsResponse200LinksPaymentMethods.from_dict(
            d.pop("paymentMethods")
        )

        simulate_installments_response_200_links = cls(
            self_=self_,
            installment=installment,
            payment_methods=payment_methods,
        )

        return simulate_installments_response_200_links
