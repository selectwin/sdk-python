from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.utils_rules_of_recurrencies_response_200_data_frequency_count import (
        UtilsRulesOfRecurrenciesResponse200DataFrequencyCount,
    )


T = TypeVar("T", bound="UtilsRulesOfRecurrenciesResponse200Data")


@_attrs_define
class UtilsRulesOfRecurrenciesResponse200Data:
    """
    Attributes:
        frequencies (list[str]):
        frequency_count (UtilsRulesOfRecurrenciesResponse200DataFrequencyCount):
        pricing_types (list[str]):
        pricing_schemas (list[str]):
        billing_types (list[str]):
        trial_intervals (list[str]):
    """

    frequencies: list[str]
    frequency_count: UtilsRulesOfRecurrenciesResponse200DataFrequencyCount
    pricing_types: list[str]
    pricing_schemas: list[str]
    billing_types: list[str]
    trial_intervals: list[str]

    def to_dict(self) -> dict[str, Any]:
        frequencies = self.frequencies

        frequency_count = self.frequency_count.to_dict()

        pricing_types = self.pricing_types

        pricing_schemas = self.pricing_schemas

        billing_types = self.billing_types

        trial_intervals = self.trial_intervals

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "frequencies": frequencies,
                "frequencyCount": frequency_count,
                "pricingTypes": pricing_types,
                "pricingSchemas": pricing_schemas,
                "billingTypes": billing_types,
                "trialIntervals": trial_intervals,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.utils_rules_of_recurrencies_response_200_data_frequency_count import (
            UtilsRulesOfRecurrenciesResponse200DataFrequencyCount,
        )

        d = dict(src_dict)
        frequencies = cast(list[str], d.pop("frequencies"))

        frequency_count = (
            UtilsRulesOfRecurrenciesResponse200DataFrequencyCount.from_dict(
                d.pop("frequencyCount")
            )
        )

        pricing_types = cast(list[str], d.pop("pricingTypes"))

        pricing_schemas = cast(list[str], d.pop("pricingSchemas"))

        billing_types = cast(list[str], d.pop("billingTypes"))

        trial_intervals = cast(list[str], d.pop("trialIntervals"))

        utils_rules_of_recurrencies_response_200_data = cls(
            frequencies=frequencies,
            frequency_count=frequency_count,
            pricing_types=pricing_types,
            pricing_schemas=pricing_schemas,
            billing_types=billing_types,
            trial_intervals=trial_intervals,
        )

        return utils_rules_of_recurrencies_response_200_data
