from enum import Enum


class CreateTransactionResponse201PaymentProvider(str, Enum):
    SELECTWIN = "selectwin"

    def __str__(self) -> str:
        return str(self.value)
