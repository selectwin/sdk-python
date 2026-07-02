from enum import Enum


class GetCheckoutSessionResponse200Currency(str, Enum):
    BRL = "BRL"

    def __str__(self) -> str:
        return str(self.value)
