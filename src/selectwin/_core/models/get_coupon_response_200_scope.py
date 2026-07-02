from enum import Enum


class GetCouponResponse200Scope(str, Enum):
    FIRSTCHARGE = "firstCharge"
    RECURRING = "recurring"

    def __str__(self) -> str:
        return str(self.value)
