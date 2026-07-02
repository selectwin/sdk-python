from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.list_balance_history_response_200_data_item_new_balance import (
        ListBalanceHistoryResponse200DataItemNewBalance,
    )
    from ..models.list_balance_history_response_200_data_item_old_balance import (
        ListBalanceHistoryResponse200DataItemOldBalance,
    )


T = TypeVar("T", bound="ListBalanceHistoryResponse200DataItem")


@_attrs_define
class ListBalanceHistoryResponse200DataItem:
    """
    Attributes:
        id (int):
        from_type (None | str):
        to_type (None | str):
        processed_amount (int):
        old_balance (ListBalanceHistoryResponse200DataItemOldBalance):
        new_balance (ListBalanceHistoryResponse200DataItemNewBalance):
        handled_by (None | str):
        created_at (str):
    """

    id: int
    from_type: None | str
    to_type: None | str
    processed_amount: int
    old_balance: ListBalanceHistoryResponse200DataItemOldBalance
    new_balance: ListBalanceHistoryResponse200DataItemNewBalance
    handled_by: None | str
    created_at: str

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        from_type: None | str
        from_type = self.from_type

        to_type: None | str
        to_type = self.to_type

        processed_amount = self.processed_amount

        old_balance = self.old_balance.to_dict()

        new_balance = self.new_balance.to_dict()

        handled_by: None | str
        handled_by = self.handled_by

        created_at = self.created_at

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "id": id,
                "fromType": from_type,
                "toType": to_type,
                "processedAmount": processed_amount,
                "oldBalance": old_balance,
                "newBalance": new_balance,
                "handledBy": handled_by,
                "createdAt": created_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.list_balance_history_response_200_data_item_new_balance import (
            ListBalanceHistoryResponse200DataItemNewBalance,
        )
        from ..models.list_balance_history_response_200_data_item_old_balance import (
            ListBalanceHistoryResponse200DataItemOldBalance,
        )

        d = dict(src_dict)
        id = d.pop("id")

        def _parse_from_type(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        from_type = _parse_from_type(d.pop("fromType"))

        def _parse_to_type(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        to_type = _parse_to_type(d.pop("toType"))

        processed_amount = d.pop("processedAmount")

        old_balance = ListBalanceHistoryResponse200DataItemOldBalance.from_dict(
            d.pop("oldBalance")
        )

        new_balance = ListBalanceHistoryResponse200DataItemNewBalance.from_dict(
            d.pop("newBalance")
        )

        def _parse_handled_by(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        handled_by = _parse_handled_by(d.pop("handledBy"))

        created_at = d.pop("createdAt")

        list_balance_history_response_200_data_item = cls(
            id=id,
            from_type=from_type,
            to_type=to_type,
            processed_amount=processed_amount,
            old_balance=old_balance,
            new_balance=new_balance,
            handled_by=handled_by,
            created_at=created_at,
        )

        return list_balance_history_response_200_data_item
