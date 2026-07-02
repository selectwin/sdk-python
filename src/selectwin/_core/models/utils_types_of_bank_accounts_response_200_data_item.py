from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

T = TypeVar("T", bound="UtilsTypesOfBankAccountsResponse200DataItem")


@_attrs_define
class UtilsTypesOfBankAccountsResponse200DataItem:
    """
    Attributes:
        bank_id (int):
        bank_code (None | str):
        name (None | str):
    """

    bank_id: int
    bank_code: None | str
    name: None | str

    def to_dict(self) -> dict[str, Any]:
        bank_id = self.bank_id

        bank_code: None | str
        bank_code = self.bank_code

        name: None | str
        name = self.name

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "bankId": bank_id,
                "bankCode": bank_code,
                "name": name,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        bank_id = d.pop("bankId")

        def _parse_bank_code(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        bank_code = _parse_bank_code(d.pop("bankCode"))

        def _parse_name(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        name = _parse_name(d.pop("name"))

        utils_types_of_bank_accounts_response_200_data_item = cls(
            bank_id=bank_id,
            bank_code=bank_code,
            name=name,
        )

        return utils_types_of_bank_accounts_response_200_data_item
