from enum import Enum


class CreateTransactionResponse201Method(str, Enum):
    BILLET = "billet"
    CREDIT = "credit"
    PIX = "pix"

    def __str__(self) -> str:
        return str(self.value)
