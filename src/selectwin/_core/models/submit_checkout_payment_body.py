from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.submit_checkout_payment_body_payment import (
        SubmitCheckoutPaymentBodyPayment,
    )


T = TypeVar("T", bound="SubmitCheckoutPaymentBody")


@_attrs_define
class SubmitCheckoutPaymentBody:
    """
    Attributes:
        payment (SubmitCheckoutPaymentBodyPayment):
    """

    payment: SubmitCheckoutPaymentBodyPayment

    def to_dict(self) -> dict[str, Any]:
        payment = self.payment.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "payment": payment,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.submit_checkout_payment_body_payment import (
            SubmitCheckoutPaymentBodyPayment,
        )

        d = dict(src_dict)
        payment = SubmitCheckoutPaymentBodyPayment.from_dict(d.pop("payment"))

        submit_checkout_payment_body = cls(
            payment=payment,
        )

        return submit_checkout_payment_body
