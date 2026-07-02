from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.list_checkout_sessions_response_200_page_offset import (
        ListCheckoutSessionsResponse200PageOffset,
    )


T = TypeVar("T", bound="ListCheckoutSessionsResponse200Page")


@_attrs_define
class ListCheckoutSessionsResponse200Page:
    """
    Attributes:
        offset (ListCheckoutSessionsResponse200PageOffset):
        current (int):
        total (int):
    """

    offset: ListCheckoutSessionsResponse200PageOffset
    current: int
    total: int

    def to_dict(self) -> dict[str, Any]:
        offset = self.offset.to_dict()

        current = self.current

        total = self.total

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "offset": offset,
                "current": current,
                "total": total,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.list_checkout_sessions_response_200_page_offset import (
            ListCheckoutSessionsResponse200PageOffset,
        )

        d = dict(src_dict)
        offset = ListCheckoutSessionsResponse200PageOffset.from_dict(d.pop("offset"))

        current = d.pop("current")

        total = d.pop("total")

        list_checkout_sessions_response_200_page = cls(
            offset=offset,
            current=current,
            total=total,
        )

        return list_checkout_sessions_response_200_page
