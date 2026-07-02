from enum import Enum


class CreateCheckoutSessionResponse201CustomInputs(str, Enum):
    NULL = "null"

    def __str__(self) -> str:
        return str(self.value)
