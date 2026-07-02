from enum import Enum


class DeleteCheckoutPaymentLinkResponse200Resource(str, Enum):
    CHECKOUT_PAYMENTLINK = "checkout-paymentLink"

    def __str__(self) -> str:
        return str(self.value)
