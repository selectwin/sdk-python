from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..models.create_subscription_body_frequency import CreateSubscriptionBodyFrequency
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.create_subscription_body_billing import CreateSubscriptionBodyBilling
    from ..models.create_subscription_body_callback import (
        CreateSubscriptionBodyCallback,
    )
    from ..models.create_subscription_body_customer import (
        CreateSubscriptionBodyCustomer,
    )
    from ..models.create_subscription_body_discounts_item import (
        CreateSubscriptionBodyDiscountsItem,
    )
    from ..models.create_subscription_body_free_trial import (
        CreateSubscriptionBodyFreeTrial,
    )
    from ..models.create_subscription_body_geolocation import (
        CreateSubscriptionBodyGeolocation,
    )
    from ..models.create_subscription_body_items_item import (
        CreateSubscriptionBodyItemsItem,
    )
    from ..models.create_subscription_body_metadata import (
        CreateSubscriptionBodyMetadata,
    )
    from ..models.create_subscription_body_payment import CreateSubscriptionBodyPayment
    from ..models.create_subscription_body_shipping import (
        CreateSubscriptionBodyShipping,
    )
    from ..models.create_subscription_body_splits_item import (
        CreateSubscriptionBodySplitsItem,
    )


T = TypeVar("T", bound="CreateSubscriptionBody")


