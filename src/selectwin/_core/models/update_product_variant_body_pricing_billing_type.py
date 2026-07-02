from enum import Enum


class UpdateProductVariantBodyPricingBillingType(str, Enum):
    EXACTDAY = "exactday"
    POSTPAID = "postpaid"
    PREPAID = "prepaid"

    def __str__(self) -> str:
        return str(self.value)
