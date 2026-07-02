from enum import Enum


class SubmitTransactionDisputeResponse200Method(str, Enum):
    BILLET = "billet"
    CREDIT = "credit"
    PIX = "pix"

    def __str__(self) -> str:
        return str(self.value)
