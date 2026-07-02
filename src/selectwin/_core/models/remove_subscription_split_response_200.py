from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.remove_subscription_split_response_200_links import (
        RemoveSubscriptionSplitResponse200Links,
    )
    from ..models.remove_subscription_split_response_200_merchant import (
        RemoveSubscriptionSplitResponse200Merchant,
    )
    from ..models.remove_subscription_split_response_200_splits_item import (
        RemoveSubscriptionSplitResponse200SplitsItem,
    )


T = TypeVar("T", bound="RemoveSubscriptionSplitResponse200")


@_attrs_define
class RemoveSubscriptionSplitResponse200:
    """
    Attributes:
        subscription (str): Public identifier (subs_/sub_…)
        splits (list[RemoveSubscriptionSplitResponse200SplitsItem]):
        total_percentage (float):
        remaining_percentage (float):
        remaining_amount (str):
        merchant (RemoveSubscriptionSplitResponse200Merchant | Unset):
        field_links (RemoveSubscriptionSplitResponse200Links | Unset):
    """

    subscription: str
    splits: list[RemoveSubscriptionSplitResponse200SplitsItem]
    total_percentage: float
    remaining_percentage: float
    remaining_amount: str
    merchant: RemoveSubscriptionSplitResponse200Merchant | Unset = UNSET
    field_links: RemoveSubscriptionSplitResponse200Links | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        subscription = self.subscription

        splits = []
        for splits_item_data in self.splits:
            splits_item = splits_item_data.to_dict()
            splits.append(splits_item)

        total_percentage = self.total_percentage

        remaining_percentage = self.remaining_percentage

        remaining_amount = self.remaining_amount

        merchant: dict[str, Any] | Unset = UNSET
        if not isinstance(self.merchant, Unset):
            merchant = self.merchant.to_dict()

        field_links: dict[str, Any] | Unset = UNSET
        if not isinstance(self.field_links, Unset):
            field_links = self.field_links.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "subscription": subscription,
                "splits": splits,
                "totalPercentage": total_percentage,
                "remainingPercentage": remaining_percentage,
                "remainingAmount": remaining_amount,
            }
        )
        if merchant is not UNSET:
            field_dict["merchant"] = merchant
        if field_links is not UNSET:
            field_dict["_links"] = field_links

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.remove_subscription_split_response_200_links import (
            RemoveSubscriptionSplitResponse200Links,
        )
        from ..models.remove_subscription_split_response_200_merchant import (
            RemoveSubscriptionSplitResponse200Merchant,
        )
        from ..models.remove_subscription_split_response_200_splits_item import (
            RemoveSubscriptionSplitResponse200SplitsItem,
        )

        d = dict(src_dict)
        subscription = d.pop("subscription")

        splits = []
        _splits = d.pop("splits")
        for splits_item_data in _splits:
            splits_item = RemoveSubscriptionSplitResponse200SplitsItem.from_dict(
                splits_item_data
            )

            splits.append(splits_item)

        total_percentage = d.pop("totalPercentage")

        remaining_percentage = d.pop("remainingPercentage")

        remaining_amount = d.pop("remainingAmount")

        _merchant = d.pop("merchant", UNSET)
        merchant: RemoveSubscriptionSplitResponse200Merchant | Unset
        if isinstance(_merchant, Unset):
            merchant = UNSET
        else:
            merchant = RemoveSubscriptionSplitResponse200Merchant.from_dict(_merchant)

        _field_links = d.pop("_links", UNSET)
        field_links: RemoveSubscriptionSplitResponse200Links | Unset
        if isinstance(_field_links, Unset):
            field_links = UNSET
        else:
            field_links = RemoveSubscriptionSplitResponse200Links.from_dict(
                _field_links
            )

        remove_subscription_split_response_200 = cls(
            subscription=subscription,
            splits=splits,
            total_percentage=total_percentage,
            remaining_percentage=remaining_percentage,
            remaining_amount=remaining_amount,
            merchant=merchant,
            field_links=field_links,
        )

        return remove_subscription_split_response_200
