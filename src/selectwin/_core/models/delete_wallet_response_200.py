from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.delete_wallet_response_200_links import DeleteWalletResponse200Links
    from ..models.delete_wallet_response_200_merchant import (
        DeleteWalletResponse200Merchant,
    )


T = TypeVar("T", bound="DeleteWalletResponse200")


@_attrs_define
class DeleteWalletResponse200:
    """
    Attributes:
        id (str):
        resource (str):
        deleted (bool):
        merchant (DeleteWalletResponse200Merchant | Unset):
        field_links (DeleteWalletResponse200Links | Unset):
    """

    id: str
    resource: str
    deleted: bool
    merchant: DeleteWalletResponse200Merchant | Unset = UNSET
    field_links: DeleteWalletResponse200Links | Unset = UNSET

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
        from ..models.delete_wallet_response_200_links import (
            DeleteWalletResponse200Links,
        )
        from ..models.delete_wallet_response_200_merchant import (
            DeleteWalletResponse200Merchant,
        )

        d = dict(src_dict)
        id = d.pop("id")

        resource = d.pop("resource")

        deleted = d.pop("deleted")

        _merchant = d.pop("merchant", UNSET)
        merchant: DeleteWalletResponse200Merchant | Unset
        if isinstance(_merchant, Unset):
            merchant = UNSET
        else:
            merchant = DeleteWalletResponse200Merchant.from_dict(_merchant)

        _field_links = d.pop("_links", UNSET)
        field_links: DeleteWalletResponse200Links | Unset
        if isinstance(_field_links, Unset):
            field_links = UNSET
        else:
            field_links = DeleteWalletResponse200Links.from_dict(_field_links)

        delete_wallet_response_200 = cls(
            id=id,
            resource=resource,
            deleted=deleted,
            merchant=merchant,
            field_links=field_links,
        )

        return delete_wallet_response_200
