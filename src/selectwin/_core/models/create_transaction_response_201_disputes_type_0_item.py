from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateTransactionResponse201DisputesType0Item")


@_attrs_define
class CreateTransactionResponse201DisputesType0Item:
    """
    Attributes:
        id (None | str):
        return_email (None | str):
        description (None | str):
        updated_at (None | str):
        created_at (None | str):
        delivery_proof (Any | Unset):
        shipment_proof (Any | Unset):
        delivery_receipts (Any | Unset):
        fiscal_documents (Any | Unset):
        communication_proof (Any | Unset):
    """

    id: None | str
    return_email: None | str
    description: None | str
    updated_at: None | str
    created_at: None | str
    delivery_proof: Any | Unset = UNSET
    shipment_proof: Any | Unset = UNSET
    delivery_receipts: Any | Unset = UNSET
    fiscal_documents: Any | Unset = UNSET
    communication_proof: Any | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        id: None | str
        id = self.id

        return_email: None | str
        return_email = self.return_email

        description: None | str
        description = self.description

        updated_at: None | str
        updated_at = self.updated_at

        created_at: None | str
        created_at = self.created_at

        delivery_proof = self.delivery_proof

        shipment_proof = self.shipment_proof

        delivery_receipts = self.delivery_receipts

        fiscal_documents = self.fiscal_documents

        communication_proof = self.communication_proof

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "id": id,
                "returnEmail": return_email,
                "description": description,
                "updatedAt": updated_at,
                "createdAt": created_at,
            }
        )
        if delivery_proof is not UNSET:
            field_dict["deliveryProof"] = delivery_proof
        if shipment_proof is not UNSET:
            field_dict["shipmentProof"] = shipment_proof
        if delivery_receipts is not UNSET:
            field_dict["deliveryReceipts"] = delivery_receipts
        if fiscal_documents is not UNSET:
            field_dict["fiscalDocuments"] = fiscal_documents
        if communication_proof is not UNSET:
            field_dict["communicationProof"] = communication_proof

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_id(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        id = _parse_id(d.pop("id"))

        def _parse_return_email(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        return_email = _parse_return_email(d.pop("returnEmail"))

        def _parse_description(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        description = _parse_description(d.pop("description"))

        def _parse_updated_at(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        updated_at = _parse_updated_at(d.pop("updatedAt"))

        def _parse_created_at(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        created_at = _parse_created_at(d.pop("createdAt"))

        delivery_proof = d.pop("deliveryProof", UNSET)

        shipment_proof = d.pop("shipmentProof", UNSET)

        delivery_receipts = d.pop("deliveryReceipts", UNSET)

        fiscal_documents = d.pop("fiscalDocuments", UNSET)

        communication_proof = d.pop("communicationProof", UNSET)

        create_transaction_response_201_disputes_type_0_item = cls(
            id=id,
            return_email=return_email,
            description=description,
            updated_at=updated_at,
            created_at=created_at,
            delivery_proof=delivery_proof,
            shipment_proof=shipment_proof,
            delivery_receipts=delivery_receipts,
            fiscal_documents=fiscal_documents,
            communication_proof=communication_proof,
        )

        return create_transaction_response_201_disputes_type_0_item
