from enum import Enum


class ListProductsResponse200DataItemVariantsItemPricingSchema(str, Enum):
    PACKAGE = "package"
    TIERED = "tiered"
    UNIT = "unit"

    def __str__(self) -> str:
        return str(self.value)
