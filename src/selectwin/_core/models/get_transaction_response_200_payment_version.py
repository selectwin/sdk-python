from enum import Enum


class GetTransactionResponse200PaymentVersion(str, Enum):
    VALUE_0 = "1.1"

    def __str__(self) -> str:
        return str(self.value)
