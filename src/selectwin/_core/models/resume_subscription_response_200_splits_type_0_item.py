from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

T = TypeVar("T", bound="ResumeSubscriptionResponse200SplitsType0Item")


@_attrs_define
class ResumeSubscriptionResponse200SplitsType0Item:
    """
    Attributes:
        id (str): Public identifier (ssp_/split_…)
        recipient (None | str):
        type_ (str):
        value (float):
        charge_processing_fee (bool):
        liable (bool):
        updated_at (str):
        created_at (str):
    """

    id: str
    recipient: None | str
    type_: str
    value: float
    charge_processing_fee: bool
    liable: bool
    updated_at: str
    created_at: str

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        recipient: None | str
        recipient = self.recipient

        type_ = self.type_

        value = self.value

        charge_processing_fee = self.charge_processing_fee

        liable = self.liable

        updated_at = self.updated_at

        created_at = self.created_at

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "id": id,
                "recipient": recipient,
                "type": type_,
                "value": value,
                "chargeProcessingFee": charge_processing_fee,
                "liable": liable,
                "updatedAt": updated_at,
                "createdAt": created_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        def _parse_recipient(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        recipient = _parse_recipient(d.pop("recipient"))

        type_ = d.pop("type")

        value = d.pop("value")

        charge_processing_fee = d.pop("chargeProcessingFee")

        liable = d.pop("liable")

        updated_at = d.pop("updatedAt")

        created_at = d.pop("createdAt")

        resume_subscription_response_200_splits_type_0_item = cls(
            id=id,
            recipient=recipient,
            type_=type_,
            value=value,
            charge_processing_fee=charge_processing_fee,
            liable=liable,
            updated_at=updated_at,
            created_at=created_at,
        )

        return resume_subscription_response_200_splits_type_0_item
