from enum import Enum


class CreateProductVariantResponse201PricingSchema(str, Enum):
    PACKAGE = "package"
    TIERED = "tiered"
    UNIT = "unit"

    def __str__(self) -> str:
        return str(self.value)
