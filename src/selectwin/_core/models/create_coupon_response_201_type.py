from enum import Enum


class CreateCouponResponse201Type(str, Enum):
    FLAT = "flat"
    PERCENTAGE = "percentage"

    def __str__(self) -> str:
        return str(self.value)
