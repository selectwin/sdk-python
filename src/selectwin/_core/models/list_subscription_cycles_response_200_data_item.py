from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.list_subscription_cycles_response_200_data_item_links import (
        ListSubscriptionCyclesResponse200DataItemLinks,
    )
    from ..models.list_subscription_cycles_response_200_data_item_merchant import (
        ListSubscriptionCyclesResponse200DataItemMerchant,
    )


T = TypeVar("T", bound="ListSubscriptionCyclesResponse200DataItem")


@_attrs_define
class ListSubscriptionCyclesResponse200DataItem:
    """
    Attributes:
        id (str): Public identifier (scy_/cycle_…)
        cycle (int):
        status (str):
        start_date (str):
        end_date (None | str):
        due_date (str):
        billed_at (None | str):
        updated_at (str):
        created_at (str):
        merchant (ListSubscriptionCyclesResponse200DataItemMerchant | Unset):
        field_links (ListSubscriptionCyclesResponse200DataItemLinks | Unset):
    """

    id: str
    cycle: int
    status: str
    start_date: str
    end_date: None | str
    due_date: str
    billed_at: None | str
    updated_at: str
    created_at: str
    merchant: ListSubscriptionCyclesResponse200DataItemMerchant | Unset = UNSET
    field_links: ListSubscriptionCyclesResponse200DataItemLinks | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        cycle = self.cycle

        status = self.status

        start_date = self.start_date

        end_date: None | str
        end_date = self.end_date

        due_date = self.due_date

        billed_at: None | str
        billed_at = self.billed_at

        updated_at = self.updated_at

        created_at = self.created_at

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
                "cycle": cycle,
                "status": status,
                "startDate": start_date,
                "endDate": end_date,
                "dueDate": due_date,
                "billedAt": billed_at,
                "updatedAt": updated_at,
                "createdAt": created_at,
            }
        )
        if merchant is not UNSET:
            field_dict["merchant"] = merchant
        if field_links is not UNSET:
            field_dict["_links"] = field_links

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.list_subscription_cycles_response_200_data_item_links import (
            ListSubscriptionCyclesResponse200DataItemLinks,
        )
        from ..models.list_subscription_cycles_response_200_data_item_merchant import (
            ListSubscriptionCyclesResponse200DataItemMerchant,
        )

        d = dict(src_dict)
        id = d.pop("id")

        cycle = d.pop("cycle")

        status = d.pop("status")

        start_date = d.pop("startDate")

        def _parse_end_date(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        end_date = _parse_end_date(d.pop("endDate"))

        due_date = d.pop("dueDate")

        def _parse_billed_at(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        billed_at = _parse_billed_at(d.pop("billedAt"))

        updated_at = d.pop("updatedAt")

        created_at = d.pop("createdAt")

        _merchant = d.pop("merchant", UNSET)
        merchant: ListSubscriptionCyclesResponse200DataItemMerchant | Unset
        if isinstance(_merchant, Unset):
            merchant = UNSET
        else:
            merchant = ListSubscriptionCyclesResponse200DataItemMerchant.from_dict(
                _merchant
            )

        _field_links = d.pop("_links", UNSET)
        field_links: ListSubscriptionCyclesResponse200DataItemLinks | Unset
        if isinstance(_field_links, Unset):
            field_links = UNSET
        else:
            field_links = ListSubscriptionCyclesResponse200DataItemLinks.from_dict(
                _field_links
            )

        list_subscription_cycles_response_200_data_item = cls(
            id=id,
            cycle=cycle,
            status=status,
            start_date=start_date,
            end_date=end_date,
            due_date=due_date,
            billed_at=billed_at,
            updated_at=updated_at,
            created_at=created_at,
            merchant=merchant,
            field_links=field_links,
        )

        return list_subscription_cycles_response_200_data_item
