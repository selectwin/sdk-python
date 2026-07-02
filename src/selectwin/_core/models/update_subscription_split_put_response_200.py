from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.update_subscription_split_put_response_200_links import (
        UpdateSubscriptionSplitPutResponse200Links,
    )
    from ..models.update_subscription_split_put_response_200_merchant import (
        UpdateSubscriptionSplitPutResponse200Merchant,
    )


T = TypeVar("T", bound="UpdateSubscriptionSplitPutResponse200")


@_attrs_define
class UpdateSubscriptionSplitPutResponse200:
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
        merchant (UpdateSubscriptionSplitPutResponse200Merchant | Unset):
        field_links (UpdateSubscriptionSplitPutResponse200Links | Unset):
    """

    id: str
    recipient: None | str
    type_: str
    value: float
    charge_processing_fee: bool
    liable: bool
    updated_at: str
    created_at: str
    merchant: UpdateSubscriptionSplitPutResponse200Merchant | Unset = UNSET
    field_links: UpdateSubscriptionSplitPutResponse200Links | Unset = UNSET

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
                "recipient": recipient,
                "type": type_,
                "value": value,
                "chargeProcessingFee": charge_processing_fee,
                "liable": liable,
                "updatedAt": updated_at,
                "createdAt": created_at,
            }
        )
        if merchant is not UNSET:
            field_dict["merchant"] = merchant
        if field_links is not UNSET:
            field_dict["_links"] = field_links

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.update_subscription_split_put_response_200_links import (
            UpdateSubscriptionSplitPutResponse200Links,
        )
        from ..models.update_subscription_split_put_response_200_merchant import (
            UpdateSubscriptionSplitPutResponse200Merchant,
        )

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

        _merchant = d.pop("merchant", UNSET)
        merchant: UpdateSubscriptionSplitPutResponse200Merchant | Unset
        if isinstance(_merchant, Unset):
            merchant = UNSET
        else:
            merchant = UpdateSubscriptionSplitPutResponse200Merchant.from_dict(
                _merchant
            )

        _field_links = d.pop("_links", UNSET)
        field_links: UpdateSubscriptionSplitPutResponse200Links | Unset
        if isinstance(_field_links, Unset):
            field_links = UNSET
        else:
            field_links = UpdateSubscriptionSplitPutResponse200Links.from_dict(
                _field_links
            )

        update_subscription_split_put_response_200 = cls(
            id=id,
            recipient=recipient,
            type_=type_,
            value=value,
            charge_processing_fee=charge_processing_fee,
            liable=liable,
            updated_at=updated_at,
            created_at=created_at,
            merchant=merchant,
            field_links=field_links,
        )

        return update_subscription_split_put_response_200
