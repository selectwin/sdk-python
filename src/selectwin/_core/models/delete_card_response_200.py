from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.delete_card_response_200_links import DeleteCardResponse200Links
    from ..models.delete_card_response_200_merchant import DeleteCardResponse200Merchant


T = TypeVar("T", bound="DeleteCardResponse200")


@_attrs_define
class DeleteCardResponse200:
    """
    Attributes:
        id (str):
        resource (str):
        deleted (bool):
        merchant (DeleteCardResponse200Merchant | Unset):
        field_links (DeleteCardResponse200Links | Unset):
    """

    id: str
    resource: str
    deleted: bool
    merchant: DeleteCardResponse200Merchant | Unset = UNSET
    field_links: DeleteCardResponse200Links | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        resource = self.resource

        deleted = self.deleted

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
                "resource": resource,
                "deleted": deleted,
            }
        )
        if merchant is not UNSET:
            field_dict["merchant"] = merchant
        if field_links is not UNSET:
            field_dict["_links"] = field_links

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.delete_card_response_200_links import DeleteCardResponse200Links
        from ..models.delete_card_response_200_merchant import (
            DeleteCardResponse200Merchant,
        )

        d = dict(src_dict)
        id = d.pop("id")

        resource = d.pop("resource")

        deleted = d.pop("deleted")

        _merchant = d.pop("merchant", UNSET)
        merchant: DeleteCardResponse200Merchant | Unset
        if isinstance(_merchant, Unset):
            merchant = UNSET
        else:
            merchant = DeleteCardResponse200Merchant.from_dict(_merchant)

        _field_links = d.pop("_links", UNSET)
        field_links: DeleteCardResponse200Links | Unset
        if isinstance(_field_links, Unset):
            field_links = UNSET
        else:
            field_links = DeleteCardResponse200Links.from_dict(_field_links)

        delete_card_response_200 = cls(
            id=id,
            resource=resource,
            deleted=deleted,
            merchant=merchant,
            field_links=field_links,
        )

        return delete_card_response_200
