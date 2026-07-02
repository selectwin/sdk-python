from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.utils_company_types_response_200_data_item import (
        UtilsCompanyTypesResponse200DataItem,
    )


T = TypeVar("T", bound="UtilsCompanyTypesResponse200")


@_attrs_define
class UtilsCompanyTypesResponse200:
    """
    Attributes:
        data (list[UtilsCompanyTypesResponse200DataItem]):
    """

    data: list[UtilsCompanyTypesResponse200DataItem]

    def to_dict(self) -> dict[str, Any]:
        data = []
        for data_item_data in self.data:
            data_item = data_item_data.to_dict()
            data.append(data_item)

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "data": data,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.utils_company_types_response_200_data_item import (
            UtilsCompanyTypesResponse200DataItem,
        )

        d = dict(src_dict)
        data = []
        _data = d.pop("data")
        for data_item_data in _data:
            data_item = UtilsCompanyTypesResponse200DataItem.from_dict(data_item_data)

            data.append(data_item)

        utils_company_types_response_200 = cls(
            data=data,
        )

        return utils_company_types_response_200
