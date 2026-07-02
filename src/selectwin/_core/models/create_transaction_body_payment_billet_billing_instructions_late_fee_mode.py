from enum import Enum


class CreateTransactionBodyPaymentBilletBillingInstructionsLateFeeMode(str, Enum):
    FIXED = "fixed"
    PERCENTAGE = "percentage"

    def __str__(self) -> str:
        return str(self.value)
