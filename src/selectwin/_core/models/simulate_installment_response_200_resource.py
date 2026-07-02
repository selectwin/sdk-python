from enum import Enum


class SimulateInstallmentResponse200Resource(str, Enum):
    CREDIT = "credit"
    NUPAY = "nupay"

    def __str__(self) -> str:
        return str(self.value)
