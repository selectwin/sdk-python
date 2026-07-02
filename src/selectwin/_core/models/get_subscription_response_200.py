from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.get_subscription_response_200_status import (
    GetSubscriptionResponse200Status,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_subscription_response_200_billing import (
        GetSubscriptionResponse200Billing,
    )
    from ..models.get_subscription_response_200_callback_type_0 import (
        GetSubscriptionResponse200CallbackType0,
    )
    from ..models.get_subscription_response_200_current_cycle_type_0 import (
        GetSubscriptionResponse200CurrentCycleType0,
    )
    from ..models.get_subscription_response_200_customer import (
        GetSubscriptionResponse200Customer,
    )
    from ..models.get_subscription_response_200_discount_type_0 import (
        GetSubscriptionResponse200DiscountType0,
    )
    from ..models.get_subscription_response_200_geolocation_type_0 import (
        GetSubscriptionResponse200GeolocationType0,
    )
    from ..models.get_subscription_response_200_items_item import (
        GetSubscriptionResponse200ItemsItem,
    )
    from ..models.get_subscription_response_200_links import (
        GetSubscriptionResponse200Links,
    )
    from ..models.get_subscription_response_200_merchant import (
        GetSubscriptionResponse200Merchant,
    )
    from ..models.get_subscription_response_200_metadata_type_0 import (
        GetSubscriptionResponse200MetadataType0,
    )
    from ..models.get_subscription_response_200_shipping_type_0 import (
        GetSubscriptionResponse200ShippingType0,
    )
    from ..models.get_subscription_response_200_splits_type_0_item import (
        GetSubscriptionResponse200SplitsType0Item,
    )


T = TypeVar("T", bound="GetSubscriptionResponse200")


@_attrs_define
class GetSubscriptionResponse200:
    """
    Attributes:
        id (str): Public identifier (subs_/sub_…)
        status (GetSubscriptionResponse200Status):
        currency (None | str):
        method (None | str):
        type_ (None | str):
        current_cycle (GetSubscriptionResponse200CurrentCycleType0 | None):
        customer (GetSubscriptionResponse200Customer):
        billing (GetSubscriptionResponse200Billing):
        discount (GetSubscriptionResponse200DiscountType0 | None):
        discounts (list[Any] | None):
        shippable (bool):
        shipping (GetSubscriptionResponse200ShippingType0 | None):
        spplited (bool):
        splits (list[GetSubscriptionResponse200SplitsType0Item] | None):
        items (list[GetSubscriptionResponse200ItemsItem]):
        callback (GetSubscriptionResponse200CallbackType0 | None):
        geolocation (GetSubscriptionResponse200GeolocationType0 | None):
        external_reference (None | str):
        metadata (GetSubscriptionResponse200MetadataType0 | None):
        updated_at (str):
        created_at (str):
        merchant (GetSubscriptionResponse200Merchant | Unset):
        field_links (GetSubscriptionResponse200Links | Unset):
    """

    id: str
    status: GetSubscriptionResponse200Status
    currency: None | str
    method: None | str
    type_: None | str
    current_cycle: GetSubscriptionResponse200CurrentCycleType0 | None
    customer: GetSubscriptionResponse200Customer
    billing: GetSubscriptionResponse200Billing
    discount: GetSubscriptionResponse200DiscountType0 | None
    discounts: list[Any] | None
    shippable: bool
    shipping: GetSubscriptionResponse200ShippingType0 | None
    spplited: bool
    splits: list[GetSubscriptionResponse200SplitsType0Item] | None
    items: list[GetSubscriptionResponse200ItemsItem]
    callback: GetSubscriptionResponse200CallbackType0 | None
    geolocation: GetSubscriptionResponse200GeolocationType0 | None
    external_reference: None | str
    metadata: GetSubscriptionResponse200MetadataType0 | None
    updated_at: str
    created_at: str
    merchant: GetSubscriptionResponse200Merchant | Unset = UNSET
    field_links: GetSubscriptionResponse200Links | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.get_subscription_response_200_callback_type_0 import (
            GetSubscriptionResponse200CallbackType0,
        )
        from ..models.get_subscription_response_200_current_cycle_type_0 import (
            GetSubscriptionResponse200CurrentCycleType0,
        )
        from ..models.get_subscription_response_200_discount_type_0 import (
            GetSubscriptionResponse200DiscountType0,
        )
        from ..models.get_subscription_response_200_geolocation_type_0 import (
            GetSubscriptionResponse200GeolocationType0,
        )
        from ..models.get_subscription_response_200_metadata_type_0 import (
            GetSubscriptionResponse200MetadataType0,
        )
        from ..models.get_subscription_response_200_shipping_type_0 import (
            GetSubscriptionResponse200ShippingType0,
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
        if isinstance(self.current_cycle, GetSubscriptionResponse200CurrentCycleType0):
            current_cycle = self.current_cycle.to_dict()
        else:
            current_cycle = self.current_cycle

        customer = self.customer.to_dict()

        billing = self.billing.to_dict()

        discount: dict[str, Any] | None
        if isinstance(self.discount, GetSubscriptionResponse200DiscountType0):
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
        if isinstance(self.shipping, GetSubscriptionResponse200ShippingType0):
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
        if isinstance(self.callback, GetSubscriptionResponse200CallbackType0):
            callback = self.callback.to_dict()
        else:
            callback = self.callback

        geolocation: dict[str, Any] | None
        if isinstance(self.geolocation, GetSubscriptionResponse200GeolocationType0):
            geolocation = self.geolocation.to_dict()
        else:
            geolocation = self.geolocation

        external_reference: None | str
        external_reference = self.external_reference

        metadata: dict[str, Any] | None
        if isinstance(self.metadata, GetSubscriptionResponse200MetadataType0):
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
        from ..models.get_subscription_response_200_billing import (
            GetSubscriptionResponse200Billing,
        )
        from ..models.get_subscription_response_200_callback_type_0 import (
            GetSubscriptionResponse200CallbackType0,
        )
        from ..models.get_subscription_response_200_current_cycle_type_0 import (
            GetSubscriptionResponse200CurrentCycleType0,
        )
        from ..models.get_subscription_response_200_customer import (
            GetSubscriptionResponse200Customer,
        )
        from ..models.get_subscription_response_200_discount_type_0 import (
            GetSubscriptionResponse200DiscountType0,
        )
        from ..models.get_subscription_response_200_geolocation_type_0 import (
            GetSubscriptionResponse200GeolocationType0,
        )
        from ..models.get_subscription_response_200_items_item import (
            GetSubscriptionResponse200ItemsItem,
        )
        from ..models.get_subscription_response_200_links import (
            GetSubscriptionResponse200Links,
        )
        from ..models.get_subscription_response_200_merchant import (
            GetSubscriptionResponse200Merchant,
        )
        from ..models.get_subscription_response_200_metadata_type_0 import (
            GetSubscriptionResponse200MetadataType0,
        )
        from ..models.get_subscription_response_200_shipping_type_0 import (
            GetSubscriptionResponse200ShippingType0,
        )
        from ..models.get_subscription_response_200_splits_type_0_item import (
            GetSubscriptionResponse200SplitsType0Item,
        )

        d = dict(src_dict)
        id = d.pop("id")

        status = GetSubscriptionResponse200Status(d.pop("status"))

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
        ) -> GetSubscriptionResponse200CurrentCycleType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                current_cycle_type_0 = (
                    GetSubscriptionResponse200CurrentCycleType0.from_dict(data)
                )

                return current_cycle_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(GetSubscriptionResponse200CurrentCycleType0 | None, data)

        current_cycle = _parse_current_cycle(d.pop("currentCycle"))

        customer = GetSubscriptionResponse200Customer.from_dict(d.pop("customer"))

        billing = GetSubscriptionResponse200Billing.from_dict(d.pop("billing"))

        def _parse_discount(
            data: object,
        ) -> GetSubscriptionResponse200DiscountType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                discount_type_0 = GetSubscriptionResponse200DiscountType0.from_dict(
                    data
                )

                return discount_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(GetSubscriptionResponse200DiscountType0 | None, data)

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
        ) -> GetSubscriptionResponse200ShippingType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                shipping_type_0 = GetSubscriptionResponse200ShippingType0.from_dict(
                    data
                )

                return shipping_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(GetSubscriptionResponse200ShippingType0 | None, data)

        shipping = _parse_shipping(d.pop("shipping"))

        spplited = d.pop("spplited")

        def _parse_splits(
            data: object,
        ) -> list[GetSubscriptionResponse200SplitsType0Item] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                splits_type_0 = []
                _splits_type_0 = data
                for splits_type_0_item_data in _splits_type_0:
                    splits_type_0_item = (
                        GetSubscriptionResponse200SplitsType0Item.from_dict(
                            splits_type_0_item_data
                        )
                    )

                    splits_type_0.append(splits_type_0_item)

                return splits_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[GetSubscriptionResponse200SplitsType0Item] | None, data)

        splits = _parse_splits(d.pop("splits"))

        items = []
        _items = d.pop("items")
        for items_item_data in _items:
            items_item = GetSubscriptionResponse200ItemsItem.from_dict(items_item_data)

            items.append(items_item)

        def _parse_callback(
            data: object,
        ) -> GetSubscriptionResponse200CallbackType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                callback_type_0 = GetSubscriptionResponse200CallbackType0.from_dict(
                    data
                )

                return callback_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(GetSubscriptionResponse200CallbackType0 | None, data)

        callback = _parse_callback(d.pop("callback"))

        def _parse_geolocation(
            data: object,
        ) -> GetSubscriptionResponse200GeolocationType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                geolocation_type_0 = (
                    GetSubscriptionResponse200GeolocationType0.from_dict(data)
                )

                return geolocation_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(GetSubscriptionResponse200GeolocationType0 | None, data)

        geolocation = _parse_geolocation(d.pop("geolocation"))

        def _parse_external_reference(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        external_reference = _parse_external_reference(d.pop("externalReference"))

        def _parse_metadata(
            data: object,
        ) -> GetSubscriptionResponse200MetadataType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                metadata_type_0 = GetSubscriptionResponse200MetadataType0.from_dict(
                    data
                )

                return metadata_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(GetSubscriptionResponse200MetadataType0 | None, data)

        metadata = _parse_metadata(d.pop("metadata"))

        updated_at = d.pop("updatedAt")

        created_at = d.pop("createdAt")

        _merchant = d.pop("merchant", UNSET)
        merchant: GetSubscriptionResponse200Merchant | Unset
        if isinstance(_merchant, Unset):
            merchant = UNSET
        else:
            merchant = GetSubscriptionResponse200Merchant.from_dict(_merchant)

        _field_links = d.pop("_links", UNSET)
        field_links: GetSubscriptionResponse200Links | Unset
        if isinstance(_field_links, Unset):
            field_links = UNSET
        else:
            field_links = GetSubscriptionResponse200Links.from_dict(_field_links)

        get_subscription_response_200 = cls(
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

        return get_subscription_response_200
