from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..models.refund_transaction_response_202_status import (
    RefundTransactionResponse202Status,
)

T = TypeVar("T", bound="RefundTransactionResponse202")


@_attrs_define
class RefundTransactionResponse202:
    """
    Attributes:
        transaction_id (str): Public identifier (tra_/trx_…)
        status (RefundTransactionResponse202Status):
        accepted (bool):
    """

    transaction_id: str
    status: RefundTransactionResponse202Status
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

        status = RefundTransactionResponse202Status(d.pop("status"))

        accepted = d.pop("accepted")

        refund_transaction_response_202 = cls(
            transaction_id=transaction_id,
            status=status,
            accepted=accepted,
        )

        return refund_transaction_response_202
