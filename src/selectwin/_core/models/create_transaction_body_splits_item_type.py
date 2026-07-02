from enum import Enum


class CreateTransactionBodySplitsItemType(str, Enum):
    FLAT = "flat"
    PERCENTAGE = "percentage"

    def __str__(self) -> str:
        return str(self.value)
