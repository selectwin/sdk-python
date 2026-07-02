from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.list_webhook_events_response_200_data_item_dispatches_item import (
        ListWebhookEventsResponse200DataItemDispatchesItem,
    )
    from ..models.list_webhook_events_response_200_data_item_links import (
        ListWebhookEventsResponse200DataItemLinks,
    )
    from ..models.list_webhook_events_response_200_data_item_merchant import (
        ListWebhookEventsResponse200DataItemMerchant,
    )


T = TypeVar("T", bound="ListWebhookEventsResponse200DataItem")


@_attrs_define
class ListWebhookEventsResponse200DataItem:
    """
    Attributes:
        id (str): Public identifier (wbh_…)
        type_ (str):
        resource (str):
        resource_id (None | str):
        source (str):
        delivered (bool):
        attempts (int):
        created_at (str):
        data (Any | Unset):
        dispatches (list[ListWebhookEventsResponse200DataItemDispatchesItem] | Unset):
        merchant (ListWebhookEventsResponse200DataItemMerchant | Unset):
        field_links (ListWebhookEventsResponse200DataItemLinks | Unset):
    """

    id: str
    type_: str
    resource: str
    resource_id: None | str
    source: str
    delivered: bool
    attempts: int
    created_at: str
    data: Any | Unset = UNSET
    dispatches: list[ListWebhookEventsResponse200DataItemDispatchesItem] | Unset = UNSET
    merchant: ListWebhookEventsResponse200DataItemMerchant | Unset = UNSET
    field_links: ListWebhookEventsResponse200DataItemLinks | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        type_ = self.type_

        resource = self.resource

        resource_id: None | str
        resource_id = self.resource_id

        source = self.source

        delivered = self.delivered

        attempts = self.attempts

        created_at = self.created_at

        data = self.data

        dispatches: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.dispatches, Unset):
            dispatches = []
            for dispatches_item_data in self.dispatches:
                dispatches_item = dispatches_item_data.to_dict()
                dispatches.append(dispatches_item)

        merchant: dict[str, Any] | Unset = UNSET
        if not isinstance(self.merchant, Unset):
            merchant = self.merchant.to_dict()

        field_links: dict[str, Any] | Unset = UNSET
        if not isinstance(self.field_links, Unset):
            field_links = self.field_links.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "id": id,
                "type": type_,
                "resource": resource,
                "resourceId": resource_id,
                "source": source,
                "delivered": delivered,
                "attempts": attempts,
                "createdAt": created_at,
            }
        )
        if data is not UNSET:
            field_dict["data"] = data
        if dispatches is not UNSET:
            field_dict["dispatches"] = dispatches
        if merchant is not UNSET:
            field_dict["merchant"] = merchant
        if field_links is not UNSET:
            field_dict["_links"] = field_links

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.list_webhook_events_response_200_data_item_dispatches_item import (
            ListWebhookEventsResponse200DataItemDispatchesItem,
        )
        from ..models.list_webhook_events_response_200_data_item_links import (
            ListWebhookEventsResponse200DataItemLinks,
        )
        from ..models.list_webhook_events_response_200_data_item_merchant import (
            ListWebhookEventsResponse200DataItemMerchant,
        )

        d = dict(src_dict)
        id = d.pop("id")

        type_ = d.pop("type")

        resource = d.pop("resource")

        def _parse_resource_id(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        resource_id = _parse_resource_id(d.pop("resourceId"))

        source = d.pop("source")

        delivered = d.pop("delivered")

        attempts = d.pop("attempts")

        created_at = d.pop("createdAt")

        data = d.pop("data", UNSET)

        _dispatches = d.pop("dispatches", UNSET)
        dispatches: list[ListWebhookEventsResponse200DataItemDispatchesItem] | Unset = (
            UNSET
        )
        if _dispatches is not UNSET:
            dispatches = []
            for dispatches_item_data in _dispatches:
                dispatches_item = (
                    ListWebhookEventsResponse200DataItemDispatchesItem.from_dict(
                        dispatches_item_data
                    )
                )

                dispatches.append(dispatches_item)

        _merchant = d.pop("merchant", UNSET)
        merchant: ListWebhookEventsResponse200DataItemMerchant | Unset
        if isinstance(_merchant, Unset):
            merchant = UNSET
        else:
            merchant = ListWebhookEventsResponse200DataItemMerchant.from_dict(_merchant)

        _field_links = d.pop("_links", UNSET)
        field_links: ListWebhookEventsResponse200DataItemLinks | Unset
        if isinstance(_field_links, Unset):
            field_links = UNSET
        else:
            field_links = ListWebhookEventsResponse200DataItemLinks.from_dict(
                _field_links
            )

        list_webhook_events_response_200_data_item = cls(
            id=id,
            type_=type_,
            resource=resource,
            resource_id=resource_id,
            source=source,
            delivered=delivered,
            attempts=attempts,
            created_at=created_at,
            data=data,
            dispatches=dispatches,
            merchant=merchant,
            field_links=field_links,
        )

        return list_webhook_events_response_200_data_item
