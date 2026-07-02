from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

T = TypeVar("T", bound="GetCustomerResponse200TransactionsItem")


@_attrs_define
class GetCustomerResponse200TransactionsItem:
    """
    Attributes:
        id (str): Public identifier (tra_/trx_…)
        custom_id (None | str):
        customer_id (None | str): Public identifier (cus_…)
        card_brand (None | str):
        amount (str):
        original_amount (str):
        status (str):
        method (str):
        currency (str):
        fees (int):
        approved_at (None | str):
        updated_at (str):
        created_at (str):
        images (list[str]):
    """

    id: str
    custom_id: None | str
    customer_id: None | str
    card_brand: None | str
    amount: str
    original_amount: str
    status: str
    method: str
    currency: str
    fees: int
    approved_at: None | str
    updated_at: str
    created_at: str
    images: list[str]

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        custom_id: None | str
        custom_id = self.custom_id

        customer_id: None | str
        customer_id = self.customer_id

        card_brand: None | str
        card_brand = self.card_brand

        amount = self.amount

        original_amount = self.original_amount

        status = self.status

        method = self.method

        currency = self.currency

        fees = self.fees

        approved_at: None | str
        approved_at = self.approved_at

        updated_at = self.updated_at

        created_at = self.created_at

        images = self.images

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "id": id,
                "customId": custom_id,
                "customerId": customer_id,
                "cardBrand": card_brand,
                "amount": amount,
                "originalAmount": original_amount,
                "status": status,
                "method": method,
                "currency": currency,
                "fees": fees,
                "approvedAt": approved_at,
                "updatedAt": updated_at,
                "createdAt": created_at,
                "images": images,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        def _parse_custom_id(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        custom_id = _parse_custom_id(d.pop("customId"))

        def _parse_customer_id(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        customer_id = _parse_customer_id(d.pop("customerId"))

        def _parse_card_brand(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        card_brand = _parse_card_brand(d.pop("cardBrand"))

        amount = d.pop("amount")

        original_amount = d.pop("originalAmount")

        status = d.pop("status")

        method = d.pop("method")

        currency = d.pop("currency")

        fees = d.pop("fees")

        def _parse_approved_at(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        approved_at = _parse_approved_at(d.pop("approvedAt"))

        updated_at = d.pop("updatedAt")

        created_at = d.pop("createdAt")

        images = cast(list[str], d.pop("images"))

        get_customer_response_200_transactions_item = cls(
            id=id,
            custom_id=custom_id,
            customer_id=customer_id,
            card_brand=card_brand,
            amount=amount,
            original_amount=original_amount,
            status=status,
            method=method,
            currency=currency,
            fees=fees,
            approved_at=approved_at,
            updated_at=updated_at,
            created_at=created_at,
            images=images,
        )

        return get_customer_response_200_transactions_item
