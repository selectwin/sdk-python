from enum import Enum


class CreateCouponResponse201Scope(str, Enum):
    FIRSTCHARGE = "firstCharge"
    RECURRING = "recurring"

    def __str__(self) -> str:
        return str(self.value)
