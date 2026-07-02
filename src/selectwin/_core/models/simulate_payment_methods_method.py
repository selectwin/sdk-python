from enum import Enum


class SimulatePaymentMethodsMethod(str, Enum):
    BILLET = "billet"
    CREDIT = "credit"
    NUPAY = "nupay"
    PIX = "pix"

    def __str__(self) -> str:
        return str(self.value)
