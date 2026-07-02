from enum import Enum


class CreateTransactionResponse201PaymentVersion(str, Enum):
    VALUE_0 = "1.1"

    def __str__(self) -> str:
        return str(self.value)
