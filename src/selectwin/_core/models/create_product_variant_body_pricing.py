from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.create_product_variant_body_pricing_billing_frequency import (
    CreateProductVariantBodyPricingBillingFrequency,
)
from ..models.create_product_variant_body_pricing_billing_type import (
    CreateProductVariantBodyPricingBillingType,
)
from ..models.create_product_variant_body_pricing_schema import (
    CreateProductVariantBodyPricingSchema,
)
from ..models.create_product_variant_body_pricing_tiers_mode import (
    CreateProductVariantBodyPricingTiersMode,
)
from ..models.create_product_variant_body_pricing_trial_interval import (
    CreateProductVariantBodyPricingTrialInterval,
)
from ..models.create_product_variant_body_pricing_type import (
    CreateProductVariantBodyPricingType,
)
from ..models.create_product_variant_body_pricing_usage_aggregation import (
    CreateProductVariantBodyPricingUsageAggregation,
)
from ..models.create_product_variant_body_pricing_usage_type import (
    CreateProductVariantBodyPricingUsageType,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.create_product_variant_body_pricing_tiers_item import (
        CreateProductVariantBodyPricingTiersItem,
    )
    from ..models.create_product_variant_body_pricing_transform_quantity import (
        CreateProductVariantBodyPricingTransformQuantity,
    )


T = TypeVar("T", bound="CreateProductVariantBodyPricing")


@_attrs_define
class CreateProductVariantBodyPricing:
    """
    Attributes:
        unit_price (int | Unset):
        old_price (int | Unset):
        cost_per_item (int | Unset):
        currency (str | Unset): ISO 4217 currency code Default: 'BRL'.
        schema (CreateProductVariantBodyPricingSchema | Unset):  Default: CreateProductVariantBodyPricingSchema.UNIT.
        type_ (CreateProductVariantBodyPricingType | Unset):  Default: CreateProductVariantBodyPricingType.ONETIME.
        days_trial (int | Unset):
        billing_type (CreateProductVariantBodyPricingBillingType | Unset):
        billing_frequency (CreateProductVariantBodyPricingBillingFrequency | Unset):
        billing_frequency_count (int | Unset):
        billing_exact_day (int | Unset):
        cycles (int | None | Unset):
        trial_interval (CreateProductVariantBodyPricingTrialInterval | Unset):
        trial_interval_count (int | Unset):
        tiers_mode (CreateProductVariantBodyPricingTiersMode | Unset):
        tiers (list[CreateProductVariantBodyPricingTiersItem] | Unset):
        transform_quantity (CreateProductVariantBodyPricingTransformQuantity | Unset):
        usage_type (CreateProductVariantBodyPricingUsageType | Unset):  Default:
            CreateProductVariantBodyPricingUsageType.LICENSED.
        usage_aggregation (CreateProductVariantBodyPricingUsageAggregation | Unset):
        meter_event_name (str | Unset):
    """

    unit_price: int | Unset = UNSET
    old_price: int | Unset = UNSET
    cost_per_item: int | Unset = UNSET
    currency: str | Unset = "BRL"
    schema: CreateProductVariantBodyPricingSchema | Unset = (
        CreateProductVariantBodyPricingSchema.UNIT
    )
    type_: CreateProductVariantBodyPricingType | Unset = (
        CreateProductVariantBodyPricingType.ONETIME
    )
    days_trial: int | Unset = UNSET
    billing_type: CreateProductVariantBodyPricingBillingType | Unset = UNSET
    billing_frequency: CreateProductVariantBodyPricingBillingFrequency | Unset = UNSET
    billing_frequency_count: int | Unset = UNSET
    billing_exact_day: int | Unset = UNSET
    cycles: int | None | Unset = UNSET
    trial_interval: CreateProductVariantBodyPricingTrialInterval | Unset = UNSET
    trial_interval_count: int | Unset = UNSET
    tiers_mode: CreateProductVariantBodyPricingTiersMode | Unset = UNSET
    tiers: list[CreateProductVariantBodyPricingTiersItem] | Unset = UNSET
    transform_quantity: CreateProductVariantBodyPricingTransformQuantity | Unset = UNSET
    usage_type: CreateProductVariantBodyPricingUsageType | Unset = (
        CreateProductVariantBodyPricingUsageType.LICENSED
    )
    usage_aggregation: CreateProductVariantBodyPricingUsageAggregation | Unset = UNSET
    meter_event_name: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        unit_price = self.unit_price

        old_price = self.old_price

        cost_per_item = self.cost_per_item

        currency = self.currency

        schema: str | Unset = UNSET
        if not isinstance(self.schema, Unset):
            schema = self.schema.value

        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        days_trial = self.days_trial

        billing_type: str | Unset = UNSET
        if not isinstance(self.billing_type, Unset):
            billing_type = self.billing_type.value

        billing_frequency: str | Unset = UNSET
        if not isinstance(self.billing_frequency, Unset):
            billing_frequency = self.billing_frequency.value

        billing_frequency_count = self.billing_frequency_count

        billing_exact_day = self.billing_exact_day

        cycles: int | None | Unset
        if isinstance(self.cycles, Unset):
            cycles = UNSET
        else:
            cycles = self.cycles

        trial_interval: str | Unset = UNSET
        if not isinstance(self.trial_interval, Unset):
            trial_interval = self.trial_interval.value

        trial_interval_count = self.trial_interval_count

        tiers_mode: str | Unset = UNSET
        if not isinstance(self.tiers_mode, Unset):
            tiers_mode = self.tiers_mode.value

        tiers: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.tiers, Unset):
            tiers = []
            for tiers_item_data in self.tiers:
                tiers_item = tiers_item_data.to_dict()
                tiers.append(tiers_item)

        transform_quantity: dict[str, Any] | Unset = UNSET
        if not isinstance(self.transform_quantity, Unset):
            transform_quantity = self.transform_quantity.to_dict()

        usage_type: str | Unset = UNSET
        if not isinstance(self.usage_type, Unset):
            usage_type = self.usage_type.value

        usage_aggregation: str | Unset = UNSET
        if not isinstance(self.usage_aggregation, Unset):
            usage_aggregation = self.usage_aggregation.value

        meter_event_name = self.meter_event_name

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if unit_price is not UNSET:
            field_dict["unitPrice"] = unit_price
        if old_price is not UNSET:
            field_dict["oldPrice"] = old_price
        if cost_per_item is not UNSET:
            field_dict["costPerItem"] = cost_per_item
        if currency is not UNSET:
            field_dict["currency"] = currency
        if schema is not UNSET:
            field_dict["schema"] = schema
        if type_ is not UNSET:
            field_dict["type"] = type_
        if days_trial is not UNSET:
            field_dict["daysTrial"] = days_trial
        if billing_type is not UNSET:
            field_dict["billingType"] = billing_type
        if billing_frequency is not UNSET:
            field_dict["billingFrequency"] = billing_frequency
        if billing_frequency_count is not UNSET:
            field_dict["billingFrequencyCount"] = billing_frequency_count
        if billing_exact_day is not UNSET:
            field_dict["billingExactDay"] = billing_exact_day
        if cycles is not UNSET:
            field_dict["cycles"] = cycles
        if trial_interval is not UNSET:
            field_dict["trialInterval"] = trial_interval
        if trial_interval_count is not UNSET:
            field_dict["trialIntervalCount"] = trial_interval_count
        if tiers_mode is not UNSET:
            field_dict["tiersMode"] = tiers_mode
        if tiers is not UNSET:
            field_dict["tiers"] = tiers
        if transform_quantity is not UNSET:
            field_dict["transformQuantity"] = transform_quantity
        if usage_type is not UNSET:
            field_dict["usageType"] = usage_type
        if usage_aggregation is not UNSET:
            field_dict["usageAggregation"] = usage_aggregation
        if meter_event_name is not UNSET:
            field_dict["meterEventName"] = meter_event_name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.create_product_variant_body_pricing_tiers_item import (
            CreateProductVariantBodyPricingTiersItem,
        )
        from ..models.create_product_variant_body_pricing_transform_quantity import (
            CreateProductVariantBodyPricingTransformQuantity,
        )

        d = dict(src_dict)
        unit_price = d.pop("unitPrice", UNSET)

        old_price = d.pop("oldPrice", UNSET)

        cost_per_item = d.pop("costPerItem", UNSET)

        currency = d.pop("currency", UNSET)

        _schema = d.pop("schema", UNSET)
        schema: CreateProductVariantBodyPricingSchema | Unset
        if isinstance(_schema, Unset):
            schema = UNSET
        else:
            schema = CreateProductVariantBodyPricingSchema(_schema)

        _type_ = d.pop("type", UNSET)
        type_: CreateProductVariantBodyPricingType | Unset
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = CreateProductVariantBodyPricingType(_type_)

        days_trial = d.pop("daysTrial", UNSET)

        _billing_type = d.pop("billingType", UNSET)
        billing_type: CreateProductVariantBodyPricingBillingType | Unset
        if isinstance(_billing_type, Unset):
            billing_type = UNSET
        else:
            billing_type = CreateProductVariantBodyPricingBillingType(_billing_type)

        _billing_frequency = d.pop("billingFrequency", UNSET)
        billing_frequency: CreateProductVariantBodyPricingBillingFrequency | Unset
        if isinstance(_billing_frequency, Unset):
            billing_frequency = UNSET
        else:
            billing_frequency = CreateProductVariantBodyPricingBillingFrequency(
                _billing_frequency
            )

        billing_frequency_count = d.pop("billingFrequencyCount", UNSET)

        billing_exact_day = d.pop("billingExactDay", UNSET)

        def _parse_cycles(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        cycles = _parse_cycles(d.pop("cycles", UNSET))

        _trial_interval = d.pop("trialInterval", UNSET)
        trial_interval: CreateProductVariantBodyPricingTrialInterval | Unset
        if isinstance(_trial_interval, Unset):
            trial_interval = UNSET
        else:
            trial_interval = CreateProductVariantBodyPricingTrialInterval(
                _trial_interval
            )

        trial_interval_count = d.pop("trialIntervalCount", UNSET)

        _tiers_mode = d.pop("tiersMode", UNSET)
        tiers_mode: CreateProductVariantBodyPricingTiersMode | Unset
        if isinstance(_tiers_mode, Unset):
            tiers_mode = UNSET
        else:
            tiers_mode = CreateProductVariantBodyPricingTiersMode(_tiers_mode)

        _tiers = d.pop("tiers", UNSET)
        tiers: list[CreateProductVariantBodyPricingTiersItem] | Unset = UNSET
        if _tiers is not UNSET:
            tiers = []
            for tiers_item_data in _tiers:
                tiers_item = CreateProductVariantBodyPricingTiersItem.from_dict(
                    tiers_item_data
                )

                tiers.append(tiers_item)

        _transform_quantity = d.pop("transformQuantity", UNSET)
        transform_quantity: CreateProductVariantBodyPricingTransformQuantity | Unset
        if isinstance(_transform_quantity, Unset):
            transform_quantity = UNSET
        else:
            transform_quantity = (
                CreateProductVariantBodyPricingTransformQuantity.from_dict(
                    _transform_quantity
                )
            )

        _usage_type = d.pop("usageType", UNSET)
        usage_type: CreateProductVariantBodyPricingUsageType | Unset
        if isinstance(_usage_type, Unset):
            usage_type = UNSET
        else:
            usage_type = CreateProductVariantBodyPricingUsageType(_usage_type)

        _usage_aggregation = d.pop("usageAggregation", UNSET)
        usage_aggregation: CreateProductVariantBodyPricingUsageAggregation | Unset
        if isinstance(_usage_aggregation, Unset):
            usage_aggregation = UNSET
        else:
            usage_aggregation = CreateProductVariantBodyPricingUsageAggregation(
                _usage_aggregation
            )

        meter_event_name = d.pop("meterEventName", UNSET)

        create_product_variant_body_pricing = cls(
            unit_price=unit_price,
            old_price=old_price,
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
            tiers=tiers,
            transform_quantity=transform_quantity,
            usage_type=usage_type,
            usage_aggregation=usage_aggregation,
            meter_event_name=meter_event_name,
        )

        return create_product_variant_body_pricing
