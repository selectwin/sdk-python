from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.create_withdrawal_response_201_links import (
        CreateWithdrawalResponse201Links,
    )
    from ..models.create_withdrawal_response_201_merchant import (
        CreateWithdrawalResponse201Merchant,
    )
    from ..models.create_withdrawal_response_201_receiving_bank_account_type_0 import (
        CreateWithdrawalResponse201ReceivingBankAccountType0,
    )


T = TypeVar("T", bound="CreateWithdrawalResponse201")


@_attrs_define
class CreateWithdrawalResponse201:
    """
    Attributes:
        id (str): Public identifier (cash_…)
        wallet_id (None | str): Public identifier (wall_…)
        amount (int):
        fee (int):
        status (str):
        method (None | str):
        currency (str):
        transfer_code (None | str):
        paid_at (None | str):
        approved_at (None | str):
        created_at (str):
        updated_at (str):
        receiving_bank_account (CreateWithdrawalResponse201ReceivingBankAccountType0 | None | Unset):
        merchant (CreateWithdrawalResponse201Merchant | Unset):
        field_links (CreateWithdrawalResponse201Links | Unset):
    """

    id: str
    wallet_id: None | str
    amount: int
    fee: int
    status: str
    method: None | str
    currency: str
    transfer_code: None | str
    paid_at: None | str
    approved_at: None | str
    created_at: str
    updated_at: str
    receiving_bank_account: (
        CreateWithdrawalResponse201ReceivingBankAccountType0 | None | Unset
    ) = UNSET
    merchant: CreateWithdrawalResponse201Merchant | Unset = UNSET
    field_links: CreateWithdrawalResponse201Links | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.create_withdrawal_response_201_receiving_bank_account_type_0 import (
            CreateWithdrawalResponse201ReceivingBankAccountType0,
        )

        id = self.id

        wallet_id: None | str
        wallet_id = self.wallet_id

        amount = self.amount

        fee = self.fee

        status = self.status

        method: None | str
        method = self.method

        currency = self.currency

        transfer_code: None | str
        transfer_code = self.transfer_code

        paid_at: None | str
        paid_at = self.paid_at

        approved_at: None | str
        approved_at = self.approved_at

        created_at = self.created_at

        updated_at = self.updated_at

        receiving_bank_account: dict[str, Any] | None | Unset
        if isinstance(self.receiving_bank_account, Unset):
            receiving_bank_account = UNSET
        elif isinstance(
            self.receiving_bank_account,
            CreateWithdrawalResponse201ReceivingBankAccountType0,
        ):
            receiving_bank_account = self.receiving_bank_account.to_dict()
        else:
            receiving_bank_account = self.receiving_bank_account

        merchant: dict[str, Any] | Unset = UNSET
        if not isinstance(self.merchant, Unset):
            merchant = self.merchant.to_dict()

        field_links: dict[str, Any] | Unset = UNSET
        if not isinstance(self.field_links, Unset):
            field_links = self.field_links.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "id": id,
                "walletId": wallet_id,
                "amount": amount,
                "fee": fee,
                "status": status,
                "method": method,
                "currency": currency,
                "transferCode": transfer_code,
                "paidAt": paid_at,
                "approvedAt": approved_at,
                "createdAt": created_at,
                "updatedAt": updated_at,
            }
        )
        if receiving_bank_account is not UNSET:
            field_dict["receivingBankAccount"] = receiving_bank_account
        if merchant is not UNSET:
            field_dict["merchant"] = merchant
        if field_links is not UNSET:
            field_dict["_links"] = field_links

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.create_withdrawal_response_201_links import (
            CreateWithdrawalResponse201Links,
        )
        from ..models.create_withdrawal_response_201_merchant import (
            CreateWithdrawalResponse201Merchant,
        )
        from ..models.create_withdrawal_response_201_receiving_bank_account_type_0 import (
            CreateWithdrawalResponse201ReceivingBankAccountType0,
        )

        d = dict(src_dict)
        id = d.pop("id")

        def _parse_wallet_id(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        wallet_id = _parse_wallet_id(d.pop("walletId"))

        amount = d.pop("amount")

        fee = d.pop("fee")

        status = d.pop("status")

        def _parse_method(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        method = _parse_method(d.pop("method"))

        currency = d.pop("currency")

        def _parse_transfer_code(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        transfer_code = _parse_transfer_code(d.pop("transferCode"))

        def _parse_paid_at(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        paid_at = _parse_paid_at(d.pop("paidAt"))

        def _parse_approved_at(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        approved_at = _parse_approved_at(d.pop("approvedAt"))

        created_at = d.pop("createdAt")

        updated_at = d.pop("updatedAt")

        def _parse_receiving_bank_account(
            data: object,
        ) -> CreateWithdrawalResponse201ReceivingBankAccountType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                receiving_bank_account_type_0 = (
                    CreateWithdrawalResponse201ReceivingBankAccountType0.from_dict(data)
                )

                return receiving_bank_account_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                CreateWithdrawalResponse201ReceivingBankAccountType0 | None | Unset,
                data,
            )

        receiving_bank_account = _parse_receiving_bank_account(
            d.pop("receivingBankAccount", UNSET)
        )

        _merchant = d.pop("merchant", UNSET)
        merchant: CreateWithdrawalResponse201Merchant | Unset
        if isinstance(_merchant, Unset):
            merchant = UNSET
        else:
            merchant = CreateWithdrawalResponse201Merchant.from_dict(_merchant)

        _field_links = d.pop("_links", UNSET)
        field_links: CreateWithdrawalResponse201Links | Unset
        if isinstance(_field_links, Unset):
            field_links = UNSET
        else:
            field_links = CreateWithdrawalResponse201Links.from_dict(_field_links)

        create_withdrawal_response_201 = cls(
            id=id,
            wallet_id=wallet_id,
            amount=amount,
            fee=fee,
            status=status,
            method=method,
            currency=currency,
            transfer_code=transfer_code,
            paid_at=paid_at,
            approved_at=approved_at,
            created_at=created_at,
            updated_at=updated_at,
            receiving_bank_account=receiving_bank_account,
            merchant=merchant,
            field_links=field_links,
        )

        return create_withdrawal_response_201
