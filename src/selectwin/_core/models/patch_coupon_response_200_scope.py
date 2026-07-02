from enum import Enum


class PatchCouponResponse200Scope(str, Enum):
    FIRSTCHARGE = "firstCharge"
    RECURRING = "recurring"

    def __str__(self) -> str:
        return str(self.value)
