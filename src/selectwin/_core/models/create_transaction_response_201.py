from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.create_transaction_response_201_method import (
    CreateTransactionResponse201Method,
)
from ..models.create_transaction_response_201_status import (
    CreateTransactionResponse201Status,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.create_transaction_response_201_billing import (
        CreateTransactionResponse201Billing,
    )
    from ..models.create_transaction_response_201_callback_type_0 import (
        CreateTransactionResponse201CallbackType0,
    )
    from ..models.create_transaction_response_201_customer_type_0 import (
        CreateTransactionResponse201CustomerType0,
    )
    from ..models.create_transaction_response_201_discount_type_0 import (
        CreateTransactionResponse201DiscountType0,
    )
    from ..models.create_transaction_response_201_disputes_type_0_item import (
        CreateTransactionResponse201DisputesType0Item,
    )
    from ..models.create_transaction_response_201_items_type_0_item import (
        CreateTransactionResponse201ItemsType0Item,
    )
    from ..models.create_transaction_response_201_links import (
        CreateTransactionResponse201Links,
    )
    from ..models.create_transaction_response_201_merchant import (
        CreateTransactionResponse201Merchant,
    )
    from ..models.create_transaction_response_201_payment import (
        CreateTransactionResponse201Payment,
    )
    from ..models.create_transaction_response_201_receivables_type_0_item import (
        CreateTransactionResponse201ReceivablesType0Item,
    )
    from ..models.create_transaction_response_201_refunds_type_0_item import (
        CreateTransactionResponse201RefundsType0Item,
    )
    from ..models.create_transaction_response_201_splits_type_0_item import (
        CreateTransactionResponse201SplitsType0Item,
    )
    from ..models.create_transaction_response_201_timeline_item import (
        CreateTransactionResponse201TimelineItem,
    )


T = TypeVar("T", bound="CreateTransactionResponse201")


@_attrs_define
class CreateTransactionResponse201:
    """
    Attributes:
        id (str): Public identifier (tra_/trx_…)
        custom_id (None | str):
        amount (int):
        original_amount (int):
        fees (int):
        net (int):
        status (CreateTransactionResponse201Status):
        method (CreateTransactionResponse201Method):
        currency (str):
        payment (CreateTransactionResponse201Payment):
        discount (CreateTransactionResponse201DiscountType0 | None):
        discounts (list[Any] | None):
        customer (CreateTransactionResponse201CustomerType0 | None):
        billing (CreateTransactionResponse201Billing):
        external_reference (None | str):
        shippable (bool):
        spplited (bool):
        items (list[CreateTransactionResponse201ItemsType0Item] | None):
        receivables (list[CreateTransactionResponse201ReceivablesType0Item] | None):
        splits (list[CreateTransactionResponse201SplitsType0Item] | None):
        refunds (list[CreateTransactionResponse201RefundsType0Item] | None):
        disputes (list[CreateTransactionResponse201DisputesType0Item] | None):
        timeline (list[CreateTransactionResponse201TimelineItem]):
        callback (CreateTransactionResponse201CallbackType0 | None):
        processing_time_ms (int | None):
        updated_at (str):
        created_at (str):
        shipping (Any | Unset):
        metadata (Any | Unset):
        merchant (CreateTransactionResponse201Merchant | Unset):
        field_links (CreateTransactionResponse201Links | Unset):
    """

    id: str
    custom_id: None | str
    amount: int
    original_amount: int
    fees: int
    net: int
    status: CreateTransactionResponse201Status
    method: CreateTransactionResponse201Method
    currency: str
    payment: CreateTransactionResponse201Payment
    discount: CreateTransactionResponse201DiscountType0 | None
    discounts: list[Any] | None
    customer: CreateTransactionResponse201CustomerType0 | None
    billing: CreateTransactionResponse201Billing
    external_reference: None | str
    shippable: bool
    spplited: bool
    items: list[CreateTransactionResponse201ItemsType0Item] | None
    receivables: list[CreateTransactionResponse201ReceivablesType0Item] | None
    splits: list[CreateTransactionResponse201SplitsType0Item] | None
    refunds: list[CreateTransactionResponse201RefundsType0Item] | None
    disputes: list[CreateTransactionResponse201DisputesType0Item] | None
    timeline: list[CreateTransactionResponse201TimelineItem]
    callback: CreateTransactionResponse201CallbackType0 | None
    processing_time_ms: int | None
    updated_at: str
    created_at: str
    shipping: Any | Unset = UNSET
    metadata: Any | Unset = UNSET
    merchant: CreateTransactionResponse201Merchant | Unset = UNSET
    field_links: CreateTransactionResponse201Links | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.create_transaction_response_201_callback_type_0 import (
            CreateTransactionResponse201CallbackType0,
        )
        from ..models.create_transaction_response_201_customer_type_0 import (
            CreateTransactionResponse201CustomerType0,
        )
        from ..models.create_transaction_response_201_discount_type_0 import (
            CreateTransactionResponse201DiscountType0,
        )

        id = self.id

        custom_id: None | str
        custom_id = self.custom_id

        amount = self.amount

        original_amount = self.original_amount

        fees = self.fees

        net = self.net

        status = self.status.value

        method = self.method.value

        currency = self.currency

        payment = self.payment.to_dict()

        discount: dict[str, Any] | None
        if isinstance(self.discount, CreateTransactionResponse201DiscountType0):
            discount = self.discount.to_dict()
        else:
            discount = self.discount

        discounts: list[Any] | None
        if isinstance(self.discounts, list):
            discounts = self.discounts

        else:
            discounts = self.discounts

        customer: dict[str, Any] | None
        if isinstance(self.customer, CreateTransactionResponse201CustomerType0):
            customer = self.customer.to_dict()
        else:
            customer = self.customer

        billing = self.billing.to_dict()

        external_reference: None | str
        external_reference = self.external_reference

        shippable = self.shippable

        spplited = self.spplited

        items: list[dict[str, Any]] | None
        if isinstance(self.items, list):
            items = []
            for items_type_0_item_data in self.items:
                items_type_0_item = items_type_0_item_data.to_dict()
                items.append(items_type_0_item)

        else:
            items = self.items

        receivables: list[dict[str, Any]] | None
        if isinstance(self.receivables, list):
            receivables = []
            for receivables_type_0_item_data in self.receivables:
                receivables_type_0_item = receivables_type_0_item_data.to_dict()
                receivables.append(receivables_type_0_item)

        else:
            receivables = self.receivables

        splits: list[dict[str, Any]] | None
        if isinstance(self.splits, list):
            splits = []
            for splits_type_0_item_data in self.splits:
                splits_type_0_item = splits_type_0_item_data.to_dict()
                splits.append(splits_type_0_item)

        else:
            splits = self.splits

        refunds: list[dict[str, Any]] | None
        if isinstance(self.refunds, list):
            refunds = []
            for refunds_type_0_item_data in self.refunds:
                refunds_type_0_item = refunds_type_0_item_data.to_dict()
                refunds.append(refunds_type_0_item)

        else:
            refunds = self.refunds

        disputes: list[dict[str, Any]] | None
        if isinstance(self.disputes, list):
            disputes = []
            for disputes_type_0_item_data in self.disputes:
                disputes_type_0_item = disputes_type_0_item_data.to_dict()
                disputes.append(disputes_type_0_item)

        else:
            disputes = self.disputes

        timeline = []
        for timeline_item_data in self.timeline:
            timeline_item = timeline_item_data.to_dict()
            timeline.append(timeline_item)

        callback: dict[str, Any] | None
        if isinstance(self.callback, CreateTransactionResponse201CallbackType0):
            callback = self.callback.to_dict()
        else:
            callback = self.callback

        processing_time_ms: int | None
        processing_time_ms = self.processing_time_ms

        updated_at = self.updated_at

        created_at = self.created_at

        shipping = self.shipping

        metadata = self.metadata

        merchant: dict[str, Any] | Unset = UNSET
        if not isinstance(self.merchant, Unset):
            merchant = self.merchant.to_dict()

        field_links: dict[str, Any] | Unset = UNSET
        if not isinstance(self.field_links, Unset):
            field_links = self.field_links.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "id": id,
                "customId": custom_id,
                "amount": amount,
                "originalAmount": original_amount,
                "fees": fees,
                "net": net,
                "status": status,
                "method": method,
                "currency": currency,
                "payment": payment,
                "discount": discount,
                "discounts": discounts,
                "customer": customer,
                "billing": billing,
                "externalReference": external_reference,
                "shippable": shippable,
                "spplited": spplited,
                "items": items,
                "receivables": receivables,
                "splits": splits,
                "refunds": refunds,
                "disputes": disputes,
                "timeline": timeline,
                "callback": callback,
                "processingTimeMs": processing_time_ms,
                "updatedAt": updated_at,
                "createdAt": created_at,
            }
        )
        if shipping is not UNSET:
            field_dict["shipping"] = shipping
        if metadata is not UNSET:
            field_dict["metadata"] = metadata
        if merchant is not UNSET:
            field_dict["merchant"] = merchant
        if field_links is not UNSET:
            field_dict["_links"] = field_links

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.create_transaction_response_201_billing import (
            CreateTransactionResponse201Billing,
        )
        from ..models.create_transaction_response_201_callback_type_0 import (
            CreateTransactionResponse201CallbackType0,
        )
        from ..models.create_transaction_response_201_customer_type_0 import (
            CreateTransactionResponse201CustomerType0,
        )
        from ..models.create_transaction_response_201_discount_type_0 import (
            CreateTransactionResponse201DiscountType0,
        )
        from ..models.create_transaction_response_201_disputes_type_0_item import (
            CreateTransactionResponse201DisputesType0Item,
        )
        from ..models.create_transaction_response_201_items_type_0_item import (
            CreateTransactionResponse201ItemsType0Item,
        )
        from ..models.create_transaction_response_201_links import (
            CreateTransactionResponse201Links,
        )
        from ..models.create_transaction_response_201_merchant import (
            CreateTransactionResponse201Merchant,
        )
        from ..models.create_transaction_response_201_payment import (
            CreateTransactionResponse201Payment,
        )
        from ..models.create_transaction_response_201_receivables_type_0_item import (
            CreateTransactionResponse201ReceivablesType0Item,
        )
        from ..models.create_transaction_response_201_refunds_type_0_item import (
            CreateTransactionResponse201RefundsType0Item,
        )
        from ..models.create_transaction_response_201_splits_type_0_item import (
            CreateTransactionResponse201SplitsType0Item,
        )
        from ..models.create_transaction_response_201_timeline_item import (
            CreateTransactionResponse201TimelineItem,
        )

        d = dict(src_dict)
        id = d.pop("id")

        def _parse_custom_id(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        custom_id = _parse_custom_id(d.pop("customId"))

        amount = d.pop("amount")

        original_amount = d.pop("originalAmount")

        fees = d.pop("fees")

        net = d.pop("net")

        status = CreateTransactionResponse201Status(d.pop("status"))

        method = CreateTransactionResponse201Method(d.pop("method"))

        currency = d.pop("currency")

        payment = CreateTransactionResponse201Payment.from_dict(d.pop("payment"))

        def _parse_discount(
            data: object,
        ) -> CreateTransactionResponse201DiscountType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                discount_type_0 = CreateTransactionResponse201DiscountType0.from_dict(
                    data
                )

                return discount_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(CreateTransactionResponse201DiscountType0 | None, data)

        discount = _parse_discount(d.pop("discount"))

        def _parse_discounts(data: object) -> list[Any] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                discounts_type_0 = cast(list[Any], data)

                return discounts_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[Any] | None, data)

        discounts = _parse_discounts(d.pop("discounts"))

        def _parse_customer(
            data: object,
        ) -> CreateTransactionResponse201CustomerType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                customer_type_0 = CreateTransactionResponse201CustomerType0.from_dict(
                    data
                )

                return customer_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(CreateTransactionResponse201CustomerType0 | None, data)

        customer = _parse_customer(d.pop("customer"))

        billing = CreateTransactionResponse201Billing.from_dict(d.pop("billing"))

        def _parse_external_reference(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        external_reference = _parse_external_reference(d.pop("externalReference"))

        shippable = d.pop("shippable")

        spplited = d.pop("spplited")

        def _parse_items(
            data: object,
        ) -> list[CreateTransactionResponse201ItemsType0Item] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                items_type_0 = []
                _items_type_0 = data
                for items_type_0_item_data in _items_type_0:
                    items_type_0_item = (
                        CreateTransactionResponse201ItemsType0Item.from_dict(
                            items_type_0_item_data
                        )
                    )

                    items_type_0.append(items_type_0_item)

                return items_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[CreateTransactionResponse201ItemsType0Item] | None, data)

        items = _parse_items(d.pop("items"))

        def _parse_receivables(
            data: object,
        ) -> list[CreateTransactionResponse201ReceivablesType0Item] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                receivables_type_0 = []
                _receivables_type_0 = data
                for receivables_type_0_item_data in _receivables_type_0:
                    receivables_type_0_item = (
                        CreateTransactionResponse201ReceivablesType0Item.from_dict(
                            receivables_type_0_item_data
                        )
                    )

                    receivables_type_0.append(receivables_type_0_item)

                return receivables_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                list[CreateTransactionResponse201ReceivablesType0Item] | None, data
            )

        receivables = _parse_receivables(d.pop("receivables"))

        def _parse_splits(
            data: object,
        ) -> list[CreateTransactionResponse201SplitsType0Item] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                splits_type_0 = []
                _splits_type_0 = data
                for splits_type_0_item_data in _splits_type_0:
                    splits_type_0_item = (
                        CreateTransactionResponse201SplitsType0Item.from_dict(
                            splits_type_0_item_data
                        )
                    )

                    splits_type_0.append(splits_type_0_item)

                return splits_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[CreateTransactionResponse201SplitsType0Item] | None, data)

        splits = _parse_splits(d.pop("splits"))

        def _parse_refunds(
            data: object,
        ) -> list[CreateTransactionResponse201RefundsType0Item] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                refunds_type_0 = []
                _refunds_type_0 = data
                for refunds_type_0_item_data in _refunds_type_0:
                    refunds_type_0_item = (
                        CreateTransactionResponse201RefundsType0Item.from_dict(
                            refunds_type_0_item_data
                        )
                    )

                    refunds_type_0.append(refunds_type_0_item)

                return refunds_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[CreateTransactionResponse201RefundsType0Item] | None, data)

        refunds = _parse_refunds(d.pop("refunds"))

        def _parse_disputes(
            data: object,
        ) -> list[CreateTransactionResponse201DisputesType0Item] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                disputes_type_0 = []
                _disputes_type_0 = data
                for disputes_type_0_item_data in _disputes_type_0:
                    disputes_type_0_item = (
                        CreateTransactionResponse201DisputesType0Item.from_dict(
                            disputes_type_0_item_data
                        )
                    )

                    disputes_type_0.append(disputes_type_0_item)

                return disputes_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                list[CreateTransactionResponse201DisputesType0Item] | None, data
            )

        disputes = _parse_disputes(d.pop("disputes"))

        timeline = []
        _timeline = d.pop("timeline")
        for timeline_item_data in _timeline:
            timeline_item = CreateTransactionResponse201TimelineItem.from_dict(
                timeline_item_data
            )

            timeline.append(timeline_item)

        def _parse_callback(
            data: object,
        ) -> CreateTransactionResponse201CallbackType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                callback_type_0 = CreateTransactionResponse201CallbackType0.from_dict(
                    data
                )

                return callback_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(CreateTransactionResponse201CallbackType0 | None, data)

        callback = _parse_callback(d.pop("callback"))

        def _parse_processing_time_ms(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        processing_time_ms = _parse_processing_time_ms(d.pop("processingTimeMs"))

        updated_at = d.pop("updatedAt")

        created_at = d.pop("createdAt")

        shipping = d.pop("shipping", UNSET)

        metadata = d.pop("metadata", UNSET)

        _merchant = d.pop("merchant", UNSET)
        merchant: CreateTransactionResponse201Merchant | Unset
        if isinstance(_merchant, Unset):
            merchant = UNSET
        else:
            merchant = CreateTransactionResponse201Merchant.from_dict(_merchant)

        _field_links = d.pop("_links", UNSET)
        field_links: CreateTransactionResponse201Links | Unset
        if isinstance(_field_links, Unset):
            field_links = UNSET
        else:
            field_links = CreateTransactionResponse201Links.from_dict(_field_links)

        create_transaction_response_201 = cls(
            id=id,
            custom_id=custom_id,
            amount=amount,
            original_amount=original_amount,
            fees=fees,
            net=net,
            status=status,
            method=method,
            currency=currency,
            payment=payment,
            discount=discount,
            discounts=discounts,
            customer=customer,
            billing=billing,
            external_reference=external_reference,
            shippable=shippable,
            spplited=spplited,
            items=items,
            receivables=receivables,
            splits=splits,
            refunds=refunds,
            disputes=disputes,
            timeline=timeline,
            callback=callback,
            processing_time_ms=processing_time_ms,
            updated_at=updated_at,
            created_at=created_at,
            shipping=shipping,
            metadata=metadata,
            merchant=merchant,
            field_links=field_links,
        )

        return create_transaction_response_201
