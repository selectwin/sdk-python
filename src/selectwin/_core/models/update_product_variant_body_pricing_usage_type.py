from enum import Enum


class UpdateProductVariantBodyPricingUsageType(str, Enum):
    LICENSED = "licensed"
    METERED = "metered"

    def __str__(self) -> str:
        return str(self.value)
