from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="UtilsRolesOfUserResponse200")


@_attrs_define
class UtilsRolesOfUserResponse200:
    """
    Attributes:
        data (Any | Unset):
    """

    data: Any | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        data = self.data

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if data is not UNSET:
            field_dict["data"] = data

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        data = d.pop("data", UNSET)

        utils_roles_of_user_response_200 = cls(
            data=data,
        )

        return utils_roles_of_user_response_200
