from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..models.submit_checkout_payment_response_202_status import (
    SubmitCheckoutPaymentResponse202Status,
)

T = TypeVar("T", bound="SubmitCheckoutPaymentResponse202")


@_attrs_define
class SubmitCheckoutPaymentResponse202:
    """
    Attributes:
        job_id (str): Public identifier (payjob_…)
        status (SubmitCheckoutPaymentResponse202Status):
        session_id (str): Public identifier (sess_/ckts_/ses_…)
    """

    job_id: str
    status: SubmitCheckoutPaymentResponse202Status
    session_id: str

    def to_dict(self) -> dict[str, Any]:
        job_id = self.job_id

        status = self.status.value

        session_id = self.session_id

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "jobId": job_id,
                "status": status,
                "sessionId": session_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        job_id = d.pop("jobId")

        status = SubmitCheckoutPaymentResponse202Status(d.pop("status"))

        session_id = d.pop("sessionId")

        submit_checkout_payment_response_202 = cls(
            job_id=job_id,
            status=status,
            session_id=session_id,
        )

        return submit_checkout_payment_response_202
