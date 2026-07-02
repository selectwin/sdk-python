from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

T = TypeVar("T", bound="ListWebhookEndpointsResponse200DataItemMerchant")


@_attrs_define
class ListWebhookEndpointsResponse200DataItemMerchant:
    """
    Attributes:
        name (None | str):
        merchant_id (None | str):
        is_sub_account (bool):
    """

    name: None | str
    merchant_id: None | str
    is_sub_account: bool

    def to_dict(self) -> dict[str, Any]:
        name: None | str
        name = self.name

        merchant_id: None | str
        merchant_id = self.merchant_id

        is_sub_account = self.is_sub_account

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "name": name,
                "merchantId": merchant_id,
                "isSubAccount": is_sub_account,
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

        def _parse_merchant_id(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        merchant_id = _parse_merchant_id(d.pop("merchantId"))

        is_sub_account = d.pop("isSubAccount")

        list_webhook_endpoints_response_200_data_item_merchant = cls(
            name=name,
            merchant_id=merchant_id,
            is_sub_account=is_sub_account,
        )

        return list_webhook_endpoints_response_200_data_item_merchant
