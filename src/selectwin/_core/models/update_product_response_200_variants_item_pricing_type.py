from enum import Enum


class UpdateProductResponse200VariantsItemPricingType(str, Enum):
    ONETIME = "oneTime"
    RECURRING = "recurring"

    def __str__(self) -> str:
        return str(self.value)
