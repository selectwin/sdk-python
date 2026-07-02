from enum import Enum


class UpdateCheckoutSessionBodyStatus(str, Enum):
    ABANDONED = "abandoned"
    ACTIVE = "active"

    def __str__(self) -> str:
        return str(self.value)
