from enum import Enum


class ListAllVariantsResponse200ItemPricingType(str, Enum):
    ONETIME = "oneTime"
    RECURRING = "recurring"

    def __str__(self) -> str:
        return str(self.value)
