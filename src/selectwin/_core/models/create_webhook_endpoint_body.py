from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..models.create_webhook_endpoint_body_events_item import (
    CreateWebhookEndpointBodyEventsItem,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.create_webhook_endpoint_body_metadata import (
        CreateWebhookEndpointBodyMetadata,
    )


T = TypeVar("T", bound="CreateWebhookEndpointBody")


@_attrs_define
class CreateWebhookEndpointBody:
    """
    Attributes:
        name (str):
        endpoint (str):
        events (list[CreateWebhookEndpointBodyEventsItem] | Unset):
        force_active (bool | Unset):
        enabled (bool | Unset):
        header_authorization (str | Unset):
        header_authorization_type (str | Unset):
        metadata (CreateWebhookEndpointBodyMetadata | Unset):
    """

    name: str
    endpoint: str
    events: list[CreateWebhookEndpointBodyEventsItem] | Unset = UNSET
    force_active: bool | Unset = UNSET
    enabled: bool | Unset = UNSET
    header_authorization: str | Unset = UNSET
    header_authorization_type: str | Unset = UNSET
    metadata: CreateWebhookEndpointBodyMetadata | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        endpoint = self.endpoint

        events: list[str] | Unset = UNSET
        if not isinstance(self.events, Unset):
            events = []
            for events_item_data in self.events:
                events_item = events_item_data.value
                events.append(events_item)

        force_active = self.force_active

        enabled = self.enabled

        header_authorization = self.header_authorization

        header_authorization_type = self.header_authorization_type

        metadata: dict[str, Any] | Unset = UNSET
        if not isinstance(self.metadata, Unset):
            metadata = self.metadata.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "name": name,
                "endpoint": endpoint,
            }
        )
        if events is not UNSET:
            field_dict["events"] = events
        if force_active is not UNSET:
            field_dict["forceActive"] = force_active
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if header_authorization is not UNSET:
            field_dict["headerAuthorization"] = header_authorization
        if header_authorization_type is not UNSET:
            field_dict["headerAuthorizationType"] = header_authorization_type
        if metadata is not UNSET:
            field_dict["metadata"] = metadata

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.create_webhook_endpoint_body_metadata import (
            CreateWebhookEndpointBodyMetadata,
        )

        d = dict(src_dict)
        name = d.pop("name")

        endpoint = d.pop("endpoint")

        _events = d.pop("events", UNSET)
        events: list[CreateWebhookEndpointBodyEventsItem] | Unset = UNSET
        if _events is not UNSET:
            events = []
            for events_item_data in _events:
                events_item = CreateWebhookEndpointBodyEventsItem(events_item_data)

                events.append(events_item)

        force_active = d.pop("forceActive", UNSET)

        enabled = d.pop("enabled", UNSET)

        header_authorization = d.pop("headerAuthorization", UNSET)

        header_authorization_type = d.pop("headerAuthorizationType", UNSET)

        _metadata = d.pop("metadata", UNSET)
        metadata: CreateWebhookEndpointBodyMetadata | Unset
        if isinstance(_metadata, Unset):
            metadata = UNSET
        else:
            metadata = CreateWebhookEndpointBodyMetadata.from_dict(_metadata)

        create_webhook_endpoint_body = cls(
            name=name,
            endpoint=endpoint,
            events=events,
            force_active=force_active,
            enabled=enabled,
            header_authorization=header_authorization,
            header_authorization_type=header_authorization_type,
            metadata=metadata,
        )

        return create_webhook_endpoint_body
