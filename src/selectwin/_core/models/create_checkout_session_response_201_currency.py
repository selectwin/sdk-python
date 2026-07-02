from enum import Enum


class CreateCheckoutSessionResponse201Currency(str, Enum):
    BRL = "BRL"

    def __str__(self) -> str:
        return str(self.value)
