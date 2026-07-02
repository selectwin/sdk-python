from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.create_subscription_response_201_billing_address import (
        CreateSubscriptionResponse201BillingAddress,
    )


T = TypeVar("T", bound="CreateSubscriptionResponse201Billing")


@_attrs_define
class CreateSubscriptionResponse201Billing:
    """
    Attributes:
        frequency (None | str):
        frequency_count (int | None):
        end_date (None | str):
        exact_day (int | None):
        free_trial_days (int | None):
        address (CreateSubscriptionResponse201BillingAddress):
    """

    frequency: None | str
    frequency_count: int | None
    end_date: None | str
    exact_day: int | None
    free_trial_days: int | None
    address: CreateSubscriptionResponse201BillingAddress

    def to_dict(self) -> dict[str, Any]:
        frequency: None | str
        frequency = self.frequency

        frequency_count: int | None
        frequency_count = self.frequency_count

        end_date: None | str
        end_date = self.end_date

        exact_day: int | None
        exact_day = self.exact_day

        free_trial_days: int | None
        free_trial_days = self.free_trial_days

        address = self.address.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "frequency": frequency,
                "frequencyCount": frequency_count,
                "endDate": end_date,
                "exactDay": exact_day,
                "freeTrialDays": free_trial_days,
                "address": address,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.create_subscription_response_201_billing_address import (
            CreateSubscriptionResponse201BillingAddress,
        )

        d = dict(src_dict)

        def _parse_frequency(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        frequency = _parse_frequency(d.pop("frequency"))

        def _parse_frequency_count(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        frequency_count = _parse_frequency_count(d.pop("frequencyCount"))

        def _parse_end_date(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        end_date = _parse_end_date(d.pop("endDate"))

        def _parse_exact_day(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        exact_day = _parse_exact_day(d.pop("exactDay"))

        def _parse_free_trial_days(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        free_trial_days = _parse_free_trial_days(d.pop("freeTrialDays"))

        address = CreateSubscriptionResponse201BillingAddress.from_dict(
            d.pop("address")
        )

        create_subscription_response_201_billing = cls(
            frequency=frequency,
            frequency_count=frequency_count,
            end_date=end_date,
            exact_day=exact_day,
            free_trial_days=free_trial_days,
            address=address,
        )

        return create_subscription_response_201_billing
