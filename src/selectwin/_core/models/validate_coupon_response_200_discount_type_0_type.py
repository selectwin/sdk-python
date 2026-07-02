from enum import Enum


class ValidateCouponResponse200DiscountType0Type(str, Enum):
    FLAT = "flat"
    PERCENTAGE = "percentage"

    def __str__(self) -> str:
        return str(self.value)
