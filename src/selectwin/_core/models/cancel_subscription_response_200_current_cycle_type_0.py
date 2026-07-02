from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

T = TypeVar("T", bound="CancelSubscriptionResponse200CurrentCycleType0")


@_attrs_define
class CancelSubscriptionResponse200CurrentCycleType0:
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

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
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

        cancel_subscription_response_200_current_cycle_type_0 = cls(
            id=id,
            cycle=cycle,
            status=status,
            start_date=start_date,
            end_date=end_date,
            due_date=due_date,
            billed_at=billed_at,
            updated_at=updated_at,
            created_at=created_at,
        )

        return cancel_subscription_response_200_current_cycle_type_0
