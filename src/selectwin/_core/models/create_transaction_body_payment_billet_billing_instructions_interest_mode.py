from enum import Enum


class CreateTransactionBodyPaymentBilletBillingInstructionsInterestMode(str, Enum):
    DAILYAMOUNT = "dailyAmount"
    DAILYPERCENTAGE = "dailyPercentage"
    MONTHLYPERCENTAGE = "monthlyPercentage"

    def __str__(self) -> str:
        return str(self.value)
