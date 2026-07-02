from enum import Enum


class CreateCheckoutSessionBodyAmbient(str, Enum):
    LIVE = "live"
    SANDBOX = "sandbox"

    def __str__(self) -> str:
        return str(self.value)
