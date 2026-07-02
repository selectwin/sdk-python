from enum import Enum


class CreateCheckoutSessionResponse201Object(str, Enum):
    CHECKOUT_SESSION = "checkout.session"

    def __str__(self) -> str:
        return str(self.value)
