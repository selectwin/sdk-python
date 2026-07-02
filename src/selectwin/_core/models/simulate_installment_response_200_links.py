from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.simulate_installment_response_200_links_installments import (
        SimulateInstallmentResponse200LinksInstallments,
    )
    from ..models.simulate_installment_response_200_links_payment_methods import (
        SimulateInstallmentResponse200LinksPaymentMethods,
    )
    from ..models.simulate_installment_response_200_links_self import (
        SimulateInstallmentResponse200LinksSelf,
    )


T = TypeVar("T", bound="SimulateInstallmentResponse200Links")


@_attrs_define
class SimulateInstallmentResponse200Links:
    """
    Attributes:
        self_ (SimulateInstallmentResponse200LinksSelf):
        installments (SimulateInstallmentResponse200LinksInstallments):
        payment_methods (SimulateInstallmentResponse200LinksPaymentMethods):
    """

    self_: SimulateInstallmentResponse200LinksSelf
    installments: SimulateInstallmentResponse200LinksInstallments
    payment_methods: SimulateInstallmentResponse200LinksPaymentMethods

    def to_dict(self) -> dict[str, Any]:
        self_ = self.self_.to_dict()

        installments = self.installments.to_dict()

        payment_methods = self.payment_methods.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "self": self_,
                "installments": installments,
                "paymentMethods": payment_methods,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.simulate_installment_response_200_links_installments import (
            SimulateInstallmentResponse200LinksInstallments,
        )
        from ..models.simulate_installment_response_200_links_payment_methods import (
            SimulateInstallmentResponse200LinksPaymentMethods,
        )
        from ..models.simulate_installment_response_200_links_self import (
            SimulateInstallmentResponse200LinksSelf,
        )

        d = dict(src_dict)
        self_ = SimulateInstallmentResponse200LinksSelf.from_dict(d.pop("self"))

        installments = SimulateInstallmentResponse200LinksInstallments.from_dict(
            d.pop("installments")
        )

        payment_methods = SimulateInstallmentResponse200LinksPaymentMethods.from_dict(
            d.pop("paymentMethods")
        )

        simulate_installment_response_200_links = cls(
            self_=self_,
            installments=installments,
            payment_methods=payment_methods,
        )

        return simulate_installment_response_200_links
