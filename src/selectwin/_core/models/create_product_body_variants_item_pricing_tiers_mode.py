from enum import Enum


class CreateProductBodyVariantsItemPricingTiersMode(str, Enum):
    GRADUATED = "graduated"
    VOLUME = "volume"

    def __str__(self) -> str:
        return str(self.value)
