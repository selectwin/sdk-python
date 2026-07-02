from enum import Enum


class ListProductsResponse200DataItemVariantsItemPricingType(str, Enum):
    ONETIME = "oneTime"
    RECURRING = "recurring"

    def __str__(self) -> str:
        return str(self.value)
