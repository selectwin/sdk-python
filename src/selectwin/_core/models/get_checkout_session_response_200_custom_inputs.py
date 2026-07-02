from enum import Enum


class GetCheckoutSessionResponse200CustomInputs(str, Enum):
    NULL = "null"

    def __str__(self) -> str:
        return str(self.value)
