from enum import Enum


class GetProductVariantResponse200PricingType(str, Enum):
    ONETIME = "oneTime"
    RECURRING = "recurring"

    def __str__(self) -> str:
        return str(self.value)
