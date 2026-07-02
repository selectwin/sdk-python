from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.list_subscriptions_response_200_data_item_status import (
    ListSubscriptionsResponse200DataItemStatus,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.list_subscriptions_response_200_data_item_billing import (
        ListSubscriptionsResponse200DataItemBilling,
    )
    from ..models.list_subscriptions_response_200_data_item_callback_type_0 import (
        ListSubscriptionsResponse200DataItemCallbackType0,
    )
    from ..models.list_subscriptions_response_200_data_item_current_cycle_type_0 import (
        ListSubscriptionsResponse200DataItemCurrentCycleType0,
    )
    from ..models.list_subscriptions_response_200_data_item_customer import (
        ListSubscriptionsResponse200DataItemCustomer,
    )
    from ..models.list_subscriptions_response_200_data_item_discount_type_0 import (
        ListSubscriptionsResponse200DataItemDiscountType0,
    )
    from ..models.list_subscriptions_response_200_data_item_geolocation_type_0 import (
        ListSubscriptionsResponse200DataItemGeolocationType0,
    )
    from ..models.list_subscriptions_response_200_data_item_items_item import (
        ListSubscriptionsResponse200DataItemItemsItem,
    )
    from ..models.list_subscriptions_response_200_data_item_links import (
        ListSubscriptionsResponse200DataItemLinks,
    )
    from ..models.list_subscriptions_response_200_data_item_merchant import (
        ListSubscriptionsResponse200DataItemMerchant,
    )
    from ..models.list_subscriptions_response_200_data_item_metadata_type_0 import (
        ListSubscriptionsResponse200DataItemMetadataType0,
    )
    from ..models.list_subscriptions_response_200_data_item_shipping_type_0 import (
        ListSubscriptionsResponse200DataItemShippingType0,
    )
    from ..models.list_subscriptions_response_200_data_item_splits_type_0_item import (
        ListSubscriptionsResponse200DataItemSplitsType0Item,
    )


T = TypeVar("T", bound="ListSubscriptionsResponse200DataItem")


@_attrs_define
class ListSubscriptionsResponse200DataItem:
    """
    Attributes:
        id (str): Public identifier (subs_/sub_…)
        status (ListSubscriptionsResponse200DataItemStatus):
        currency (None | str):
        method (None | str):
        type_ (None | str):
        current_cycle (ListSubscriptionsResponse200DataItemCurrentCycleType0 | None):
        customer (ListSubscriptionsResponse200DataItemCustomer):
        billing (ListSubscriptionsResponse200DataItemBilling):
        discount (ListSubscriptionsResponse200DataItemDiscountType0 | None):
        discounts (list[Any] | None):
        shippable (bool):
        shipping (ListSubscriptionsResponse200DataItemShippingType0 | None):
        spplited (bool):
        splits (list[ListSubscriptionsResponse200DataItemSplitsType0Item] | None):
        items (list[ListSubscriptionsResponse200DataItemItemsItem]):
        callback (ListSubscriptionsResponse200DataItemCallbackType0 | None):
        geolocation (ListSubscriptionsResponse200DataItemGeolocationType0 | None):
        external_reference (None | str):
        metadata (ListSubscriptionsResponse200DataItemMetadataType0 | None):
        updated_at (str):
        created_at (str):
        merchant (ListSubscriptionsResponse200DataItemMerchant | Unset):
        field_links (ListSubscriptionsResponse200DataItemLinks | Unset):
    """

    id: str
    status: ListSubscriptionsResponse200DataItemStatus
    currency: None | str
    method: None | str
    type_: None | str
    current_cycle: ListSubscriptionsResponse200DataItemCurrentCycleType0 | None
    customer: ListSubscriptionsResponse200DataItemCustomer
    billing: ListSubscriptionsResponse200DataItemBilling
    discount: ListSubscriptionsResponse200DataItemDiscountType0 | None
    discounts: list[Any] | None
    shippable: bool
    shipping: ListSubscriptionsResponse200DataItemShippingType0 | None
    spplited: bool
    splits: list[ListSubscriptionsResponse200DataItemSplitsType0Item] | None
    items: list[ListSubscriptionsResponse200DataItemItemsItem]
    callback: ListSubscriptionsResponse200DataItemCallbackType0 | None
    geolocation: ListSubscriptionsResponse200DataItemGeolocationType0 | None
    external_reference: None | str
    metadata: ListSubscriptionsResponse200DataItemMetadataType0 | None
    updated_at: str
    created_at: str
    merchant: ListSubscriptionsResponse200DataItemMerchant | Unset = UNSET
    field_links: ListSubscriptionsResponse200DataItemLinks | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.list_subscriptions_response_200_data_item_callback_type_0 import (
            ListSubscriptionsResponse200DataItemCallbackType0,
        )
        from ..models.list_subscriptions_response_200_data_item_current_cycle_type_0 import (
            ListSubscriptionsResponse200DataItemCurrentCycleType0,
        )
        from ..models.list_subscriptions_response_200_data_item_discount_type_0 import (
            ListSubscriptionsResponse200DataItemDiscountType0,
        )
        from ..models.list_subscriptions_response_200_data_item_geolocation_type_0 import (
            ListSubscriptionsResponse200DataItemGeolocationType0,
        )
        from ..models.list_subscriptions_response_200_data_item_metadata_type_0 import (
            ListSubscriptionsResponse200DataItemMetadataType0,
        )
        from ..models.list_subscriptions_response_200_data_item_shipping_type_0 import (
            ListSubscriptionsResponse200DataItemShippingType0,
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
            self.current_cycle, ListSubscriptionsResponse200DataItemCurrentCycleType0
        ):
            current_cycle = self.current_cycle.to_dict()
        else:
            current_cycle = self.current_cycle

        customer = self.customer.to_dict()

        billing = self.billing.to_dict()

        discount: dict[str, Any] | None
        if isinstance(self.discount, ListSubscriptionsResponse200DataItemDiscountType0):
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
        if isinstance(self.shipping, ListSubscriptionsResponse200DataItemShippingType0):
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
        if isinstance(self.callback, ListSubscriptionsResponse200DataItemCallbackType0):
            callback = self.callback.to_dict()
        else:
            callback = self.callback

        geolocation: dict[str, Any] | None
        if isinstance(
            self.geolocation, ListSubscriptionsResponse200DataItemGeolocationType0
        ):
            geolocation = self.geolocation.to_dict()
        else:
            geolocation = self.geolocation

        external_reference: None | str
        external_reference = self.external_reference

        metadata: dict[str, Any] | None
        if isinstance(self.metadata, ListSubscriptionsResponse200DataItemMetadataType0):
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
        from ..models.list_subscriptions_response_200_data_item_billing import (
            ListSubscriptionsResponse200DataItemBilling,
        )
        from ..models.list_subscriptions_response_200_data_item_callback_type_0 import (
            ListSubscriptionsResponse200DataItemCallbackType0,
        )
        from ..models.list_subscriptions_response_200_data_item_current_cycle_type_0 import (
            ListSubscriptionsResponse200DataItemCurrentCycleType0,
        )
        from ..models.list_subscriptions_response_200_data_item_customer import (
            ListSubscriptionsResponse200DataItemCustomer,
        )
        from ..models.list_subscriptions_response_200_data_item_discount_type_0 import (
            ListSubscriptionsResponse200DataItemDiscountType0,
        )
        from ..models.list_subscriptions_response_200_data_item_geolocation_type_0 import (
            ListSubscriptionsResponse200DataItemGeolocationType0,
        )
        from ..models.list_subscriptions_response_200_data_item_items_item import (
            ListSubscriptionsResponse200DataItemItemsItem,
        )
        from ..models.list_subscriptions_response_200_data_item_links import (
            ListSubscriptionsResponse200DataItemLinks,
        )
        from ..models.list_subscriptions_response_200_data_item_merchant import (
            ListSubscriptionsResponse200DataItemMerchant,
        )
        from ..models.list_subscriptions_response_200_data_item_metadata_type_0 import (
            ListSubscriptionsResponse200DataItemMetadataType0,
        )
        from ..models.list_subscriptions_response_200_data_item_shipping_type_0 import (
            ListSubscriptionsResponse200DataItemShippingType0,
        )
        from ..models.list_subscriptions_response_200_data_item_splits_type_0_item import (
            ListSubscriptionsResponse200DataItemSplitsType0Item,
        )

        d = dict(src_dict)
        id = d.pop("id")

        status = ListSubscriptionsResponse200DataItemStatus(d.pop("status"))

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
        ) -> ListSubscriptionsResponse200DataItemCurrentCycleType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                current_cycle_type_0 = (
                    ListSubscriptionsResponse200DataItemCurrentCycleType0.from_dict(
                        data
                    )
                )

                return current_cycle_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                ListSubscriptionsResponse200DataItemCurrentCycleType0 | None, data
            )

        current_cycle = _parse_current_cycle(d.pop("currentCycle"))

        customer = ListSubscriptionsResponse200DataItemCustomer.from_dict(
            d.pop("customer")
        )

        billing = ListSubscriptionsResponse200DataItemBilling.from_dict(
            d.pop("billing")
        )

        def _parse_discount(
            data: object,
        ) -> ListSubscriptionsResponse200DataItemDiscountType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                discount_type_0 = (
                    ListSubscriptionsResponse200DataItemDiscountType0.from_dict(data)
                )

                return discount_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ListSubscriptionsResponse200DataItemDiscountType0 | None, data)

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
        ) -> ListSubscriptionsResponse200DataItemShippingType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                shipping_type_0 = (
                    ListSubscriptionsResponse200DataItemShippingType0.from_dict(data)
                )

                return shipping_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ListSubscriptionsResponse200DataItemShippingType0 | None, data)

        shipping = _parse_shipping(d.pop("shipping"))

        spplited = d.pop("spplited")

        def _parse_splits(
            data: object,
        ) -> list[ListSubscriptionsResponse200DataItemSplitsType0Item] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                splits_type_0 = []
                _splits_type_0 = data
                for splits_type_0_item_data in _splits_type_0:
                    splits_type_0_item = (
                        ListSubscriptionsResponse200DataItemSplitsType0Item.from_dict(
                            splits_type_0_item_data
                        )
                    )

                    splits_type_0.append(splits_type_0_item)

                return splits_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                list[ListSubscriptionsResponse200DataItemSplitsType0Item] | None, data
            )

        splits = _parse_splits(d.pop("splits"))

        items = []
        _items = d.pop("items")
        for items_item_data in _items:
            items_item = ListSubscriptionsResponse200DataItemItemsItem.from_dict(
                items_item_data
            )

            items.append(items_item)

        def _parse_callback(
            data: object,
        ) -> ListSubscriptionsResponse200DataItemCallbackType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                callback_type_0 = (
                    ListSubscriptionsResponse200DataItemCallbackType0.from_dict(data)
                )

                return callback_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ListSubscriptionsResponse200DataItemCallbackType0 | None, data)

        callback = _parse_callback(d.pop("callback"))

        def _parse_geolocation(
            data: object,
        ) -> ListSubscriptionsResponse200DataItemGeolocationType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                geolocation_type_0 = (
                    ListSubscriptionsResponse200DataItemGeolocationType0.from_dict(data)
                )

                return geolocation_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                ListSubscriptionsResponse200DataItemGeolocationType0 | None, data
            )

        geolocation = _parse_geolocation(d.pop("geolocation"))

        def _parse_external_reference(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        external_reference = _parse_external_reference(d.pop("externalReference"))

        def _parse_metadata(
            data: object,
        ) -> ListSubscriptionsResponse200DataItemMetadataType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                metadata_type_0 = (
                    ListSubscriptionsResponse200DataItemMetadataType0.from_dict(data)
                )

                return metadata_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ListSubscriptionsResponse200DataItemMetadataType0 | None, data)

        metadata = _parse_metadata(d.pop("metadata"))

        updated_at = d.pop("updatedAt")

        created_at = d.pop("createdAt")

        _merchant = d.pop("merchant", UNSET)
        merchant: ListSubscriptionsResponse200DataItemMerchant | Unset
        if isinstance(_merchant, Unset):
            merchant = UNSET
        else:
            merchant = ListSubscriptionsResponse200DataItemMerchant.from_dict(_merchant)

        _field_links = d.pop("_links", UNSET)
        field_links: ListSubscriptionsResponse200DataItemLinks | Unset
        if isinstance(_field_links, Unset):
            field_links = UNSET
        else:
            field_links = ListSubscriptionsResponse200DataItemLinks.from_dict(
                _field_links
            )

        list_subscriptions_response_200_data_item = cls(
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

        return list_subscriptions_response_200_data_item
