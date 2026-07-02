from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

T = TypeVar("T", bound="GetCustomerResponse200SubscriptionsItemCustomerTelephoneType0")


@_attrs_define
class GetCustomerResponse200SubscriptionsItemCustomerTelephoneType0:
    """
    Attributes:
        country_code (None | str):
        area_code (None | str):
        number (None | str):
        line (None | str):
    """

    country_code: None | str
    area_code: None | str
    number: None | str
    line: None | str

    def to_dict(self) -> dict[str, Any]:
        country_code: None | str
        country_code = self.country_code

        area_code: None | str
        area_code = self.area_code

        number: None | str
        number = self.number

        line: None | str
        line = self.line

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "countryCode": country_code,
                "areaCode": area_code,
                "number": number,
                "line": line,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_country_code(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        country_code = _parse_country_code(d.pop("countryCode"))

        def _parse_area_code(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        area_code = _parse_area_code(d.pop("areaCode"))

        def _parse_number(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        number = _parse_number(d.pop("number"))

        def _parse_line(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        line = _parse_line(d.pop("line"))

        get_customer_response_200_subscriptions_item_customer_telephone_type_0 = cls(
            country_code=country_code,
            area_code=area_code,
            number=number,
            line=line,
        )

        return get_customer_response_200_subscriptions_item_customer_telephone_type_0
