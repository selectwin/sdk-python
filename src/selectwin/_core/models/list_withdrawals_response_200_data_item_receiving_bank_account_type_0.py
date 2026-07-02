from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

T = TypeVar("T", bound="ListWithdrawalsResponse200DataItemReceivingBankAccountType0")


@_attrs_define
class ListWithdrawalsResponse200DataItemReceivingBankAccountType0:
    """
    Attributes:
        holder_name (None | str):
        document (None | str):
        bank_code (None | str):
        bank_name (None | str):
        routing_number (None | str):
        account_number (None | str):
        type_ (None | str):
        pix_key (None | str):
    """

    holder_name: None | str
    document: None | str
    bank_code: None | str
    bank_name: None | str
    routing_number: None | str
    account_number: None | str
    type_: None | str
    pix_key: None | str

    def to_dict(self) -> dict[str, Any]:
        holder_name: None | str
        holder_name = self.holder_name

        document: None | str
        document = self.document

        bank_code: None | str
        bank_code = self.bank_code

        bank_name: None | str
        bank_name = self.bank_name

        routing_number: None | str
        routing_number = self.routing_number

        account_number: None | str
        account_number = self.account_number

        type_: None | str
        type_ = self.type_

        pix_key: None | str
        pix_key = self.pix_key

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "holderName": holder_name,
                "document": document,
                "bankCode": bank_code,
                "bankName": bank_name,
                "routingNumber": routing_number,
                "accountNumber": account_number,
                "type": type_,
                "pixKey": pix_key,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_holder_name(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        holder_name = _parse_holder_name(d.pop("holderName"))

        def _parse_document(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        document = _parse_document(d.pop("document"))

        def _parse_bank_code(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        bank_code = _parse_bank_code(d.pop("bankCode"))

        def _parse_bank_name(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        bank_name = _parse_bank_name(d.pop("bankName"))

        def _parse_routing_number(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        routing_number = _parse_routing_number(d.pop("routingNumber"))

        def _parse_account_number(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        account_number = _parse_account_number(d.pop("accountNumber"))

        def _parse_type_(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        type_ = _parse_type_(d.pop("type"))

        def _parse_pix_key(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        pix_key = _parse_pix_key(d.pop("pixKey"))

        list_withdrawals_response_200_data_item_receiving_bank_account_type_0 = cls(
            holder_name=holder_name,
            document=document,
            bank_code=bank_code,
            bank_name=bank_name,
            routing_number=routing_number,
            account_number=account_number,
            type_=type_,
            pix_key=pix_key,
        )

        return list_withdrawals_response_200_data_item_receiving_bank_account_type_0
