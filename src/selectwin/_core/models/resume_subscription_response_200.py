from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.resume_subscription_response_200_status import (
    ResumeSubscriptionResponse200Status,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.resume_subscription_response_200_billing import (
        ResumeSubscriptionResponse200Billing,
    )
    from ..models.resume_subscription_response_200_callback_type_0 import (
        ResumeSubscriptionResponse200CallbackType0,
    )
    from ..models.resume_subscription_response_200_current_cycle_type_0 import (
        ResumeSubscriptionResponse200CurrentCycleType0,
    )
    from ..models.resume_subscription_response_200_customer import (
        ResumeSubscriptionResponse200Customer,
    )
    from ..models.resume_subscription_response_200_discount_type_0 import (
        ResumeSubscriptionResponse200DiscountType0,
    )
    from ..models.resume_subscription_response_200_geolocation_type_0 import (
        ResumeSubscriptionResponse200GeolocationType0,
    )
    from ..models.resume_subscription_response_200_items_item import (
        ResumeSubscriptionResponse200ItemsItem,
    )
    from ..models.resume_subscription_response_200_links import (
        ResumeSubscriptionResponse200Links,
    )
    from ..models.resume_subscription_response_200_merchant import (
        ResumeSubscriptionResponse200Merchant,
    )
    from ..models.resume_subscription_response_200_metadata_type_0 import (
        ResumeSubscriptionResponse200MetadataType0,
    )
    from ..models.resume_subscription_response_200_shipping_type_0 import (
        ResumeSubscriptionResponse200ShippingType0,
    )
    from ..models.resume_subscription_response_200_splits_type_0_item import (
        ResumeSubscriptionResponse200SplitsType0Item,
    )


T = TypeVar("T", bound="ResumeSubscriptionResponse200")


@_attrs_define
class ResumeSubscriptionResponse200:
    """
    Attributes:
        id (str): Public identifier (subs_/sub_…)
        status (ResumeSubscriptionResponse200Status):
        currency (None | str):
        method (None | str):
        type_ (None | str):
        current_cycle (None | ResumeSubscriptionResponse200CurrentCycleType0):
        customer (ResumeSubscriptionResponse200Customer):
        billing (ResumeSubscriptionResponse200Billing):
        discount (None | ResumeSubscriptionResponse200DiscountType0):
        discounts (list[Any] | None):
        shippable (bool):
        shipping (None | ResumeSubscriptionResponse200ShippingType0):
        spplited (bool):
        splits (list[ResumeSubscriptionResponse200SplitsType0Item] | None):
        items (list[ResumeSubscriptionResponse200ItemsItem]):
        callback (None | ResumeSubscriptionResponse200CallbackType0):
        geolocation (None | ResumeSubscriptionResponse200GeolocationType0):
        external_reference (None | str):
        metadata (None | ResumeSubscriptionResponse200MetadataType0):
        updated_at (str):
        created_at (str):
        merchant (ResumeSubscriptionResponse200Merchant | Unset):
        field_links (ResumeSubscriptionResponse200Links | Unset):
    """

    id: str
    status: ResumeSubscriptionResponse200Status
    currency: None | str
    method: None | str
    type_: None | str
    current_cycle: None | ResumeSubscriptionResponse200CurrentCycleType0
    customer: ResumeSubscriptionResponse200Customer
    billing: ResumeSubscriptionResponse200Billing
    discount: None | ResumeSubscriptionResponse200DiscountType0
    discounts: list[Any] | None
    shippable: bool
    shipping: None | ResumeSubscriptionResponse200ShippingType0
    spplited: bool
    splits: list[ResumeSubscriptionResponse200SplitsType0Item] | None
    items: list[ResumeSubscriptionResponse200ItemsItem]
    callback: None | ResumeSubscriptionResponse200CallbackType0
    geolocation: None | ResumeSubscriptionResponse200GeolocationType0
    external_reference: None | str
    metadata: None | ResumeSubscriptionResponse200MetadataType0
    updated_at: str
    created_at: str
    merchant: ResumeSubscriptionResponse200Merchant | Unset = UNSET
    field_links: ResumeSubscriptionResponse200Links | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.resume_subscription_response_200_callback_type_0 import (
            ResumeSubscriptionResponse200CallbackType0,
        )
        from ..models.resume_subscription_response_200_current_cycle_type_0 import (
            ResumeSubscriptionResponse200CurrentCycleType0,
        )
        from ..models.resume_subscription_response_200_discount_type_0 import (
            ResumeSubscriptionResponse200DiscountType0,
        )
        from ..models.resume_subscription_response_200_geolocation_type_0 import (
            ResumeSubscriptionResponse200GeolocationType0,
        )
        from ..models.resume_subscription_response_200_metadata_type_0 import (
            ResumeSubscriptionResponse200MetadataType0,
        )
        from ..models.resume_subscription_response_200_shipping_type_0 import (
            ResumeSubscriptionResponse200ShippingType0,
        )

        id = self.id

        status = self.status.value

        currency: None | str
        currency = self.currency

        method: None | str
        method = self.method

        type_: None | str
        type_ = self.type_

        current_cycle: dict[str, Any] | None
        if isinstance(
            self.current_cycle, ResumeSubscriptionResponse200CurrentCycleType0
        ):
            current_cycle = self.current_cycle.to_dict()
        else:
            current_cycle = self.current_cycle

        customer = self.customer.to_dict()

        billing = self.billing.to_dict()

        discount: dict[str, Any] | None
        if isinstance(self.discount, ResumeSubscriptionResponse200DiscountType0):
            discount = self.discount.to_dict()
        else:
            discount = self.discount

        discounts: list[Any] | None
        if isinstance(self.discounts, list):
            discounts = self.discounts

        else:
            discounts = self.discounts

        shippable = self.shippable

        shipping: dict[str, Any] | None
        if isinstance(self.shipping, ResumeSubscriptionResponse200ShippingType0):
            shipping = self.shipping.to_dict()
        else:
            shipping = self.shipping

        spplited = self.spplited

        splits: list[dict[str, Any]] | None
        if isinstance(self.splits, list):
            splits = []
            for splits_type_0_item_data in self.splits:
                splits_type_0_item = splits_type_0_item_data.to_dict()
                splits.append(splits_type_0_item)

        else:
            splits = self.splits

        items = []
        for items_item_data in self.items:
            items_item = items_item_data.to_dict()
            items.append(items_item)

        callback: dict[str, Any] | None
        if isinstance(self.callback, ResumeSubscriptionResponse200CallbackType0):
            callback = self.callback.to_dict()
        else:
            callback = self.callback

        geolocation: dict[str, Any] | None
        if isinstance(self.geolocation, ResumeSubscriptionResponse200GeolocationType0):
            geolocation = self.geolocation.to_dict()
        else:
            geolocation = self.geolocation

        external_reference: None | str
        external_reference = self.external_reference

        metadata: dict[str, Any] | None
        if isinstance(self.metadata, ResumeSubscriptionResponse200MetadataType0):
            metadata = self.metadata.to_dict()
        else:
            metadata = self.metadata

        updated_at = self.updated_at

        created_at = self.created_at

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
                "status": status,
                "currency": currency,
                "method": method,
                "type": type_,
                "currentCycle": current_cycle,
                "customer": customer,
                "billing": billing,
                "discount": discount,
                "discounts": discounts,
                "shippable": shippable,
                "shipping": shipping,
                "spplited": spplited,
                "splits": splits,
                "items": items,
                "callback": callback,
                "geolocation": geolocation,
                "externalReference": external_reference,
                "metadata": metadata,
                "updatedAt": updated_at,
                "createdAt": created_at,
            }
        )
        if merchant is not UNSET:
            field_dict["merchant"] = merchant
        if field_links is not UNSET:
            field_dict["_links"] = field_links

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.resume_subscription_response_200_billing import (
            ResumeSubscriptionResponse200Billing,
        )
        from ..models.resume_subscription_response_200_callback_type_0 import (
            ResumeSubscriptionResponse200CallbackType0,
        )
        from ..models.resume_subscription_response_200_current_cycle_type_0 import (
            ResumeSubscriptionResponse200CurrentCycleType0,
        )
        from ..models.resume_subscription_response_200_customer import (
            ResumeSubscriptionResponse200Customer,
        )
        from ..models.resume_subscription_response_200_discount_type_0 import (
            ResumeSubscriptionResponse200DiscountType0,
        )
        from ..models.resume_subscription_response_200_geolocation_type_0 import (
            ResumeSubscriptionResponse200GeolocationType0,
        )
        from ..models.resume_subscription_response_200_items_item import (
            ResumeSubscriptionResponse200ItemsItem,
        )
        from ..models.resume_subscription_response_200_links import (
            ResumeSubscriptionResponse200Links,
        )
        from ..models.resume_subscription_response_200_merchant import (
            ResumeSubscriptionResponse200Merchant,
        )
        from ..models.resume_subscription_response_200_metadata_type_0 import (
            ResumeSubscriptionResponse200MetadataType0,
        )
        from ..models.resume_subscription_response_200_shipping_type_0 import (
            ResumeSubscriptionResponse200ShippingType0,
        )
        from ..models.resume_subscription_response_200_splits_type_0_item import (
            ResumeSubscriptionResponse200SplitsType0Item,
        )

        d = dict(src_dict)
        id = d.pop("id")

        status = ResumeSubscriptionResponse200Status(d.pop("status"))

        def _parse_currency(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        currency = _parse_currency(d.pop("currency"))

        def _parse_method(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        method = _parse_method(d.pop("method"))

        def _parse_type_(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        type_ = _parse_type_(d.pop("type"))

        def _parse_current_cycle(
            data: object,
        ) -> None | ResumeSubscriptionResponse200CurrentCycleType0:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                current_cycle_type_0 = (
                    ResumeSubscriptionResponse200CurrentCycleType0.from_dict(data)
                )

                return current_cycle_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | ResumeSubscriptionResponse200CurrentCycleType0, data)

        current_cycle = _parse_current_cycle(d.pop("currentCycle"))

        customer = ResumeSubscriptionResponse200Customer.from_dict(d.pop("customer"))

        billing = ResumeSubscriptionResponse200Billing.from_dict(d.pop("billing"))

        def _parse_discount(
            data: object,
        ) -> None | ResumeSubscriptionResponse200DiscountType0:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                discount_type_0 = ResumeSubscriptionResponse200DiscountType0.from_dict(
                    data
                )

                return discount_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | ResumeSubscriptionResponse200DiscountType0, data)

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

        shippable = d.pop("shippable")

        def _parse_shipping(
            data: object,
        ) -> None | ResumeSubscriptionResponse200ShippingType0:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                shipping_type_0 = ResumeSubscriptionResponse200ShippingType0.from_dict(
                    data
                )

                return shipping_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | ResumeSubscriptionResponse200ShippingType0, data)

        shipping = _parse_shipping(d.pop("shipping"))

        spplited = d.pop("spplited")

        def _parse_splits(
            data: object,
        ) -> list[ResumeSubscriptionResponse200SplitsType0Item] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                splits_type_0 = []
                _splits_type_0 = data
                for splits_type_0_item_data in _splits_type_0:
                    splits_type_0_item = (
                        ResumeSubscriptionResponse200SplitsType0Item.from_dict(
                            splits_type_0_item_data
                        )
                    )

                    splits_type_0.append(splits_type_0_item)

                return splits_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[ResumeSubscriptionResponse200SplitsType0Item] | None, data)

        splits = _parse_splits(d.pop("splits"))

        items = []
        _items = d.pop("items")
        for items_item_data in _items:
            items_item = ResumeSubscriptionResponse200ItemsItem.from_dict(
                items_item_data
            )

            items.append(items_item)

        def _parse_callback(
            data: object,
        ) -> None | ResumeSubscriptionResponse200CallbackType0:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                callback_type_0 = ResumeSubscriptionResponse200CallbackType0.from_dict(
                    data
                )

                return callback_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | ResumeSubscriptionResponse200CallbackType0, data)

        callback = _parse_callback(d.pop("callback"))

        def _parse_geolocation(
            data: object,
        ) -> None | ResumeSubscriptionResponse200GeolocationType0:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                geolocation_type_0 = (
                    ResumeSubscriptionResponse200GeolocationType0.from_dict(data)
                )

                return geolocation_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | ResumeSubscriptionResponse200GeolocationType0, data)

        geolocation = _parse_geolocation(d.pop("geolocation"))

        def _parse_external_reference(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        external_reference = _parse_external_reference(d.pop("externalReference"))

        def _parse_metadata(
            data: object,
        ) -> None | ResumeSubscriptionResponse200MetadataType0:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                metadata_type_0 = ResumeSubscriptionResponse200MetadataType0.from_dict(
                    data
                )

                return metadata_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | ResumeSubscriptionResponse200MetadataType0, data)

        metadata = _parse_metadata(d.pop("metadata"))

        updated_at = d.pop("updatedAt")

        created_at = d.pop("createdAt")

        _merchant = d.pop("merchant", UNSET)
        merchant: ResumeSubscriptionResponse200Merchant | Unset
        if isinstance(_merchant, Unset):
            merchant = UNSET
        else:
            merchant = ResumeSubscriptionResponse200Merchant.from_dict(_merchant)

        _field_links = d.pop("_links", UNSET)
        field_links: ResumeSubscriptionResponse200Links | Unset
        if isinstance(_field_links, Unset):
            field_links = UNSET
        else:
            field_links = ResumeSubscriptionResponse200Links.from_dict(_field_links)

        resume_subscription_response_200 = cls(
            id=id,
            status=status,
            currency=currency,
            method=method,
            type_=type_,
            current_cycle=current_cycle,
            customer=customer,
            billing=billing,
            discount=discount,
            discounts=discounts,
            shippable=shippable,
            shipping=shipping,
            spplited=spplited,
            splits=splits,
            items=items,
            callback=callback,
            geolocation=geolocation,
            external_reference=external_reference,
            metadata=metadata,
            updated_at=updated_at,
            created_at=created_at,
            merchant=merchant,
            field_links=field_links,
        )

        return resume_subscription_response_200
