from enum import Enum


class AddSubscriptionThresholdResponse201Kind(str, Enum):
    AMOUNT = "amount"
    QUANTITY = "quantity"

    def __str__(self) -> str:
        return str(self.value)
