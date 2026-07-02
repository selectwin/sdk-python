from enum import Enum


class AddSubscriptionThresholdBodyKind(str, Enum):
    AMOUNT = "amount"
    QUANTITY = "quantity"

    def __str__(self) -> str:
        return str(self.value)
