from enum import Enum


class SimulateInstallmentResource(str, Enum):
    CREDIT = "credit"
    NUPAY = "nupay"

    def __str__(self) -> str:
        return str(self.value)
