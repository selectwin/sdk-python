from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.webhook_event_payload_payload_object import (
        WebhookEventPayloadPayloadObject,
    )


T = TypeVar("T", bound="WebhookEventPayloadPayload")


@_attrs_define
class WebhookEventPayloadPayload:
    """Conteúdo do evento; `object` é o recurso relacionado (campos variam por `type`).

    Attributes:
        object_ (WebhookEventPayloadPayloadObject): Recurso associado ao evento.
    """

    object_: WebhookEventPayloadPayloadObject

    def to_dict(self) -> dict[str, Any]:
        object_ = self.object_.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "object": object_,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.webhook_event_payload_payload_object import (
            WebhookEventPayloadPayloadObject,
        )

        d = dict(src_dict)
        object_ = WebhookEventPayloadPayloadObject.from_dict(d.pop("object"))

        webhook_event_payload_payload = cls(
            object_=object_,
        )

        return webhook_event_payload_payload
