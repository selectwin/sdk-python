from enum import Enum


class CreateProductVariantBodyPricingBillingType(str, Enum):
    EXACTDAY = "exactday"
    POSTPAID = "postpaid"
    PREPAID = "prepaid"

    def __str__(self) -> str:
        return str(self.value)
