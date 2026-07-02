from enum import Enum


class ListTransactionsMethod(str, Enum):
    BILLET = "billet"
    CREDIT = "credit"
    NUPAY = "nupay"
    PIX = "pix"

    def __str__(self) -> str:
        return str(self.value)
