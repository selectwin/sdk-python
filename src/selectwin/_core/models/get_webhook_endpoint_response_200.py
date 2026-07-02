from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_webhook_endpoint_response_200_links import (
        GetWebhookEndpointResponse200Links,
    )
    from ..models.get_webhook_endpoint_response_200_merchant import (
        GetWebhookEndpointResponse200Merchant,
    )
    from ..models.get_webhook_endpoint_response_200_metadata_type_0 import (
        GetWebhookEndpointResponse200MetadataType0,
    )


T = TypeVar("T", bound="GetWebhookEndpointResponse200")


@_attrs_define
class GetWebhookEndpointResponse200:
    """
    Attributes:
        id (str): Public identifier (wbe_/wbh_…)
        name (str):
        endpoint (str):
        enabled (bool):
        events (list[str] | None):
        force_active (bool):
        shots_qty (int):
        failed_shots_qty (int):
        last_delivery_at (None | str):
        metadata (GetWebhookEndpointResponse200MetadataType0 | None):
        created_at (str):
        updated_at (str):
        merchant (GetWebhookEndpointResponse200Merchant | Unset):
        field_links (GetWebhookEndpointResponse200Links | Unset):
    """

    id: str
    name: str
    endpoint: str
    enabled: bool
    events: list[str] | None
    force_active: bool
    shots_qty: int
    failed_shots_qty: int
    last_delivery_at: None | str
    metadata: GetWebhookEndpointResponse200MetadataType0 | None
    created_at: str
    updated_at: str
    merchant: GetWebhookEndpointResponse200Merchant | Unset = UNSET
    field_links: GetWebhookEndpointResponse200Links | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.get_webhook_endpoint_response_200_metadata_type_0 import (
            GetWebhookEndpointResponse200MetadataType0,
        )

        id = self.id

        name = self.name

        endpoint = self.endpoint

        enabled = self.enabled

        events: list[str] | None
        if isinstance(self.events, list):
            events = self.events

        else:
            events = self.events

        force_active = self.force_active

        shots_qty = self.shots_qty

        failed_shots_qty = self.failed_shots_qty

        last_delivery_at: None | str
        last_delivery_at = self.last_delivery_at

        metadata: dict[str, Any] | None
        if isinstance(self.metadata, GetWebhookEndpointResponse200MetadataType0):
            metadata = self.metadata.to_dict()
        else:
            metadata = self.metadata

        created_at = self.created_at

        updated_at = self.updated_at

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
                "name": name,
                "endpoint": endpoint,
                "enabled": enabled,
                "events": events,
                "forceActive": force_active,
                "shotsQty": shots_qty,
                "failedShotsQty": failed_shots_qty,
                "lastDeliveryAt": last_delivery_at,
                "metadata": metadata,
                "createdAt": created_at,
                "updatedAt": updated_at,
            }
        )
        if merchant is not UNSET:
            field_dict["merchant"] = merchant
        if field_links is not UNSET:
            field_dict["_links"] = field_links

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_webhook_endpoint_response_200_links import (
            GetWebhookEndpointResponse200Links,
        )
        from ..models.get_webhook_endpoint_response_200_merchant import (
            GetWebhookEndpointResponse200Merchant,
        )
        from ..models.get_webhook_endpoint_response_200_metadata_type_0 import (
            GetWebhookEndpointResponse200MetadataType0,
        )

        d = dict(src_dict)
        id = d.pop("id")

        name = d.pop("name")

        endpoint = d.pop("endpoint")

        enabled = d.pop("enabled")

        def _parse_events(data: object) -> list[str] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                events_type_0 = cast(list[str], data)

                return events_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None, data)

        events = _parse_events(d.pop("events"))

        force_active = d.pop("forceActive")

        shots_qty = d.pop("shotsQty")

        failed_shots_qty = d.pop("failedShotsQty")

        def _parse_last_delivery_at(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        last_delivery_at = _parse_last_delivery_at(d.pop("lastDeliveryAt"))

        def _parse_metadata(
            data: object,
        ) -> GetWebhookEndpointResponse200MetadataType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                metadata_type_0 = GetWebhookEndpointResponse200MetadataType0.from_dict(
                    data
                )

                return metadata_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(GetWebhookEndpointResponse200MetadataType0 | None, data)

        metadata = _parse_metadata(d.pop("metadata"))

        created_at = d.pop("createdAt")

        updated_at = d.pop("updatedAt")

        _merchant = d.pop("merchant", UNSET)
        merchant: GetWebhookEndpointResponse200Merchant | Unset
        if isinstance(_merchant, Unset):
            merchant = UNSET
        else:
            merchant = GetWebhookEndpointResponse200Merchant.from_dict(_merchant)

        _field_links = d.pop("_links", UNSET)
        field_links: GetWebhookEndpointResponse200Links | Unset
        if isinstance(_field_links, Unset):
            field_links = UNSET
        else:
            field_links = GetWebhookEndpointResponse200Links.from_dict(_field_links)

        get_webhook_endpoint_response_200 = cls(
            id=id,
            name=name,
            endpoint=endpoint,
            enabled=enabled,
            events=events,
            force_active=force_active,
            shots_qty=shots_qty,
            failed_shots_qty=failed_shots_qty,
            last_delivery_at=last_delivery_at,
            metadata=metadata,
            created_at=created_at,
            updated_at=updated_at,
            merchant=merchant,
            field_links=field_links,
        )

        return get_webhook_endpoint_response_200
