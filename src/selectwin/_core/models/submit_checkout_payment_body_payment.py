from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..models.submit_checkout_payment_body_payment_method import (
    SubmitCheckoutPaymentBodyPaymentMethod,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="SubmitCheckoutPaymentBodyPayment")


@_attrs_define
class SubmitCheckoutPaymentBodyPayment:
    """
    Attributes:
        method (SubmitCheckoutPaymentBodyPaymentMethod):
        card_id (str | Unset): Public identifier (card_…)
        installments (int | Unset):  Default: 1.
        capture (bool | Unset):  Default: True.
    """

    method: SubmitCheckoutPaymentBodyPaymentMethod
    card_id: str | Unset = UNSET
    installments: int | Unset = 1
    capture: bool | Unset = True

    def to_dict(self) -> dict[str, Any]:
        method = self.method.value

        card_id = self.card_id

        installments = self.installments

        capture = self.capture

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "method": method,
            }
        )
        if card_id is not UNSET:
            field_dict["cardId"] = card_id
        if installments is not UNSET:
            field_dict["installments"] = installments
        if capture is not UNSET:
            field_dict["capture"] = capture

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        method = SubmitCheckoutPaymentBodyPaymentMethod(d.pop("method"))

        card_id = d.pop("cardId", UNSET)

        installments = d.pop("installments", UNSET)

        capture = d.pop("capture", UNSET)

        submit_checkout_payment_body_payment = cls(
            method=method,
            card_id=card_id,
            installments=installments,
            capture=capture,
        )

        return submit_checkout_payment_body_payment
