from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.list_cards_response_200_page_offset import (
        ListCardsResponse200PageOffset,
    )


T = TypeVar("T", bound="ListCardsResponse200Page")


@_attrs_define
class ListCardsResponse200Page:
    """
    Attributes:
        offset (ListCardsResponse200PageOffset):
        current (int):
        total (int):
    """

    offset: ListCardsResponse200PageOffset
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
        from ..models.list_cards_response_200_page_offset import (
            ListCardsResponse200PageOffset,
        )

        d = dict(src_dict)
        offset = ListCardsResponse200PageOffset.from_dict(d.pop("offset"))

        current = d.pop("current")

        total = d.pop("total")

        list_cards_response_200_page = cls(
            offset=offset,
            current=current,
            total=total,
        )

        return list_cards_response_200_page
