from enum import Enum


class CreateTransactionBodyPaymentBilletBillingInstructionsDiscountsItemMode(str, Enum):
    FIXED = "fixed"
    PERCENTAGE = "percentage"

    def __str__(self) -> str:
        return str(self.value)
