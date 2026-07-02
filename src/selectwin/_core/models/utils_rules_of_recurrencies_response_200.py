from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.utils_rules_of_recurrencies_response_200_data import (
        UtilsRulesOfRecurrenciesResponse200Data,
    )


T = TypeVar("T", bound="UtilsRulesOfRecurrenciesResponse200")


@_attrs_define
class UtilsRulesOfRecurrenciesResponse200:
    """
    Attributes:
        data (UtilsRulesOfRecurrenciesResponse200Data):
    """

    data: UtilsRulesOfRecurrenciesResponse200Data

    def to_dict(self) -> dict[str, Any]:
        data = self.data.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "data": data,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.utils_rules_of_recurrencies_response_200_data import (
            UtilsRulesOfRecurrenciesResponse200Data,
        )

        d = dict(src_dict)
        data = UtilsRulesOfRecurrenciesResponse200Data.from_dict(d.pop("data"))

        utils_rules_of_recurrencies_response_200 = cls(
            data=data,
        )

        return utils_rules_of_recurrencies_response_200
