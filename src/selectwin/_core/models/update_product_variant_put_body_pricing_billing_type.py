from enum import Enum


class UpdateProductVariantPutBodyPricingBillingType(str, Enum):
    EXACTDAY = "exactday"
    POSTPAID = "postpaid"
    PREPAID = "prepaid"

    def __str__(self) -> str:
        return str(self.value)
