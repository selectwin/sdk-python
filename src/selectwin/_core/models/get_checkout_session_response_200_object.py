from enum import Enum


class GetCheckoutSessionResponse200Object(str, Enum):
    CHECKOUT_SESSION = "checkout.session"

    def __str__(self) -> str:
        return str(self.value)
