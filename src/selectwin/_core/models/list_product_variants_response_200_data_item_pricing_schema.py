from enum import Enum


class ListProductVariantsResponse200DataItemPricingSchema(str, Enum):
    PACKAGE = "package"
    TIERED = "tiered"
    UNIT = "unit"

    def __str__(self) -> str:
        return str(self.value)
