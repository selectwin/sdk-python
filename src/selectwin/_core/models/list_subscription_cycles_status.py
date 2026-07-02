from enum import Enum


class ListSubscriptionCyclesStatus(str, Enum):
    CANCELED = "canceled"
    FAILED = "failed"
    PAID = "paid"
    PROCESSING = "processing"
    SCHEDULED = "scheduled"

    def __str__(self) -> str:
        return str(self.value)
