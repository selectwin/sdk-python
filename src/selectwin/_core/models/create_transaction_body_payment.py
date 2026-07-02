from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..models.create_transaction_body_payment_method import (
    CreateTransactionBodyPaymentMethod,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.create_transaction_body_payment_billet import (
        CreateTransactionBodyPaymentBillet,
    )
    from ..models.create_transaction_body_payment_card import (
        CreateTransactionBodyPaymentCard,
    )
    from ..models.create_transaction_body_payment_pix import (
        CreateTransactionBodyPaymentPix,
    )


T = TypeVar("T", bound="CreateTransactionBodyPayment")


@_attrs_define
class CreateTransactionBodyPayment:
    """
    Attributes:
        method (CreateTransactionBodyPaymentMethod):
        currency (str | Unset): ISO 4217 currency code Default: 'BRL'.
        installments (int | Unset):  Default: 1.
        capture (bool | Unset):  Default: True.
        finance_installments (bool | Unset):  Default: True.
        card (CreateTransactionBodyPaymentCard | Unset):
        pix (CreateTransactionBodyPaymentPix | Unset):
        billet (CreateTransactionBodyPaymentBillet | Unset):
    """

    method: CreateTransactionBodyPaymentMethod
    currency: str | Unset = "BRL"
    installments: int | Unset = 1
    capture: bool | Unset = True
    finance_installments: bool | Unset = True
    card: CreateTransactionBodyPaymentCard | Unset = UNSET
    pix: CreateTransactionBodyPaymentPix | Unset = UNSET
    billet: CreateTransactionBodyPaymentBillet | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        method = self.method.value

        currency = self.currency

        installments = self.installments

        capture = self.capture

        finance_installments = self.finance_installments

        card: dict[str, Any] | Unset = UNSET
        if not isinstance(self.card, Unset):
            card = self.card.to_dict()

        pix: dict[str, Any] | Unset = UNSET
        if not isinstance(self.pix, Unset):
            pix = self.pix.to_dict()

        billet: dict[str, Any] | Unset = UNSET
        if not isinstance(self.billet, Unset):
            billet = self.billet.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "method": method,
            }
        )
        if currency is not UNSET:
            field_dict["currency"] = currency
        if installments is not UNSET:
            field_dict["installments"] = installments
        if capture is not UNSET:
            field_dict["capture"] = capture
        if finance_installments is not UNSET:
            field_dict["financeInstallments"] = finance_installments
        if card is not UNSET:
            field_dict["card"] = card
        if pix is not UNSET:
            field_dict["pix"] = pix
        if billet is not UNSET:
            field_dict["billet"] = billet

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.create_transaction_body_payment_billet import (
            CreateTransactionBodyPaymentBillet,
        )
        from ..models.create_transaction_body_payment_card import (
            CreateTransactionBodyPaymentCard,
        )
        from ..models.create_transaction_body_payment_pix import (
            CreateTransactionBodyPaymentPix,
        )

        d = dict(src_dict)
        method = CreateTransactionBodyPaymentMethod(d.pop("method"))

        currency = d.pop("currency", UNSET)

        installments = d.pop("installments", UNSET)

        capture = d.pop("capture", UNSET)

        finance_installments = d.pop("financeInstallments", UNSET)

        _card = d.pop("card", UNSET)
        card: CreateTransactionBodyPaymentCard | Unset
        if isinstance(_card, Unset):
            card = UNSET
        else:
            card = CreateTransactionBodyPaymentCard.from_dict(_card)

        _pix = d.pop("pix", UNSET)
        pix: CreateTransactionBodyPaymentPix | Unset
        if isinstance(_pix, Unset):
            pix = UNSET
        else:
            pix = CreateTransactionBodyPaymentPix.from_dict(_pix)

        _billet = d.pop("billet", UNSET)
        billet: CreateTransactionBodyPaymentBillet | Unset
        if isinstance(_billet, Unset):
            billet = UNSET
        else:
            billet = CreateTransactionBodyPaymentBillet.from_dict(_billet)

        create_transaction_body_payment = cls(
            method=method,
            currency=currency,
            installments=installments,
            capture=capture,
            finance_installments=finance_installments,
            card=card,
            pix=pix,
            billet=billet,
        )

        return create_transaction_body_payment
