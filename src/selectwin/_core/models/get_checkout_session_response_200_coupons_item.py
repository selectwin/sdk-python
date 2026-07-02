from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

T = TypeVar("T", bound="GetCheckoutSessionResponse200CouponsItem")


@_attrs_define
class GetCheckoutSessionResponse200CouponsItem:
    """
    Attributes:
        code (None | str):
        type_ (None | str):
        value (float | None):
    """

    code: None | str
    type_: None | str
    value: float | None

    def to_dict(self) -> dict[str, Any]:
        code: None | str
        code = self.code

        type_: None | str
        type_ = self.type_

        value: float | None
        value = self.value

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "code": code,
                "type": type_,
                "value": value,
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

        def _parse_type_(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        type_ = _parse_type_(d.pop("type"))

        def _parse_value(data: object) -> float | None:
            if data is None:
                return data
            return cast(float | None, data)

        value = _parse_value(d.pop("value"))

        get_checkout_session_response_200_coupons_item = cls(
            code=code,
            type_=type_,
            value=value,
        )

        return get_checkout_session_response_200_coupons_item
