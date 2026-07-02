from enum import Enum


class DeleteCheckoutSessionResponse200Resource(str, Enum):
    CHECKOUTSESSION = "checkoutSession"

    def __str__(self) -> str:
        return str(self.value)
