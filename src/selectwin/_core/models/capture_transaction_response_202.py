from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..models.capture_transaction_response_202_status import (
    CaptureTransactionResponse202Status,
)

T = TypeVar("T", bound="CaptureTransactionResponse202")


@_attrs_define
class CaptureTransactionResponse202:
    """
    Attributes:
        transaction_id (str): Public identifier (tra_/trx_…)
        status (CaptureTransactionResponse202Status):
        accepted (bool):
    """

    transaction_id: str
    status: CaptureTransactionResponse202Status
    accepted: bool

    def to_dict(self) -> dict[str, Any]:
        transaction_id = self.transaction_id

        status = self.status.value

        accepted = self.accepted

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "transactionId": transaction_id,
                "status": status,
                "accepted": accepted,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        transaction_id = d.pop("transactionId")

        status = CaptureTransactionResponse202Status(d.pop("status"))

        accepted = d.pop("accepted")

        capture_transaction_response_202 = cls(
            transaction_id=transaction_id,
            status=status,
            accepted=accepted,
        )

        return capture_transaction_response_202
