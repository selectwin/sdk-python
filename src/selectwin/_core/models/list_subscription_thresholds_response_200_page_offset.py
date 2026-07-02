from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="ListSubscriptionThresholdsResponse200PageOffset")


@_attrs_define
class ListSubscriptionThresholdsResponse200PageOffset:
    """
    Attributes:
        first (int):
        prev (int):
        next_ (int):
        last (int):
    """

    first: int
    prev: int
    next_: int
    last: int

    def to_dict(self) -> dict[str, Any]:
        first = self.first

        prev = self.prev

        next_ = self.next_

        last = self.last

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "first": first,
                "prev": prev,
                "next": next_,
                "last": last,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        first = d.pop("first")

        prev = d.pop("prev")

        next_ = d.pop("next")

        last = d.pop("last")

        list_subscription_thresholds_response_200_page_offset = cls(
            first=first,
            prev=prev,
            next_=next_,
            last=last,
        )

        return list_subscription_thresholds_response_200_page_offset
