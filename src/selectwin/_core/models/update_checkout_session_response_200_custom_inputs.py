from enum import Enum


class UpdateCheckoutSessionResponse200CustomInputs(str, Enum):
    NULL = "null"

    def __str__(self) -> str:
        return str(self.value)
