from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.webhook_event_payload_payload import WebhookEventPayloadPayload


T = TypeVar("T", bound="WebhookEventPayload")


@_attrs_define
class WebhookEventPayload:
    """Envelope do evento entregue à sua URL. A forma de `payload.object` depende de `type` (ex.: `transaction.approved`).

    Example:
        {'id': 'wbh_758c47e09f43c6d99cfe', 'type': 'transaction.approved', 'source': 'webhook', 'payload': {'object':
            {'id': 'tra_0a1b2c3d4e5f60718293', 'status': 'approved'}}, 'createdAt': '2026-01-15T12:00:00.000Z', 'updatedAt':
            '2026-01-15T12:00:00.000Z', 'correlationId': 'cor_1776016593'}

    Attributes:
        id (str): Identificador público do evento. Example: wbh_758c47e09f43c6d99cfe.
        type_ (str): Tipo no formato `recurso.acao`. Example: transaction.approved.
        source (str): Origem do evento na plataforma. Example: webhook.
        payload (WebhookEventPayloadPayload): Conteúdo do evento; `object` é o recurso relacionado (campos variam por
            `type`).
        created_at (datetime.datetime): Criação do evento (UTC, ISO 8601). Example: 2026-01-15T12:00:00.000Z.
        updated_at (datetime.datetime): Última atualização (UTC, ISO 8601). Example: 2026-01-15T12:00:00.000Z.
        correlation_id (str): Identificador para correlacionar logs/suporte. Example: cor_1776016593.
    """

    id: str
    type_: str
    source: str
    payload: WebhookEventPayloadPayload
    created_at: datetime.datetime
    updated_at: datetime.datetime
    correlation_id: str

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        type_ = self.type_

        source = self.source

        payload = self.payload.to_dict()

        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        correlation_id = self.correlation_id

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "id": id,
                "type": type_,
                "source": source,
                "payload": payload,
                "createdAt": created_at,
                "updatedAt": updated_at,
                "correlationId": correlation_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.webhook_event_payload_payload import WebhookEventPayloadPayload

        d = dict(src_dict)
        id = d.pop("id")

        type_ = d.pop("type")

        source = d.pop("source")

        payload = WebhookEventPayloadPayload.from_dict(d.pop("payload"))

        created_at = datetime.datetime.fromisoformat(d.pop("createdAt"))

        updated_at = datetime.datetime.fromisoformat(d.pop("updatedAt"))

        correlation_id = d.pop("correlationId")

        webhook_event_payload = cls(
            id=id,
            type_=type_,
            source=source,
            payload=payload,
            created_at=created_at,
            updated_at=updated_at,
            correlation_id=correlation_id,
        )

        return webhook_event_payload
