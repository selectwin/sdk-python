from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="CreateCheckoutSessionResponse201PaymentSelectionType0")


@_attrs_define
class CreateCheckoutSessionResponse201PaymentSelectionType0:
    """
    Attributes:
        method (str):
    """

    method: str

    def to_dict(self) -> dict[str, Any]:
        method = self.method

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "method": method,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        method = d.pop("method")

        create_checkout_session_response_201_payment_selection_type_0 = cls(
            method=method,
        )

        return create_checkout_session_response_201_payment_selection_type_0
