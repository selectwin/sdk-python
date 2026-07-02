from enum import Enum


class CreateProductVariantBodyPricingUsageType(str, Enum):
    LICENSED = "licensed"
    METERED = "metered"

    def __str__(self) -> str:
        return str(self.value)
