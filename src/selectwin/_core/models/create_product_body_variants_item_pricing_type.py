from enum import Enum


class CreateProductBodyVariantsItemPricingType(str, Enum):
    ONETIME = "oneTime"
    RECURRING = "recurring"

    def __str__(self) -> str:
        return str(self.value)
