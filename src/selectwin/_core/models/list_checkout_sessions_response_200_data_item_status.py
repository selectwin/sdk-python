from enum import Enum


class ListCheckoutSessionsResponse200DataItemStatus(str, Enum):
    ABANDONED = "abandoned"
    ACTIVE = "active"
    CANCELLED = "cancelled"
    COMPLETED = "completed"
    EXPIRED = "expired"

    def __str__(self) -> str:
        return str(self.value)