@_attrs_define
class CreateSubscriptionBody:
    """
    Attributes:
        customer (CreateSubscriptionBodyCustomer):
        items (list[CreateSubscriptionBodyItemsItem]):
        payment (CreateSubscriptionBodyPayment):
        name (str | Unset):
        description (str | Unset):
        billing (CreateSubscriptionBodyBilling | Unset):
        frequency (CreateSubscriptionBodyFrequency | Unset):  Default: CreateSubscriptionBodyFrequency.MONTHLY.
        frequency_count (int | Unset):  Default: 1.
        exact_day (int | Unset):
        free_trial (CreateSubscriptionBodyFreeTrial | Unset):
        start_date (str | Unset):
        end_date (str | Unset):
        auto_renew (bool | Unset):
        external_reference (str | Unset):
        metadata (CreateSubscriptionBodyMetadata | Unset):
        discounts (list[CreateSubscriptionBodyDiscountsItem] | Unset):
        splits (list[CreateSubscriptionBodySplitsItem] | Unset):
        shipping (CreateSubscriptionBodyShipping | Unset):
        callback (CreateSubscriptionBodyCallback | Unset):
        geolocation (CreateSubscriptionBodyGeolocation | Unset):
        session_id (str | Unset):
        integration_id (str | Unset):
        on_behalf_of (str | Unset): Public identifier (prefix_value)
    """

    customer: CreateSubscriptionBodyCustomer
    items: list[CreateSubscriptionBodyItemsItem]
    payment: CreateSubscriptionBodyPayment
    name: str | Unset = UNSET
    description: str | Unset = UNSET
    billing: CreateSubscriptionBodyBilling | Unset = UNSET
    frequency: CreateSubscriptionBodyFrequency | Unset = (
        CreateSubscriptionBodyFrequency.MONTHLY
    )
    frequency_count: int | Unset = 1
    exact_day: int | Unset = UNSET
    free_trial: CreateSubscriptionBodyFreeTrial | Unset = UNSET
    start_date: str | Unset = UNSET
    end_date: str | Unset = UNSET
    auto_renew: bool | Unset = UNSET
    external_reference: str | Unset = UNSET
    metadata: CreateSubscriptionBodyMetadata | Unset = UNSET
    discounts: list[CreateSubscriptionBodyDiscountsItem] | Unset = UNSET
    splits: list[CreateSubscriptionBodySplitsItem] | Unset = UNSET
    shipping: CreateSubscriptionBodyShipping | Unset = UNSET
    callback: CreateSubscriptionBodyCallback | Unset = UNSET
    geolocation: CreateSubscriptionBodyGeolocation | Unset = UNSET
    session_id: str | Unset = UNSET
    integration_id: str | Unset = UNSET
    on_behalf_of: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        customer = self.customer.to_dict()

        items = []
        for items_item_data in self.items:
            items_item = items_item_data.to_dict()
            items.append(items_item)

        payment = self.payment.to_dict()

        name = self.name

        description = self.description

        billing: dict[str, Any] | Unset = UNSET
        if not isinstance(self.billing, Unset):
            billing = self.billing.to_dict()

        frequency: str | Unset = UNSET
        if not isinstance(self.frequency, Unset):
            frequency = self.frequency.value

        frequency_count = self.frequency_count

        exact_day = self.exact_day

        free_trial: dict[str, Any] | Unset = UNSET
        if not isinstance(self.free_trial, Unset):
            free_trial = self.free_trial.to_dict()

        start_date = self.start_date

        end_date = self.end_date

        auto_renew = self.auto_renew

        external_reference = self.external_reference

        metadata: dict[str, Any] | Unset = UNSET
        if not isinstance(self.metadata, Unset):
            metadata = self.metadata.to_dict()

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

        shipping: dict[str, Any] | Unset = UNSET
        if not isinstance(self.shipping, Unset):
            shipping = self.shipping.to_dict()

        callback: dict[str, Any] | Unset = UNSET
        if not isinstance(self.callback, Unset):
            callback = self.callback.to_dict()

        geolocation: dict[str, Any] | Unset = UNSET
        if not isinstance(self.geolocation, Unset):
            geolocation = self.geolocation.to_dict()

        session_id = self.session_id

        integration_id = self.integration_id

        on_behalf_of = self.on_behalf_of

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "customer": customer,
                "items": items,
                "payment": payment,
            }
        )
        if name is not UNSET:
            field_dict["name"] = name
        if description is not UNSET:
            field_dict["description"] = description
        if billing is not UNSET:
            field_dict["billing"] = billing
        if frequency is not UNSET:
            field_dict["frequency"] = frequency
        if frequency_count is not UNSET:
            field_dict["frequencyCount"] = frequency_count
        if exact_day is not UNSET:
            field_dict["exactDay"] = exact_day
        if free_trial is not UNSET:
            field_dict["freeTrial"] = free_trial
        if start_date is not UNSET:
            field_dict["startDate"] = start_date
        if end_date is not UNSET:
            field_dict["endDate"] = end_date
        if auto_renew is not UNSET:
            field_dict["autoRenew"] = auto_renew
        if external_reference is not UNSET:
            field_dict["externalReference"] = external_reference
        if metadata is not UNSET:
            field_dict["metadata"] = metadata
        if discounts is not UNSET:
            field_dict["discounts"] = discounts
        if splits is not UNSET:
            field_dict["splits"] = splits
        if shipping is not UNSET:
            field_dict["shipping"] = shipping
        if callback is not UNSET:
            field_dict["callback"] = callback
        if geolocation is not UNSET:
            field_dict["geolocation"] = geolocation
        if session_id is not UNSET:
            field_dict["sessionId"] = session_id
        if integration_id is not UNSET:
            field_dict["integrationId"] = integration_id
        if on_behalf_of is not UNSET:
            field_dict["onBehalfOf"] = on_behalf_of

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.create_subscription_body_billing import (
            CreateSubscriptionBodyBilling,
        )
        from ..models.create_subscription_body_callback import (
            CreateSubscriptionBodyCallback,
        )
        from ..models.create_subscription_body_customer import (
            CreateSubscriptionBodyCustomer,
        )
        from ..models.create_subscription_body_discounts_item import (
            CreateSubscriptionBodyDiscountsItem,
        )
        from ..models.create_subscription_body_free_trial import (
            CreateSubscriptionBodyFreeTrial,
        )
        from ..models.create_subscription_body_geolocation import (
            CreateSubscriptionBodyGeolocation,
        )
        from ..models.create_subscription_body_items_item import (
            CreateSubscriptionBodyItemsItem,
        )
        from ..models.create_subscription_body_metadata import (
            CreateSubscriptionBodyMetadata,
        )
        from ..models.create_subscription_body_payment import (
            CreateSubscriptionBodyPayment,
        )
        from ..models.create_subscription_body_shipping import (
            CreateSubscriptionBodyShipping,
        )
        from ..models.create_subscription_body_splits_item import (
            CreateSubscriptionBodySplitsItem,
        )

        d = dict(src_dict)
        customer = CreateSubscriptionBodyCustomer.from_dict(d.pop("customer"))

        items = []
        _items = d.pop("items")
        for items_item_data in _items:
            items_item = CreateSubscriptionBodyItemsItem.from_dict(items_item_data)

            items.append(items_item)

        payment = CreateSubscriptionBodyPayment.from_dict(d.pop("payment"))

        name = d.pop("name", UNSET)

        description = d.pop("description", UNSET)

        _billing = d.pop("billing", UNSET)
        billing: CreateSubscriptionBodyBilling | Unset
        if isinstance(_billing, Unset):
            billing = UNSET
        else:
            billing = CreateSubscriptionBodyBilling.from_dict(_billing)

        _frequency = d.pop("frequency", UNSET)
        frequency: CreateSubscriptionBodyFrequency | Unset
        if isinstance(_frequency, Unset):
            frequency = UNSET
        else:
            frequency = CreateSubscriptionBodyFrequency(_frequency)

        frequency_count = d.pop("frequencyCount", UNSET)

        exact_day = d.pop("exactDay", UNSET)

        _free_trial = d.pop("freeTrial", UNSET)
        free_trial: CreateSubscriptionBodyFreeTrial | Unset
        if isinstance(_free_trial, Unset):
            free_trial = UNSET
        else:
            free_trial = CreateSubscriptionBodyFreeTrial.from_dict(_free_trial)

        start_date = d.pop("startDate", UNSET)

        end_date = d.pop("endDate", UNSET)

        auto_renew = d.pop("autoRenew", UNSET)

        external_reference = d.pop("externalReference", UNSET)

        _metadata = d.pop("metadata", UNSET)
        metadata: CreateSubscriptionBodyMetadata | Unset
        if isinstance(_metadata, Unset):
            metadata = UNSET
        else:
            metadata = CreateSubscriptionBodyMetadata.from_dict(_metadata)

        _discounts = d.pop("discounts", UNSET)
        discounts: list[CreateSubscriptionBodyDiscountsItem] | Unset = UNSET
        if _discounts is not UNSET:
            discounts = []
            for discounts_item_data in _discounts:
                discounts_item = CreateSubscriptionBodyDiscountsItem.from_dict(
                    discounts_item_data
                )

                discounts.append(discounts_item)

        _splits = d.pop("splits", UNSET)
        splits: list[CreateSubscriptionBodySplitsItem] | Unset = UNSET
        if _splits is not UNSET:
            splits = []
            for splits_item_data in _splits:
                splits_item = CreateSubscriptionBodySplitsItem.from_dict(
                    splits_item_data
                )

                splits.append(splits_item)

        _shipping = d.pop("shipping", UNSET)
        shipping: CreateSubscriptionBodyShipping | Unset
        if isinstance(_shipping, Unset):
            shipping = UNSET
        else:
            shipping = CreateSubscriptionBodyShipping.from_dict(_shipping)

        _callback = d.pop("callback", UNSET)
        callback: CreateSubscriptionBodyCallback | Unset
        if isinstance(_callback, Unset):
            callback = UNSET
        else:
            callback = CreateSubscriptionBodyCallback.from_dict(_callback)

        _geolocation = d.pop("geolocation", UNSET)
        geolocation: CreateSubscriptionBodyGeolocation | Unset
        if isinstance(_geolocation, Unset):
            geolocation = UNSET
        else:
            geolocation = CreateSubscriptionBodyGeolocation.from_dict(_geolocation)

        session_id = d.pop("sessionId", UNSET)

        integration_id = d.pop("integrationId", UNSET)

        on_behalf_of = d.pop("onBehalfOf", UNSET)

        create_subscription_body = cls(
            customer=customer,
            items=items,
            payment=payment,
            name=name,
            description=description,
            billing=billing,
            frequency=frequency,
            frequency_count=frequency_count,
            exact_day=exact_day,
            free_trial=free_trial,
            start_date=start_date,
            end_date=end_date,
            auto_renew=auto_renew,
            external_reference=external_reference,
            metadata=metadata,
            discounts=discounts,
            splits=splits,
            shipping=shipping,
            callback=callback,
            geolocation=geolocation,
            session_id=session_id,
            integration_id=integration_id,
            on_behalf_of=on_behalf_of,
        )

        return create_subscription_body
