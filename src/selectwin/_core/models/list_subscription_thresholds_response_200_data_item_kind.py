from enum import Enum


class ListSubscriptionThresholdsResponse200DataItemKind(str, Enum):
    AMOUNT = "amount"
    QUANTITY = "quantity"

    def __str__(self) -> str:
        return str(self.value)
