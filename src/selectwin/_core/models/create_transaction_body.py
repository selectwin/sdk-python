from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.create_transaction_body_billing import CreateTransactionBodyBilling
    from ..models.create_transaction_body_callback import CreateTransactionBodyCallback
    from ..models.create_transaction_body_customer import CreateTransactionBodyCustomer
    from ..models.create_transaction_body_discounts_item import (
        CreateTransactionBodyDiscountsItem,
    )
    from ..models.create_transaction_body_geolocation import (
        CreateTransactionBodyGeolocation,
    )
    from ..models.create_transaction_body_items_item import (
        CreateTransactionBodyItemsItem,
    )
    from ..models.create_transaction_body_metadata import CreateTransactionBodyMetadata
    from ..models.create_transaction_body_payment import CreateTransactionBodyPayment
    from ..models.create_transaction_body_shipping import CreateTransactionBodyShipping
    from ..models.create_transaction_body_splits_item import (
        CreateTransactionBodySplitsItem,
    )


T = TypeVar("T", bound="CreateTransactionBody")


@_attrs_define
class CreateTransactionBody:
    """
    Attributes:
        amount (int):
        payment (CreateTransactionBodyPayment): **Regra:** Com `method=credit`, `card` é **obrigatório** (`card.id` de
            um cartão salvo, ou cartão completo inline: holderName, expirationMonth, expirationYear, numbering,
            securityCode).
        customer (CreateTransactionBodyCustomer): **Regra:** Obrigatório informar `id` (cliente salvo) **OU** os dados
            inline `firstName` + `lastName` + `email` (a API faz find-or-create). Enviar `customer: {}` é rejeitado.
        billing (CreateTransactionBodyBilling | Unset): **Regra:** Obrigatório quando `payment.method=billet` (endereço
            do pagador): `billing.address.id` (salvo) ou endereço inline com postcode + street + number.
        items (list[CreateTransactionBodyItemsItem] | Unset):
        discounts (list[CreateTransactionBodyDiscountsItem] | Unset):
        splits (list[CreateTransactionBodySplitsItem] | Unset):
        on_behalf_of (str | Unset): Public identifier (prefix_value)
        geolocation (CreateTransactionBodyGeolocation | Unset):
        shipping (CreateTransactionBodyShipping | Unset):
        callback (CreateTransactionBodyCallback | Unset):
        description (str | Unset):
        external_reference (str | Unset):
        metadata (CreateTransactionBodyMetadata | Unset):
        source (str | Unset):
    """

    amount: int
    payment: CreateTransactionBodyPayment
    customer: CreateTransactionBodyCustomer
    billing: CreateTransactionBodyBilling | Unset = UNSET
    items: list[CreateTransactionBodyItemsItem] | Unset = UNSET
    discounts: list[CreateTransactionBodyDiscountsItem] | Unset = UNSET
    splits: list[CreateTransactionBodySplitsItem] | Unset = UNSET
    on_behalf_of: str | Unset = UNSET
    geolocation: CreateTransactionBodyGeolocation | Unset = UNSET
    shipping: CreateTransactionBodyShipping | Unset = UNSET
    callback: CreateTransactionBodyCallback | Unset = UNSET
    description: str | Unset = UNSET
    external_reference: str | Unset = UNSET
    metadata: CreateTransactionBodyMetadata | Unset = UNSET
    source: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        amount = self.amount

        payment = self.payment.to_dict()

        customer = self.customer.to_dict()

        billing: dict[str, Any] | Unset = UNSET
        if not isinstance(self.billing, Unset):
            billing = self.billing.to_dict()

        items: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.items, Unset):
            items = []
            for items_item_data in self.items:
                items_item = items_item_data.to_dict()
                items.append(items_item)

        discounts: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.discounts, Unset):
            discounts = []
            for discounts_item_data in self.discounts:
                discounts_item = discounts_item_data.to_dict()
                discounts.append(discounts_item)

        splits: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.splits, Unset):
            splits = []
            for splits_item_data in self.splits:
                splits_item = splits_item_data.to_dict()
                splits.append(splits_item)

        on_behalf_of = self.on_behalf_of

        geolocation: dict[str, Any] | Unset = UNSET
        if not isinstance(self.geolocation, Unset):
            geolocation = self.geolocation.to_dict()

        shipping: dict[str, Any] | Unset = UNSET
        if not isinstance(self.shipping, Unset):
            shipping = self.shipping.to_dict()

        callback: dict[str, Any] | Unset = UNSET
        if not isinstance(self.callback, Unset):
            callback = self.callback.to_dict()

        description = self.description

        external_reference = self.external_reference

        metadata: dict[str, Any] | Unset = UNSET
        if not isinstance(self.metadata, Unset):
            metadata = self.metadata.to_dict()

        source = self.source

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "amount": amount,
                "payment": payment,
                "customer": customer,
            }
        )
        if billing is not UNSET:
            field_dict["billing"] = billing
        if items is not UNSET:
            field_dict["items"] = items
        if discounts is not UNSET:
            field_dict["discounts"] = discounts
        if splits is not UNSET:
            field_dict["splits"] = splits
        if on_behalf_of is not UNSET:
            field_dict["onBehalfOf"] = on_behalf_of
        if geolocation is not UNSET:
            field_dict["geolocation"] = geolocation
        if shipping is not UNSET:
            field_dict["shipping"] = shipping
        if callback is not UNSET:
            field_dict["callback"] = callback
        if description is not UNSET:
            field_dict["description"] = description
        if external_reference is not UNSET:
            field_dict["externalReference"] = external_reference
        if metadata is not UNSET:
            field_dict["metadata"] = metadata
        if source is not UNSET:
            field_dict["source"] = source

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.create_transaction_body_billing import (
            CreateTransactionBodyBilling,
        )
        from ..models.create_transaction_body_callback import (
            CreateTransactionBodyCallback,
        )
        from ..models.create_transaction_body_customer import (
            CreateTransactionBodyCustomer,
        )
        from ..models.create_transaction_body_discounts_item import (
            CreateTransactionBodyDiscountsItem,
        )
        from ..models.create_transaction_body_geolocation import (
            CreateTransactionBodyGeolocation,
        )
        from ..models.create_transaction_body_items_item import (
            CreateTransactionBodyItemsItem,
        )
        from ..models.create_transaction_body_metadata import (
            CreateTransactionBodyMetadata,
        )
        from ..models.create_transaction_body_payment import (
            CreateTransactionBodyPayment,
        )
        from ..models.create_transaction_body_shipping import (
            CreateTransactionBodyShipping,
        )
        from ..models.create_transaction_body_splits_item import (
            CreateTransactionBodySplitsItem,
        )

        d = dict(src_dict)
        amount = d.pop("amount")

        payment = CreateTransactionBodyPayment.from_dict(d.pop("payment"))

        customer = CreateTransactionBodyCustomer.from_dict(d.pop("customer"))

        _billing = d.pop("billing", UNSET)
        billing: CreateTransactionBodyBilling | Unset
        if isinstance(_billing, Unset):
            billing = UNSET
        else:
            billing = CreateTransactionBodyBilling.from_dict(_billing)

        _items = d.pop("items", UNSET)
        items: list[CreateTransactionBodyItemsItem] | Unset = UNSET
        if _items is not UNSET:
            items = []
            for items_item_data in _items:
                items_item = CreateTransactionBodyItemsItem.from_dict(items_item_data)

                items.append(items_item)

        _discounts = d.pop("discounts", UNSET)
        discounts: list[CreateTransactionBodyDiscountsItem] | Unset = UNSET
        if _discounts is not UNSET:
            discounts = []
            for discounts_item_data in _discounts:
                discounts_item = CreateTransactionBodyDiscountsItem.from_dict(
                    discounts_item_data
                )

                discounts.append(discounts_item)

        _splits = d.pop("splits", UNSET)
        splits: list[CreateTransactionBodySplitsItem] | Unset = UNSET
        if _splits is not UNSET:
            splits = []
            for splits_item_data in _splits:
                splits_item = CreateTransactionBodySplitsItem.from_dict(
                    splits_item_data
                )

                splits.append(splits_item)

        on_behalf_of = d.pop("onBehalfOf", UNSET)

        _geolocation = d.pop("geolocation", UNSET)
        geolocation: CreateTransactionBodyGeolocation | Unset
        if isinstance(_geolocation, Unset):
            geolocation = UNSET
        else:
            geolocation = CreateTransactionBodyGeolocation.from_dict(_geolocation)

        _shipping = d.pop("shipping", UNSET)
        shipping: CreateTransactionBodyShipping | Unset
        if isinstance(_shipping, Unset):
            shipping = UNSET
        else:
            shipping = CreateTransactionBodyShipping.from_dict(_shipping)

        _callback = d.pop("callback", UNSET)
        callback: CreateTransactionBodyCallback | Unset
        if isinstance(_callback, Unset):
            callback = UNSET
        else:
            callback = CreateTransactionBodyCallback.from_dict(_callback)

        description = d.pop("description", UNSET)

        external_reference = d.pop("externalReference", UNSET)

        _metadata = d.pop("metadata", UNSET)
        metadata: CreateTransactionBodyMetadata | Unset
        if isinstance(_metadata, Unset):
            metadata = UNSET
        else:
            metadata = CreateTransactionBodyMetadata.from_dict(_metadata)

        source = d.pop("source", UNSET)

        create_transaction_body = cls(
            amount=amount,
            payment=payment,
            customer=customer,
            billing=billing,
            items=items,
            discounts=discounts,
            splits=splits,
            on_behalf_of=on_behalf_of,
            geolocation=geolocation,
            shipping=shipping,
            callback=callback,
            description=description,
            external_reference=external_reference,
            metadata=metadata,
            source=source,
        )

        return create_transaction_body
