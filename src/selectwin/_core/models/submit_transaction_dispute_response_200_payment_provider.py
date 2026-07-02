from enum import Enum


class SubmitTransactionDisputeResponse200PaymentProvider(str, Enum):
    SELECTWIN = "selectwin"

    def __str__(self) -> str:
        return str(self.value)
