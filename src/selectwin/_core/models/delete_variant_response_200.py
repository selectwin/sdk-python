from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..models.delete_variant_response_200_resource import (
    DeleteVariantResponse200Resource,
)

T = TypeVar("T", bound="DeleteVariantResponse200")


@_attrs_define
class DeleteVariantResponse200:
    """
    Attributes:
        id (str): Public identifier (var_/prv_…)
        resource (DeleteVariantResponse200Resource):
        deleted (bool):
    """

    id: str
    resource: DeleteVariantResponse200Resource
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

        resource = DeleteVariantResponse200Resource(d.pop("resource"))

        deleted = d.pop("deleted")

        delete_variant_response_200 = cls(
            id=id,
            resource=resource,
            deleted=deleted,
        )

        return delete_variant_response_200
