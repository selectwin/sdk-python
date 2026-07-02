from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.simulate_payment_methods_response_200_links_installment import (
        SimulatePaymentMethodsResponse200LinksInstallment,
    )
    from ..models.simulate_payment_methods_response_200_links_installments import (
        SimulatePaymentMethodsResponse200LinksInstallments,
    )
    from ..models.simulate_payment_methods_response_200_links_self import (
        SimulatePaymentMethodsResponse200LinksSelf,
    )


T = TypeVar("T", bound="SimulatePaymentMethodsResponse200Links")


@_attrs_define
class SimulatePaymentMethodsResponse200Links:
    """
    Attributes:
        self_ (SimulatePaymentMethodsResponse200LinksSelf):
        installment (SimulatePaymentMethodsResponse200LinksInstallment):
        installments (SimulatePaymentMethodsResponse200LinksInstallments):
    """

    self_: SimulatePaymentMethodsResponse200LinksSelf
    installment: SimulatePaymentMethodsResponse200LinksInstallment
    installments: SimulatePaymentMethodsResponse200LinksInstallments

    def to_dict(self) -> dict[str, Any]:
        self_ = self.self_.to_dict()

        installment = self.installment.to_dict()

        installments = self.installments.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "self": self_,
                "installment": installment,
                "installments": installments,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.simulate_payment_methods_response_200_links_installment import (
            SimulatePaymentMethodsResponse200LinksInstallment,
        )
        from ..models.simulate_payment_methods_response_200_links_installments import (
            SimulatePaymentMethodsResponse200LinksInstallments,
        )
        from ..models.simulate_payment_methods_response_200_links_self import (
            SimulatePaymentMethodsResponse200LinksSelf,
        )

        d = dict(src_dict)
        self_ = SimulatePaymentMethodsResponse200LinksSelf.from_dict(d.pop("self"))

        installment = SimulatePaymentMethodsResponse200LinksInstallment.from_dict(
            d.pop("installment")
        )

        installments = SimulatePaymentMethodsResponse200LinksInstallments.from_dict(
            d.pop("installments")
        )

        simulate_payment_methods_response_200_links = cls(
            self_=self_,
            installment=installment,
            installments=installments,
        )

        return simulate_payment_methods_response_200_links
