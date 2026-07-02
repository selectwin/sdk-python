from enum import Enum


class CreateTransactionBodyPaymentPixBillingInstructionsDiscountsItemMode(str, Enum):
    FIXED = "fixed"
    PERCENTAGE = "percentage"

    def __str__(self) -> str:
        return str(self.value)
