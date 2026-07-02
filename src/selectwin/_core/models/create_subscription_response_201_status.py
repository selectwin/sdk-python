from enum import Enum


class CreateSubscriptionResponse201Status(str, Enum):
    ACTIVE = "active"
    CANCELED = "canceled"
    PASTDUE = "pastdue"
    PAUSED = "paused"
    PENDING = "pending"
    TRIALING = "trialing"
    UNPAID = "unpaid"

    def __str__(self) -> str:
        return str(self.value)
