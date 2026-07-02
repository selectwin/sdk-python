from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..models.submit_transaction_dispute_body_documents_item_type import (
    SubmitTransactionDisputeBodyDocumentsItemType,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.submit_transaction_dispute_body_documents_item_authentication import (
        SubmitTransactionDisputeBodyDocumentsItemAuthentication,
    )


T = TypeVar("T", bound="SubmitTransactionDisputeBodyDocumentsItem")


@_attrs_define
class SubmitTransactionDisputeBodyDocumentsItem:
    """
    Attributes:
        type_ (SubmitTransactionDisputeBodyDocumentsItemType):
        asset_url (str):
        description (str | Unset):
        shipping_date (str | Unset):
        tracking_code (str | Unset):
        carrier (str | Unset):
        authentication (SubmitTransactionDisputeBodyDocumentsItemAuthentication | Unset):
    """

    type_: SubmitTransactionDisputeBodyDocumentsItemType
    asset_url: str
    description: str | Unset = UNSET
    shipping_date: str | Unset = UNSET
    tracking_code: str | Unset = UNSET
    carrier: str | Unset = UNSET
    authentication: SubmitTransactionDisputeBodyDocumentsItemAuthentication | Unset = (
        UNSET
    )

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_.value

        asset_url = self.asset_url

        description = self.description

        shipping_date = self.shipping_date

        tracking_code = self.tracking_code

        carrier = self.carrier

        authentication: dict[str, Any] | Unset = UNSET
        if not isinstance(self.authentication, Unset):
            authentication = self.authentication.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "type": type_,
                "assetUrl": asset_url,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if shipping_date is not UNSET:
            field_dict["shippingDate"] = shipping_date
        if tracking_code is not UNSET:
            field_dict["trackingCode"] = tracking_code
        if carrier is not UNSET:
            field_dict["carrier"] = carrier
        if authentication is not UNSET:
            field_dict["authentication"] = authentication

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.submit_transaction_dispute_body_documents_item_authentication import (
            SubmitTransactionDisputeBodyDocumentsItemAuthentication,
        )

        d = dict(src_dict)
        type_ = SubmitTransactionDisputeBodyDocumentsItemType(d.pop("type"))

        asset_url = d.pop("assetUrl")

        description = d.pop("description", UNSET)

        shipping_date = d.pop("shippingDate", UNSET)

        tracking_code = d.pop("trackingCode", UNSET)

        carrier = d.pop("carrier", UNSET)

        _authentication = d.pop("authentication", UNSET)
        authentication: SubmitTransactionDisputeBodyDocumentsItemAuthentication | Unset
        if isinstance(_authentication, Unset):
            authentication = UNSET
        else:
            authentication = (
                SubmitTransactionDisputeBodyDocumentsItemAuthentication.from_dict(
                    _authentication
                )
            )

        submit_transaction_dispute_body_documents_item = cls(
            type_=type_,
            asset_url=asset_url,
            description=description,
            shipping_date=shipping_date,
            tracking_code=tracking_code,
            carrier=carrier,
            authentication=authentication,
        )

        return submit_transaction_dispute_body_documents_item
