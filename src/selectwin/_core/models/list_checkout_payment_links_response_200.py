from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.list_checkout_payment_links_response_200_data_item import (
        ListCheckoutPaymentLinksResponse200DataItem,
    )
    from ..models.list_checkout_payment_links_response_200_page import (
        ListCheckoutPaymentLinksResponse200Page,
    )


T = TypeVar("T", bound="ListCheckoutPaymentLinksResponse200")


@_attrs_define
class ListCheckoutPaymentLinksResponse200:
    """
    Attributes:
        offset (int):
        limit (int):
        total (int):
        page (ListCheckoutPaymentLinksResponse200Page):
        data (list[ListCheckoutPaymentLinksResponse200DataItem]):
        has_more (bool):
    """

    offset: int
    limit: int
    total: int
    page: ListCheckoutPaymentLinksResponse200Page
    data: list[ListCheckoutPaymentLinksResponse200DataItem]
    has_more: bool

    def to_dict(self) -> dict[str, Any]:
        offset = self.offset

        limit = self.limit

        total = self.total

        page = self.page.to_dict()

        data = []
        for data_item_data in self.data:
            data_item = data_item_data.to_dict()
            data.append(data_item)

        has_more = self.has_more

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "offset": offset,
                "limit": limit,
                "total": total,
                "page": page,
                "data": data,
                "hasMore": has_more,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.list_checkout_payment_links_response_200_data_item import (
            ListCheckoutPaymentLinksResponse200DataItem,
        )
        from ..models.list_checkout_payment_links_response_200_page import (
            ListCheckoutPaymentLinksResponse200Page,
        )

        d = dict(src_dict)
        offset = d.pop("offset")

        limit = d.pop("limit")

        total = d.pop("total")

        page = ListCheckoutPaymentLinksResponse200Page.from_dict(d.pop("page"))

        data = []
        _data = d.pop("data")
        for data_item_data in _data:
            data_item = ListCheckoutPaymentLinksResponse200DataItem.from_dict(
                data_item_data
            )

            data.append(data_item)

        has_more = d.pop("hasMore")

        list_checkout_payment_links_response_200 = cls(
            offset=offset,
            limit=limit,
            total=total,
            page=page,
            data=data,
            has_more=has_more,
        )

        return list_checkout_payment_links_response_200
