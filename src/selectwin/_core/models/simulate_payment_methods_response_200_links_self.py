from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="SimulatePaymentMethodsResponse200LinksSelf")


@_attrs_define
class SimulatePaymentMethodsResponse200LinksSelf:
    """
    Attributes:
        href (str):
        method (str):
    """

    href: str
    method: str

    def to_dict(self) -> dict[str, Any]:
        href = self.href

        method = self.method

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "href": href,
                "method": method,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        href = d.pop("href")

        method = d.pop("method")

        simulate_payment_methods_response_200_links_self = cls(
            href=href,
            method=method,
        )

        return simulate_payment_methods_response_200_links_self
