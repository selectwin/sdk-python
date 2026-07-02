from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.list_addresses_response_200_data_item import (
        ListAddressesResponse200DataItem,
    )
    from ..models.list_addresses_response_200_links import ListAddressesResponse200Links
    from ..models.list_addresses_response_200_merchant import (
        ListAddressesResponse200Merchant,
    )
    from ..models.list_addresses_response_200_page import ListAddressesResponse200Page


T = TypeVar("T", bound="ListAddressesResponse200")


@_attrs_define
class ListAddressesResponse200:
    """
    Attributes:
        offset (int):
        limit (int):
        total (int):
        page (ListAddressesResponse200Page):
        has_more (bool):
        data (list[ListAddressesResponse200DataItem]):
        merchant (ListAddressesResponse200Merchant | Unset):
        field_links (ListAddressesResponse200Links | Unset):
    """

    offset: int
    limit: int
    total: int
    page: ListAddressesResponse200Page
    has_more: bool
    data: list[ListAddressesResponse200DataItem]
    merchant: ListAddressesResponse200Merchant | Unset = UNSET
    field_links: ListAddressesResponse200Links | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        offset = self.offset

        limit = self.limit

        total = self.total

        page = self.page.to_dict()

        has_more = self.has_more

        data = []
        for data_item_data in self.data:
            data_item = data_item_data.to_dict()
            data.append(data_item)

        merchant: dict[str, Any] | Unset = UNSET
        if not isinstance(self.merchant, Unset):
            merchant = self.merchant.to_dict()

        field_links: dict[str, Any] | Unset = UNSET
        if not isinstance(self.field_links, Unset):
            field_links = self.field_links.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "offset": offset,
                "limit": limit,
                "total": total,
                "page": page,
                "hasMore": has_more,
                "data": data,
            }
        )
        if merchant is not UNSET:
            field_dict["merchant"] = merchant
        if field_links is not UNSET:
            field_dict["_links"] = field_links

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.list_addresses_response_200_data_item import (
            ListAddressesResponse200DataItem,
        )
        from ..models.list_addresses_response_200_links import (
            ListAddressesResponse200Links,
        )
        from ..models.list_addresses_response_200_merchant import (
            ListAddressesResponse200Merchant,
        )
        from ..models.list_addresses_response_200_page import (
            ListAddressesResponse200Page,
        )

        d = dict(src_dict)
        offset = d.pop("offset")

        limit = d.pop("limit")

        total = d.pop("total")

        page = ListAddressesResponse200Page.from_dict(d.pop("page"))

        has_more = d.pop("hasMore")

        data = []
        _data = d.pop("data")
        for data_item_data in _data:
            data_item = ListAddressesResponse200DataItem.from_dict(data_item_data)

            data.append(data_item)

        _merchant = d.pop("merchant", UNSET)
        merchant: ListAddressesResponse200Merchant | Unset
        if isinstance(_merchant, Unset):
            merchant = UNSET
        else:
            merchant = ListAddressesResponse200Merchant.from_dict(_merchant)

        _field_links = d.pop("_links", UNSET)
        field_links: ListAddressesResponse200Links | Unset
        if isinstance(_field_links, Unset):
            field_links = UNSET
        else:
            field_links = ListAddressesResponse200Links.from_dict(_field_links)

        list_addresses_response_200 = cls(
            offset=offset,
            limit=limit,
            total=total,
            page=page,
            has_more=has_more,
            data=data,
            merchant=merchant,
            field_links=field_links,
        )

        return list_addresses_response_200
