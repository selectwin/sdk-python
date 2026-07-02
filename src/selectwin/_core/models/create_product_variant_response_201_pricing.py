from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.create_product_variant_response_201_pricing_schema import (
    CreateProductVariantResponse201PricingSchema,
)
from ..models.create_product_variant_response_201_pricing_type import (
    CreateProductVariantResponse201PricingType,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateProductVariantResponse201Pricing")


@_attrs_define
class CreateProductVariantResponse201Pricing:
    """
    Attributes:
        old_price (int | None):
        unit_price (int | None):
        cost_per_item (int | None):
        currency (str):
        schema (CreateProductVariantResponse201PricingSchema):
        type_ (CreateProductVariantResponse201PricingType):
        days_trial (int | None):
        billing_type (None | str):
        billing_frequency (None | str):
        billing_frequency_count (int | None):
        billing_exact_day (int | None):
        cycles (int | None):
        trial_interval (None | str):
        trial_interval_count (int | None):
        tiers_mode (None | str):
        usage_type (str):
        usage_aggregation (None | str):
        meter_event_name (None | str):
        tiers (Any | Unset):
        transform_quantity (Any | Unset):
    """

    old_price: int | None
    unit_price: int | None
    cost_per_item: int | None
    currency: str
    schema: CreateProductVariantResponse201PricingSchema
    type_: CreateProductVariantResponse201PricingType
    days_trial: int | None
    billing_type: None | str
    billing_frequency: None | str
    billing_frequency_count: int | None
    billing_exact_day: int | None
    cycles: int | None
    trial_interval: None | str
    trial_interval_count: int | None
    tiers_mode: None | str
    usage_type: str
    usage_aggregation: None | str
    meter_event_name: None | str
    tiers: Any | Unset = UNSET
    transform_quantity: Any | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        old_price: int | None
        old_price = self.old_price

        unit_price: int | None
        unit_price = self.unit_price

        cost_per_item: int | None
        cost_per_item = self.cost_per_item

        currency = self.currency

        schema = self.schema.value

        type_ = self.type_.value

        days_trial: int | None
        days_trial = self.days_trial

        billing_type: None | str
        billing_type = self.billing_type

        billing_frequency: None | str
        billing_frequency = self.billing_frequency

        billing_frequency_count: int | None
        billing_frequency_count = self.billing_frequency_count

        billing_exact_day: int | None
        billing_exact_day = self.billing_exact_day

        cycles: int | None
        cycles = self.cycles

        trial_interval: None | str
        trial_interval = self.trial_interval

        trial_interval_count: int | None
        trial_interval_count = self.trial_interval_count

        tiers_mode: None | str
        tiers_mode = self.tiers_mode

        usage_type = self.usage_type

        usage_aggregation: None | str
        usage_aggregation = self.usage_aggregation

        meter_event_name: None | str
        meter_event_name = self.meter_event_name

        tiers = self.tiers

        transform_quantity = self.transform_quantity

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "oldPrice": old_price,
                "unitPrice": unit_price,
                "costPerItem": cost_per_item,
                "currency": currency,
                "schema": schema,
                "type": type_,
                "daysTrial": days_trial,
                "billingType": billing_type,
                "billingFrequency": billing_frequency,
                "billingFrequencyCount": billing_frequency_count,
                "billingExactDay": billing_exact_day,
                "cycles": cycles,
                "trialInterval": trial_interval,
                "trialIntervalCount": trial_interval_count,
                "tiersMode": tiers_mode,
                "usageType": usage_type,
                "usageAggregation": usage_aggregation,
                "meterEventName": meter_event_name,
            }
        )
        if tiers is not UNSET:
            field_dict["tiers"] = tiers
        if transform_quantity is not UNSET:
            field_dict["transformQuantity"] = transform_quantity

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_old_price(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        old_price = _parse_old_price(d.pop("oldPrice"))

        def _parse_unit_price(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        unit_price = _parse_unit_price(d.pop("unitPrice"))

        def _parse_cost_per_item(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        cost_per_item = _parse_cost_per_item(d.pop("costPerItem"))

        currency = d.pop("currency")

        schema = CreateProductVariantResponse201PricingSchema(d.pop("schema"))

        type_ = CreateProductVariantResponse201PricingType(d.pop("type"))

        def _parse_days_trial(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        days_trial = _parse_days_trial(d.pop("daysTrial"))

        def _parse_billing_type(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        billing_type = _parse_billing_type(d.pop("billingType"))

        def _parse_billing_frequency(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        billing_frequency = _parse_billing_frequency(d.pop("billingFrequency"))

        def _parse_billing_frequency_count(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        billing_frequency_count = _parse_billing_frequency_count(
            d.pop("billingFrequencyCount")
        )

        def _parse_billing_exact_day(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        billing_exact_day = _parse_billing_exact_day(d.pop("billingExactDay"))

        def _parse_cycles(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        cycles = _parse_cycles(d.pop("cycles"))

        def _parse_trial_interval(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        trial_interval = _parse_trial_interval(d.pop("trialInterval"))

        def _parse_trial_interval_count(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        trial_interval_count = _parse_trial_interval_count(d.pop("trialIntervalCount"))

        def _parse_tiers_mode(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        tiers_mode = _parse_tiers_mode(d.pop("tiersMode"))

        usage_type = d.pop("usageType")

        def _parse_usage_aggregation(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        usage_aggregation = _parse_usage_aggregation(d.pop("usageAggregation"))

        def _parse_meter_event_name(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        meter_event_name = _parse_meter_event_name(d.pop("meterEventName"))

        tiers = d.pop("tiers", UNSET)

        transform_quantity = d.pop("transformQuantity", UNSET)

        create_product_variant_response_201_pricing = cls(
            old_price=old_price,
            unit_price=unit_price,
            cost_per_item=cost_per_item,
            currency=currency,
            schema=schema,
            type_=type_,
            days_trial=days_trial,
            billing_type=billing_type,
            billing_frequency=billing_frequency,
            billing_frequency_count=billing_frequency_count,
            billing_exact_day=billing_exact_day,
            cycles=cycles,
            trial_interval=trial_interval,
            trial_interval_count=trial_interval_count,
            tiers_mode=tiers_mode,
            usage_type=usage_type,
            usage_aggregation=usage_aggregation,
            meter_event_name=meter_event_name,
            tiers=tiers,
            transform_quantity=transform_quantity,
        )

        return create_product_variant_response_201_pricing
