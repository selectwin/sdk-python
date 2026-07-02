from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..models.create_subscription_body_payment_method import (
    CreateSubscriptionBodyPaymentMethod,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.create_subscription_body_payment_billet import (
        CreateSubscriptionBodyPaymentBillet,
    )
    from ..models.create_subscription_body_payment_card import (
        CreateSubscriptionBodyPaymentCard,
    )
    from ..models.create_subscription_body_payment_pix import (
        CreateSubscriptionBodyPaymentPix,
    )


T = TypeVar("T", bound="CreateSubscriptionBodyPayment")


@_attrs_define
class CreateSubscriptionBodyPayment:
    """**Regra:** Com `method=credit`, `card` é **obrigatório** (`card.id` de um cartão salvo, ou cartão completo inline:
    holderName, expirationMonth, expirationYear, numbering, securityCode).

        Attributes:
            method (CreateSubscriptionBodyPaymentMethod | Unset):  Default: CreateSubscriptionBodyPaymentMethod.CREDIT.
            card (CreateSubscriptionBodyPaymentCard | Unset):
            installments (int | Unset):  Default: 1.
            pix (CreateSubscriptionBodyPaymentPix | Unset):
            billet (CreateSubscriptionBodyPaymentBillet | Unset):
    """

    method: CreateSubscriptionBodyPaymentMethod | Unset = (
        CreateSubscriptionBodyPaymentMethod.CREDIT
    )
    card: CreateSubscriptionBodyPaymentCard | Unset = UNSET
    installments: int | Unset = 1
    pix: CreateSubscriptionBodyPaymentPix | Unset = UNSET
    billet: CreateSubscriptionBodyPaymentBillet | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        method: str | Unset = UNSET
        if not isinstance(self.method, Unset):
            method = self.method.value

        card: dict[str, Any] | Unset = UNSET
        if not isinstance(self.card, Unset):
            card = self.card.to_dict()

        installments = self.installments

        pix: dict[str, Any] | Unset = UNSET
        if not isinstance(self.pix, Unset):
            pix = self.pix.to_dict()

        billet: dict[str, Any] | Unset = UNSET
        if not isinstance(self.billet, Unset):
            billet = self.billet.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if method is not UNSET:
            field_dict["method"] = method
        if card is not UNSET:
            field_dict["card"] = card
        if installments is not UNSET:
            field_dict["installments"] = installments
        if pix is not UNSET:
            field_dict["pix"] = pix
        if billet is not UNSET:
            field_dict["billet"] = billet

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.create_subscription_body_payment_billet import (
            CreateSubscriptionBodyPaymentBillet,
        )
        from ..models.create_subscription_body_payment_card import (
            CreateSubscriptionBodyPaymentCard,
        )
        from ..models.create_subscription_body_payment_pix import (
            CreateSubscriptionBodyPaymentPix,
        )

        d = dict(src_dict)
        _method = d.pop("method", UNSET)
        method: CreateSubscriptionBodyPaymentMethod | Unset
        if isinstance(_method, Unset):
            method = UNSET
        else:
            method = CreateSubscriptionBodyPaymentMethod(_method)

        _card = d.pop("card", UNSET)
        card: CreateSubscriptionBodyPaymentCard | Unset
        if isinstance(_card, Unset):
            card = UNSET
        else:
            card = CreateSubscriptionBodyPaymentCard.from_dict(_card)

        installments = d.pop("installments", UNSET)

        _pix = d.pop("pix", UNSET)
        pix: CreateSubscriptionBodyPaymentPix | Unset
        if isinstance(_pix, Unset):
            pix = UNSET
        else:
            pix = CreateSubscriptionBodyPaymentPix.from_dict(_pix)

        _billet = d.pop("billet", UNSET)
        billet: CreateSubscriptionBodyPaymentBillet | Unset
        if isinstance(_billet, Unset):
            billet = UNSET
        else:
            billet = CreateSubscriptionBodyPaymentBillet.from_dict(_billet)

        create_subscription_body_payment = cls(
            method=method,
            card=card,
            installments=installments,
            pix=pix,
            billet=billet,
        )

        return create_subscription_body_payment
