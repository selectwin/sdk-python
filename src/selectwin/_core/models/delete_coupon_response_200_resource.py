from enum import Enum


class DeleteCouponResponse200Resource(str, Enum):
    COUPON = "coupon"

    def __str__(self) -> str:
        return str(self.value)
