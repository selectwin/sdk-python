from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.get_customer_response_200_subscriptions_item_status import (
    GetCustomerResponse200SubscriptionsItemStatus,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_customer_response_200_subscriptions_item_billing import (
        GetCustomerResponse200SubscriptionsItemBilling,
    )
    from ..models.get_customer_response_200_subscriptions_item_callback_type_0 import (
        GetCustomerResponse200SubscriptionsItemCallbackType0,
    )
    from ..models.get_customer_response_200_subscriptions_item_current_cycle_type_0 import (
        GetCustomerResponse200SubscriptionsItemCurrentCycleType0,
    )
    from ..models.get_customer_response_200_subscriptions_item_customer import (
        GetCustomerResponse200SubscriptionsItemCustomer,
    )
    from ..models.get_customer_response_200_subscriptions_item_discount_type_0 import (
        GetCustomerResponse200SubscriptionsItemDiscountType0,
    )
    from ..models.get_customer_response_200_subscriptions_item_geolocation_type_0 import (
        GetCustomerResponse200SubscriptionsItemGeolocationType0,
    )
    from ..models.get_customer_response_200_subscriptions_item_items_item import (
        GetCustomerResponse200SubscriptionsItemItemsItem,
    )
    from ..models.get_customer_response_200_subscriptions_item_links import (
        GetCustomerResponse200SubscriptionsItemLinks,
    )
    from ..models.get_customer_response_200_subscriptions_item_merchant import (
        GetCustomerResponse200SubscriptionsItemMerchant,
    )
    from ..models.get_customer_response_200_subscriptions_item_metadata_type_0 import (
        GetCustomerResponse200SubscriptionsItemMetadataType0,
    )
    from ..models.get_customer_response_200_subscriptions_item_shipping_type_0 import (
        GetCustomerResponse200SubscriptionsItemShippingType0,
    )
    from ..models.get_customer_response_200_subscriptions_item_splits_type_0_item import (
        GetCustomerResponse200SubscriptionsItemSplitsType0Item,
    )


T = TypeVar("T", bound="GetCustomerResponse200SubscriptionsItem")


@_attrs_define
class GetCustomerResponse200SubscriptionsItem:
    """
    Attributes:
        id (str): Public identifier (subs_/sub_…)
        status (GetCustomerResponse200SubscriptionsItemStatus):
        currency (None | str):
        method (None | str):
        type_ (None | str):
        current_cycle (GetCustomerResponse200SubscriptionsItemCurrentCycleType0 | None):
        customer (GetCustomerResponse200SubscriptionsItemCustomer):
        billing (GetCustomerResponse200SubscriptionsItemBilling):
        discount (GetCustomerResponse200SubscriptionsItemDiscountType0 | None):
        discounts (list[Any] | None):
        shippable (bool):
        shipping (GetCustomerResponse200SubscriptionsItemShippingType0 | None):
        spplited (bool):
        splits (list[GetCustomerResponse200SubscriptionsItemSplitsType0Item] | None):
        items (list[GetCustomerResponse200SubscriptionsItemItemsItem]):
        callback (GetCustomerResponse200SubscriptionsItemCallbackType0 | None):
        geolocation (GetCustomerResponse200SubscriptionsItemGeolocationType0 | None):
        external_reference (None | str):
        metadata (GetCustomerResponse200SubscriptionsItemMetadataType0 | None):
        updated_at (str):
        created_at (str):
        merchant (GetCustomerResponse200SubscriptionsItemMerchant | Unset):
        field_links (GetCustomerResponse200SubscriptionsItemLinks | Unset):
    """

    id: str
    status: GetCustomerResponse200SubscriptionsItemStatus
    currency: None | str
    method: None | str
    type_: None | str
    current_cycle: GetCustomerResponse200SubscriptionsItemCurrentCycleType0 | None
    customer: GetCustomerResponse200SubscriptionsItemCustomer
    billing: GetCustomerResponse200SubscriptionsItemBilling
    discount: GetCustomerResponse200SubscriptionsItemDiscountType0 | None
    discounts: list[Any] | None
    shippable: bool
    shipping: GetCustomerResponse200SubscriptionsItemShippingType0 | None
    spplited: bool
    splits: list[GetCustomerResponse200SubscriptionsItemSplitsType0Item] | None
    items: list[GetCustomerResponse200SubscriptionsItemItemsItem]
    callback: GetCustomerResponse200SubscriptionsItemCallbackType0 | None
    geolocation: GetCustomerResponse200SubscriptionsItemGeolocationType0 | None
    external_reference: None | str
    metadata: GetCustomerResponse200SubscriptionsItemMetadataType0 | None
    updated_at: str
    created_at: str
    merchant: GetCustomerResponse200SubscriptionsItemMerchant | Unset = UNSET
    field_links: GetCustomerResponse200SubscriptionsItemLinks | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.get_customer_response_200_subscriptions_item_callback_type_0 import (
            GetCustomerResponse200SubscriptionsItemCallbackType0,
        )
        from ..models.get_customer_response_200_subscriptions_item_current_cycle_type_0 import (
            GetCustomerResponse200SubscriptionsItemCurrentCycleType0,
        )
        from ..models.get_customer_response_200_subscriptions_item_discount_type_0 import (
            GetCustomerResponse200SubscriptionsItemDiscountType0,
        )
        from ..models.get_customer_response_200_subscriptions_item_geolocation_type_0 import (
            GetCustomerResponse200SubscriptionsItemGeolocationType0,
        )
        from ..models.get_customer_response_200_subscriptions_item_metadata_type_0 import (
            GetCustomerResponse200SubscriptionsItemMetadataType0,
        )
        from ..models.get_customer_response_200_subscriptions_item_shipping_type_0 import (
            GetCustomerResponse200SubscriptionsItemShippingType0,
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
            self.current_cycle, GetCustomerResponse200SubscriptionsItemCurrentCycleType0
        ):
            current_cycle = self.current_cycle.to_dict()
        else:
            current_cycle = self.current_cycle

        customer = self.customer.to_dict()

        billing = self.billing.to_dict()

        discount: dict[str, Any] | None
        if isinstance(
            self.discount, GetCustomerResponse200SubscriptionsItemDiscountType0
        ):
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
        if isinstance(
            self.shipping, GetCustomerResponse200SubscriptionsItemShippingType0
        ):
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
        if isinstance(
            self.callback, GetCustomerResponse200SubscriptionsItemCallbackType0
        ):
            callback = self.callback.to_dict()
        else:
            callback = self.callback

        geolocation: dict[str, Any] | None
        if isinstance(
            self.geolocation, GetCustomerResponse200SubscriptionsItemGeolocationType0
        ):
            geolocation = self.geolocation.to_dict()
        else:
            geolocation = self.geolocation

        external_reference: None | str
        external_reference = self.external_reference

        metadata: dict[str, Any] | None
        if isinstance(
            self.metadata, GetCustomerResponse200SubscriptionsItemMetadataType0
        ):
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
        from ..models.get_customer_response_200_subscriptions_item_billing import (
            GetCustomerResponse200SubscriptionsItemBilling,
        )
        from ..models.get_customer_response_200_subscriptions_item_callback_type_0 import (
            GetCustomerResponse200SubscriptionsItemCallbackType0,
        )
        from ..models.get_customer_response_200_subscriptions_item_current_cycle_type_0 import (
            GetCustomerResponse200SubscriptionsItemCurrentCycleType0,
        )
        from ..models.get_customer_response_200_subscriptions_item_customer import (
            GetCustomerResponse200SubscriptionsItemCustomer,
        )
        from ..models.get_customer_response_200_subscriptions_item_discount_type_0 import (
            GetCustomerResponse200SubscriptionsItemDiscountType0,
        )
        from ..models.get_customer_response_200_subscriptions_item_geolocation_type_0 import (
            GetCustomerResponse200SubscriptionsItemGeolocationType0,
        )
        from ..models.get_customer_response_200_subscriptions_item_items_item import (
            GetCustomerResponse200SubscriptionsItemItemsItem,
        )
        from ..models.get_customer_response_200_subscriptions_item_links import (
            GetCustomerResponse200SubscriptionsItemLinks,
        )
        from ..models.get_customer_response_200_subscriptions_item_merchant import (
            GetCustomerResponse200SubscriptionsItemMerchant,
        )
        from ..models.get_customer_response_200_subscriptions_item_metadata_type_0 import (
            GetCustomerResponse200SubscriptionsItemMetadataType0,
        )
        from ..models.get_customer_response_200_subscriptions_item_shipping_type_0 import (
            GetCustomerResponse200SubscriptionsItemShippingType0,
        )
        from ..models.get_customer_response_200_subscriptions_item_splits_type_0_item import (
            GetCustomerResponse200SubscriptionsItemSplitsType0Item,
        )

        d = dict(src_dict)
        id = d.pop("id")

        status = GetCustomerResponse200SubscriptionsItemStatus(d.pop("status"))

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
        ) -> GetCustomerResponse200SubscriptionsItemCurrentCycleType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                current_cycle_type_0 = (
                    GetCustomerResponse200SubscriptionsItemCurrentCycleType0.from_dict(
                        data
                    )
                )

                return current_cycle_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                GetCustomerResponse200SubscriptionsItemCurrentCycleType0 | None, data
            )

        current_cycle = _parse_current_cycle(d.pop("currentCycle"))

        customer = GetCustomerResponse200SubscriptionsItemCustomer.from_dict(
            d.pop("customer")
        )

        billing = GetCustomerResponse200SubscriptionsItemBilling.from_dict(
            d.pop("billing")
        )

        def _parse_discount(
            data: object,
        ) -> GetCustomerResponse200SubscriptionsItemDiscountType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                discount_type_0 = (
                    GetCustomerResponse200SubscriptionsItemDiscountType0.from_dict(data)
                )

                return discount_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                GetCustomerResponse200SubscriptionsItemDiscountType0 | None, data
            )

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
        ) -> GetCustomerResponse200SubscriptionsItemShippingType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                shipping_type_0 = (
                    GetCustomerResponse200SubscriptionsItemShippingType0.from_dict(data)
                )

                return shipping_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                GetCustomerResponse200SubscriptionsItemShippingType0 | None, data
            )

        shipping = _parse_shipping(d.pop("shipping"))

        spplited = d.pop("spplited")

        def _parse_splits(
            data: object,
        ) -> list[GetCustomerResponse200SubscriptionsItemSplitsType0Item] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                splits_type_0 = []
                _splits_type_0 = data
                for splits_type_0_item_data in _splits_type_0:
                    splits_type_0_item = GetCustomerResponse200SubscriptionsItemSplitsType0Item.from_dict(
                        splits_type_0_item_data
                    )

                    splits_type_0.append(splits_type_0_item)

                return splits_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                list[GetCustomerResponse200SubscriptionsItemSplitsType0Item] | None,
                data,
            )

        splits = _parse_splits(d.pop("splits"))

        items = []
        _items = d.pop("items")
        for items_item_data in _items:
            items_item = GetCustomerResponse200SubscriptionsItemItemsItem.from_dict(
                items_item_data
            )

            items.append(items_item)

        def _parse_callback(
            data: object,
        ) -> GetCustomerResponse200SubscriptionsItemCallbackType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                callback_type_0 = (
                    GetCustomerResponse200SubscriptionsItemCallbackType0.from_dict(data)
                )

                return callback_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                GetCustomerResponse200SubscriptionsItemCallbackType0 | None, data
            )

        callback = _parse_callback(d.pop("callback"))

        def _parse_geolocation(
            data: object,
        ) -> GetCustomerResponse200SubscriptionsItemGeolocationType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                geolocation_type_0 = (
                    GetCustomerResponse200SubscriptionsItemGeolocationType0.from_dict(
                        data
                    )
                )

                return geolocation_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                GetCustomerResponse200SubscriptionsItemGeolocationType0 | None, data
            )

        geolocation = _parse_geolocation(d.pop("geolocation"))

        def _parse_external_reference(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        external_reference = _parse_external_reference(d.pop("externalReference"))

        def _parse_metadata(
            data: object,
        ) -> GetCustomerResponse200SubscriptionsItemMetadataType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                metadata_type_0 = (
                    GetCustomerResponse200SubscriptionsItemMetadataType0.from_dict(data)
                )

                return metadata_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                GetCustomerResponse200SubscriptionsItemMetadataType0 | None, data
            )

        metadata = _parse_metadata(d.pop("metadata"))

        updated_at = d.pop("updatedAt")

        created_at = d.pop("createdAt")

        _merchant = d.pop("merchant", UNSET)
        merchant: GetCustomerResponse200SubscriptionsItemMerchant | Unset
        if isinstance(_merchant, Unset):
            merchant = UNSET
        else:
            merchant = GetCustomerResponse200SubscriptionsItemMerchant.from_dict(
                _merchant
            )

        _field_links = d.pop("_links", UNSET)
        field_links: GetCustomerResponse200SubscriptionsItemLinks | Unset
        if isinstance(_field_links, Unset):
            field_links = UNSET
        else:
            field_links = GetCustomerResponse200SubscriptionsItemLinks.from_dict(
                _field_links
            )

        get_customer_response_200_subscriptions_item = cls(
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

        return get_customer_response_200_subscriptions_item
