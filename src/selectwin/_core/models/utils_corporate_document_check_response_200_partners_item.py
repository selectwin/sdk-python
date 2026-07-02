from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

T = TypeVar("T", bound="UtilsCorporateDocumentCheckResponse200PartnersItem")


@_attrs_define
class UtilsCorporateDocumentCheckResponse200PartnersItem:
    """
    Attributes:
        name (None | str):
        qualification (None | str):
        since (None | str):
    """

    name: None | str
    qualification: None | str
    since: None | str

    def to_dict(self) -> dict[str, Any]:
        name: None | str
        name = self.name

        qualification: None | str
        qualification = self.qualification

        since: None | str
        since = self.since

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "name": name,
                "qualification": qualification,
                "since": since,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_name(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        name = _parse_name(d.pop("name"))

        def _parse_qualification(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        qualification = _parse_qualification(d.pop("qualification"))

        def _parse_since(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        since = _parse_since(d.pop("since"))

        utils_corporate_document_check_response_200_partners_item = cls(
            name=name,
            qualification=qualification,
            since=since,
        )

        return utils_corporate_document_check_response_200_partners_item
