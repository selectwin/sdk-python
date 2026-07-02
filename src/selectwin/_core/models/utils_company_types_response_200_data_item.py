from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

T = TypeVar("T", bound="UtilsCompanyTypesResponse200DataItem")


@_attrs_define
class UtilsCompanyTypesResponse200DataItem:
    """
    Attributes:
        category_id (int):
        mcc (None | str):
        code (None | str):
        name (None | str):
        description (None | str):
    """

    category_id: int
    mcc: None | str
    code: None | str
    name: None | str
    description: None | str

    def to_dict(self) -> dict[str, Any]:
        category_id = self.category_id

        mcc: None | str
        mcc = self.mcc

        code: None | str
        code = self.code

        name: None | str
        name = self.name

        description: None | str
        description = self.description

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "categoryId": category_id,
                "mcc": mcc,
                "code": code,
                "name": name,
                "description": description,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        category_id = d.pop("categoryId")

        def _parse_mcc(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        mcc = _parse_mcc(d.pop("mcc"))

        def _parse_code(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        code = _parse_code(d.pop("code"))

        def _parse_name(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        name = _parse_name(d.pop("name"))

        def _parse_description(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        description = _parse_description(d.pop("description"))

        utils_company_types_response_200_data_item = cls(
            category_id=category_id,
            mcc=mcc,
            code=code,
            name=name,
            description=description,
        )

        return utils_company_types_response_200_data_item
