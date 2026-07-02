from enum import Enum


class ListCouponsResponse200DataItemScope(str, Enum):
    FIRSTCHARGE = "firstCharge"
    RECURRING = "recurring"

    def __str__(self) -> str:
        return str(self.value)
