from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.submit_transaction_dispute_body_documents_item import (
        SubmitTransactionDisputeBodyDocumentsItem,
    )


T = TypeVar("T", bound="SubmitTransactionDisputeBody")


@_attrs_define
class SubmitTransactionDisputeBody:
    """
    Attributes:
        documents (list[SubmitTransactionDisputeBodyDocumentsItem]):
        description (str | Unset):
        return_email (str | Unset):
    """

    documents: list[SubmitTransactionDisputeBodyDocumentsItem]
    description: str | Unset = UNSET
    return_email: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        documents = []
        for documents_item_data in self.documents:
            documents_item = documents_item_data.to_dict()
            documents.append(documents_item)

        description = self.description

        return_email = self.return_email

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "documents": documents,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if return_email is not UNSET:
            field_dict["returnEmail"] = return_email

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.submit_transaction_dispute_body_documents_item import (
            SubmitTransactionDisputeBodyDocumentsItem,
        )

        d = dict(src_dict)
        documents = []
        _documents = d.pop("documents")
        for documents_item_data in _documents:
            documents_item = SubmitTransactionDisputeBodyDocumentsItem.from_dict(
                documents_item_data
            )

            documents.append(documents_item)

        description = d.pop("description", UNSET)

        return_email = d.pop("returnEmail", UNSET)

        submit_transaction_dispute_body = cls(
            documents=documents,
            description=description,
            return_email=return_email,
        )

        return submit_transaction_dispute_body
