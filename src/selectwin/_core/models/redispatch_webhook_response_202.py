from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="RedispatchWebhookResponse202")


@_attrs_define
class RedispatchWebhookResponse202:
    """
    Attributes:
        accepted (bool):
        id (str):
    """

    accepted: bool
    id: str

    def to_dict(self) -> dict[str, Any]:
        accepted = self.accepted

        id = self.id

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "accepted": accepted,
                "id": id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        accepted = d.pop("accepted")

        id = d.pop("id")

        redispatch_webhook_response_202 = cls(
            accepted=accepted,
            id=id,
        )

        return redispatch_webhook_response_202
