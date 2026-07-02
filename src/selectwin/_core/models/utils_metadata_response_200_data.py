from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

T = TypeVar("T", bound="UtilsMetadataResponse200Data")


@_attrs_define
class UtilsMetadataResponse200Data:
    """
    Attributes:
        api_version (str):
        currencies (list[str]):
        payment_methods (list[str]):
        document_types (list[str]):
    """

    api_version: str
    currencies: list[str]
    payment_methods: list[str]
    document_types: list[str]

    def to_dict(self) -> dict[str, Any]:
        api_version = self.api_version

        currencies = self.currencies

        payment_methods = self.payment_methods

        document_types = self.document_types

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "apiVersion": api_version,
                "currencies": currencies,
                "paymentMethods": payment_methods,
                "documentTypes": document_types,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        api_version = d.pop("apiVersion")

        currencies = cast(list[str], d.pop("currencies"))

        payment_methods = cast(list[str], d.pop("paymentMethods"))

        document_types = cast(list[str], d.pop("documentTypes"))

        utils_metadata_response_200_data = cls(
            api_version=api_version,
            currencies=currencies,
            payment_methods=payment_methods,
            document_types=document_types,
        )

        return utils_metadata_response_200_data
