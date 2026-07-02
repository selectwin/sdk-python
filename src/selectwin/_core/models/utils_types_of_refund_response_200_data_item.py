from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

T = TypeVar("T", bound="UtilsTypesOfRefundResponse200DataItem")


@_attrs_define
class UtilsTypesOfRefundResponse200DataItem:
    """
    Attributes:
        category_id (int):
        name (None | str):
    """

    category_id: int
    name: None | str

    def to_dict(self) -> dict[str, Any]:
        category_id = self.category_id

        name: None | str
        name = self.name

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "categoryId": category_id,
                "name": name,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        category_id = d.pop("categoryId")

        def _parse_name(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        name = _parse_name(d.pop("name"))

        utils_types_of_refund_response_200_data_item = cls(
            category_id=category_id,
            name=name,
        )

        return utils_types_of_refund_response_200_data_item
