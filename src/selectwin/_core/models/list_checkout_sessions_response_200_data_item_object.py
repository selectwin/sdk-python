from enum import Enum


class ListCheckoutSessionsResponse200DataItemObject(str, Enum):
    CHECKOUT_SESSION = "checkout.session"

    def __str__(self) -> str:
        return str(self.value)
