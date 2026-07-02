from enum import Enum


class CreateProductResponse201VariantsItemPricingType(str, Enum):
    ONETIME = "oneTime"
    RECURRING = "recurring"

    def __str__(self) -> str:
        return str(self.value)
