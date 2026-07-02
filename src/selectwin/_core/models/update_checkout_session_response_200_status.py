from enum import Enum


class UpdateCheckoutSessionResponse200Status(str, Enum):
    ABANDONED = "abandoned"
    ACTIVE = "active"
    CANCELLED = "cancelled"
    COMPLETED = "completed"
    EXPIRED = "expired"

    def __str__(self) -> str:
        return str(self.value)
