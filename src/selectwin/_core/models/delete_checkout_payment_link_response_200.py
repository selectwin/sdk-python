from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..models.delete_checkout_payment_link_response_200_resource import (
    DeleteCheckoutPaymentLinkResponse200Resource,
)

T = TypeVar("T", bound="DeleteCheckoutPaymentLinkResponse200")


@_attrs_define
class DeleteCheckoutPaymentLinkResponse200:
    """
    Attributes:
        id (str): Public identifier (link_…)
        resource (DeleteCheckoutPaymentLinkResponse200Resource):
        deleted (bool):
    """

    id: str
    resource: DeleteCheckoutPaymentLinkResponse200Resource
    deleted: bool

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        resource = self.resource.value

        deleted = self.deleted

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "id": id,
                "resource": resource,
                "deleted": deleted,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        resource = DeleteCheckoutPaymentLinkResponse200Resource(d.pop("resource"))

        deleted = d.pop("deleted")

        delete_checkout_payment_link_response_200 = cls(
            id=id,
            resource=resource,
            deleted=deleted,
        )

        return delete_checkout_payment_link_response_200
