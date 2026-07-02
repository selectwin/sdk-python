from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.submit_transaction_dispute_response_200_method import (
    SubmitTransactionDisputeResponse200Method,
)
from ..models.submit_transaction_dispute_response_200_status import (
    SubmitTransactionDisputeResponse200Status,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.submit_transaction_dispute_response_200_billing import (
        SubmitTransactionDisputeResponse200Billing,
    )
    from ..models.submit_transaction_dispute_response_200_callback_type_0 import (
        SubmitTransactionDisputeResponse200CallbackType0,
    )
    from ..models.submit_transaction_dispute_response_200_customer_type_0 import (
        SubmitTransactionDisputeResponse200CustomerType0,
    )
    from ..models.submit_transaction_dispute_response_200_discount_type_0 import (
        SubmitTransactionDisputeResponse200DiscountType0,
    )
    from ..models.submit_transaction_dispute_response_200_disputes_type_0_item import (
        SubmitTransactionDisputeResponse200DisputesType0Item,
    )
    from ..models.submit_transaction_dispute_response_200_items_type_0_item import (
        SubmitTransactionDisputeResponse200ItemsType0Item,
    )
    from ..models.submit_transaction_dispute_response_200_links import (
        SubmitTransactionDisputeResponse200Links,
    )
    from ..models.submit_transaction_dispute_response_200_merchant import (
        SubmitTransactionDisputeResponse200Merchant,
    )
    from ..models.submit_transaction_dispute_response_200_payment import (
        SubmitTransactionDisputeResponse200Payment,
    )
    from ..models.submit_transaction_dispute_response_200_receivables_type_0_item import (
        SubmitTransactionDisputeResponse200ReceivablesType0Item,
    )
    from ..models.submit_transaction_dispute_response_200_refunds_type_0_item import (
        SubmitTransactionDisputeResponse200RefundsType0Item,
    )
    from ..models.submit_transaction_dispute_response_200_splits_type_0_item import (
        SubmitTransactionDisputeResponse200SplitsType0Item,
    )
    from ..models.submit_transaction_dispute_response_200_timeline_item import (
        SubmitTransactionDisputeResponse200TimelineItem,
    )


T = TypeVar("T", bound="SubmitTransactionDisputeResponse200")


@_attrs_define
class SubmitTransactionDisputeResponse200:
    """
    Attributes:
        id (str): Public identifier (tra_/trx_…)
        custom_id (None | str):
        amount (int):
        original_amount (int):
        fees (int):
        net (int):
        status (SubmitTransactionDisputeResponse200Status):
        method (SubmitTransactionDisputeResponse200Method):
        currency (str):
        payment (SubmitTransactionDisputeResponse200Payment):
        discount (None | SubmitTransactionDisputeResponse200DiscountType0):
        discounts (list[Any] | None):
        customer (None | SubmitTransactionDisputeResponse200CustomerType0):
        billing (SubmitTransactionDisputeResponse200Billing):
        external_reference (None | str):
        shippable (bool):
        spplited (bool):
        items (list[SubmitTransactionDisputeResponse200ItemsType0Item] | None):
        receivables (list[SubmitTransactionDisputeResponse200ReceivablesType0Item] | None):
        splits (list[SubmitTransactionDisputeResponse200SplitsType0Item] | None):
        refunds (list[SubmitTransactionDisputeResponse200RefundsType0Item] | None):
        disputes (list[SubmitTransactionDisputeResponse200DisputesType0Item] | None):
        timeline (list[SubmitTransactionDisputeResponse200TimelineItem]):
        callback (None | SubmitTransactionDisputeResponse200CallbackType0):
        processing_time_ms (int | None):
        updated_at (str):
        created_at (str):
        shipping (Any | Unset):
        metadata (Any | Unset):
        merchant (SubmitTransactionDisputeResponse200Merchant | Unset):
        field_links (SubmitTransactionDisputeResponse200Links | Unset):
    """

    id: str
    custom_id: None | str
    amount: int
    original_amount: int
    fees: int
    net: int
    status: SubmitTransactionDisputeResponse200Status
    method: SubmitTransactionDisputeResponse200Method
    currency: str
    payment: SubmitTransactionDisputeResponse200Payment
    discount: None | SubmitTransactionDisputeResponse200DiscountType0
    discounts: list[Any] | None
    customer: None | SubmitTransactionDisputeResponse200CustomerType0
    billing: SubmitTransactionDisputeResponse200Billing
    external_reference: None | str
    shippable: bool
    spplited: bool
    items: list[SubmitTransactionDisputeResponse200ItemsType0Item] | None
    receivables: list[SubmitTransactionDisputeResponse200ReceivablesType0Item] | None
    splits: list[SubmitTransactionDisputeResponse200SplitsType0Item] | None
    refunds: list[SubmitTransactionDisputeResponse200RefundsType0Item] | None
    disputes: list[SubmitTransactionDisputeResponse200DisputesType0Item] | None
    timeline: list[SubmitTransactionDisputeResponse200TimelineItem]
    callback: None | SubmitTransactionDisputeResponse200CallbackType0
    processing_time_ms: int | None
    updated_at: str
    created_at: str
    shipping: Any | Unset = UNSET
    metadata: Any | Unset = UNSET
    merchant: SubmitTransactionDisputeResponse200Merchant | Unset = UNSET
    field_links: SubmitTransactionDisputeResponse200Links | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.submit_transaction_dispute_response_200_callback_type_0 import (
            SubmitTransactionDisputeResponse200CallbackType0,
        )
        from ..models.submit_transaction_dispute_response_200_customer_type_0 import (
            SubmitTransactionDisputeResponse200CustomerType0,
        )
        from ..models.submit_transaction_dispute_response_200_discount_type_0 import (
            SubmitTransactionDisputeResponse200DiscountType0,
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
        if isinstance(self.discount, SubmitTransactionDisputeResponse200DiscountType0):
            discount = self.discount.to_dict()
        else:
            discount = self.discount

        discounts: list[Any] | None
        if isinstance(self.discounts, list):
            discounts = self.discounts

        else:
            discounts = self.discounts

        customer: dict[str, Any] | None
        if isinstance(self.customer, SubmitTransactionDisputeResponse200CustomerType0):
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
        if isinstance(self.callback, SubmitTransactionDisputeResponse200CallbackType0):
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
        from ..models.submit_transaction_dispute_response_200_billing import (
            SubmitTransactionDisputeResponse200Billing,
        )
        from ..models.submit_transaction_dispute_response_200_callback_type_0 import (
            SubmitTransactionDisputeResponse200CallbackType0,
        )
        from ..models.submit_transaction_dispute_response_200_customer_type_0 import (
            SubmitTransactionDisputeResponse200CustomerType0,
        )
        from ..models.submit_transaction_dispute_response_200_discount_type_0 import (
            SubmitTransactionDisputeResponse200DiscountType0,
        )
        from ..models.submit_transaction_dispute_response_200_disputes_type_0_item import (
            SubmitTransactionDisputeResponse200DisputesType0Item,
        )
        from ..models.submit_transaction_dispute_response_200_items_type_0_item import (
            SubmitTransactionDisputeResponse200ItemsType0Item,
        )
        from ..models.submit_transaction_dispute_response_200_links import (
            SubmitTransactionDisputeResponse200Links,
        )
        from ..models.submit_transaction_dispute_response_200_merchant import (
            SubmitTransactionDisputeResponse200Merchant,
        )
        from ..models.submit_transaction_dispute_response_200_payment import (
            SubmitTransactionDisputeResponse200Payment,
        )
        from ..models.submit_transaction_dispute_response_200_receivables_type_0_item import (
            SubmitTransactionDisputeResponse200ReceivablesType0Item,
        )
        from ..models.submit_transaction_dispute_response_200_refunds_type_0_item import (
            SubmitTransactionDisputeResponse200RefundsType0Item,
        )
        from ..models.submit_transaction_dispute_response_200_splits_type_0_item import (
            SubmitTransactionDisputeResponse200SplitsType0Item,
        )
        from ..models.submit_transaction_dispute_response_200_timeline_item import (
            SubmitTransactionDisputeResponse200TimelineItem,
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

        status = SubmitTransactionDisputeResponse200Status(d.pop("status"))

        method = SubmitTransactionDisputeResponse200Method(d.pop("method"))

        currency = d.pop("currency")

        payment = SubmitTransactionDisputeResponse200Payment.from_dict(d.pop("payment"))

        def _parse_discount(
            data: object,
        ) -> None | SubmitTransactionDisputeResponse200DiscountType0:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                discount_type_0 = (
                    SubmitTransactionDisputeResponse200DiscountType0.from_dict(data)
                )

                return discount_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | SubmitTransactionDisputeResponse200DiscountType0, data)

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
        ) -> None | SubmitTransactionDisputeResponse200CustomerType0:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                customer_type_0 = (
                    SubmitTransactionDisputeResponse200CustomerType0.from_dict(data)
                )

                return customer_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | SubmitTransactionDisputeResponse200CustomerType0, data)

        customer = _parse_customer(d.pop("customer"))

        billing = SubmitTransactionDisputeResponse200Billing.from_dict(d.pop("billing"))

        def _parse_external_reference(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        external_reference = _parse_external_reference(d.pop("externalReference"))

        shippable = d.pop("shippable")

        spplited = d.pop("spplited")

        def _parse_items(
            data: object,
        ) -> list[SubmitTransactionDisputeResponse200ItemsType0Item] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                items_type_0 = []
                _items_type_0 = data
                for items_type_0_item_data in _items_type_0:
                    items_type_0_item = (
                        SubmitTransactionDisputeResponse200ItemsType0Item.from_dict(
                            items_type_0_item_data
                        )
                    )

                    items_type_0.append(items_type_0_item)

                return items_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                list[SubmitTransactionDisputeResponse200ItemsType0Item] | None, data
            )

        items = _parse_items(d.pop("items"))

        def _parse_receivables(
            data: object,
        ) -> list[SubmitTransactionDisputeResponse200ReceivablesType0Item] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                receivables_type_0 = []
                _receivables_type_0 = data
                for receivables_type_0_item_data in _receivables_type_0:
                    receivables_type_0_item = SubmitTransactionDisputeResponse200ReceivablesType0Item.from_dict(
                        receivables_type_0_item_data
                    )

                    receivables_type_0.append(receivables_type_0_item)

                return receivables_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                list[SubmitTransactionDisputeResponse200ReceivablesType0Item] | None,
                data,
            )

        receivables = _parse_receivables(d.pop("receivables"))

        def _parse_splits(
            data: object,
        ) -> list[SubmitTransactionDisputeResponse200SplitsType0Item] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                splits_type_0 = []
                _splits_type_0 = data
                for splits_type_0_item_data in _splits_type_0:
                    splits_type_0_item = (
                        SubmitTransactionDisputeResponse200SplitsType0Item.from_dict(
                            splits_type_0_item_data
                        )
                    )

                    splits_type_0.append(splits_type_0_item)

                return splits_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                list[SubmitTransactionDisputeResponse200SplitsType0Item] | None, data
            )

        splits = _parse_splits(d.pop("splits"))

        def _parse_refunds(
            data: object,
        ) -> list[SubmitTransactionDisputeResponse200RefundsType0Item] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                refunds_type_0 = []
                _refunds_type_0 = data
                for refunds_type_0_item_data in _refunds_type_0:
                    refunds_type_0_item = (
                        SubmitTransactionDisputeResponse200RefundsType0Item.from_dict(
                            refunds_type_0_item_data
                        )
                    )

                    refunds_type_0.append(refunds_type_0_item)

                return refunds_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                list[SubmitTransactionDisputeResponse200RefundsType0Item] | None, data
            )

        refunds = _parse_refunds(d.pop("refunds"))

        def _parse_disputes(
            data: object,
        ) -> list[SubmitTransactionDisputeResponse200DisputesType0Item] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                disputes_type_0 = []
                _disputes_type_0 = data
                for disputes_type_0_item_data in _disputes_type_0:
                    disputes_type_0_item = (
                        SubmitTransactionDisputeResponse200DisputesType0Item.from_dict(
                            disputes_type_0_item_data
                        )
                    )

                    disputes_type_0.append(disputes_type_0_item)

                return disputes_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                list[SubmitTransactionDisputeResponse200DisputesType0Item] | None, data
            )

        disputes = _parse_disputes(d.pop("disputes"))

        timeline = []
        _timeline = d.pop("timeline")
        for timeline_item_data in _timeline:
            timeline_item = SubmitTransactionDisputeResponse200TimelineItem.from_dict(
                timeline_item_data
            )

            timeline.append(timeline_item)

        def _parse_callback(
            data: object,
        ) -> None | SubmitTransactionDisputeResponse200CallbackType0:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                callback_type_0 = (
                    SubmitTransactionDisputeResponse200CallbackType0.from_dict(data)
                )

                return callback_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | SubmitTransactionDisputeResponse200CallbackType0, data)

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
        merchant: SubmitTransactionDisputeResponse200Merchant | Unset
        if isinstance(_merchant, Unset):
            merchant = UNSET
        else:
            merchant = SubmitTransactionDisputeResponse200Merchant.from_dict(_merchant)

        _field_links = d.pop("_links", UNSET)
        field_links: SubmitTransactionDisputeResponse200Links | Unset
        if isinstance(_field_links, Unset):
            field_links = UNSET
        else:
            field_links = SubmitTransactionDisputeResponse200Links.from_dict(
                _field_links
            )

        submit_transaction_dispute_response_200 = cls(
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

        return submit_transaction_dispute_response_200
