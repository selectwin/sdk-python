from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

T = TypeVar("T", bound="UtilsCorporateDocumentCheckResponse200SecondaryCnaesItem")


@_attrs_define
class UtilsCorporateDocumentCheckResponse200SecondaryCnaesItem:
    """
    Attributes:
        code (None | str):
        description (None | str):
    """

    code: None | str
    description: None | str

    def to_dict(self) -> dict[str, Any]:
        code: None | str
        code = self.code

        description: None | str
        description = self.description

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "code": code,
                "description": description,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_code(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        code = _parse_code(d.pop("code"))

        def _parse_description(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        description = _parse_description(d.pop("description"))

        utils_corporate_document_check_response_200_secondary_cnaes_item = cls(
            code=code,
            description=description,
        )

        return utils_corporate_document_check_response_200_secondary_cnaes_item
