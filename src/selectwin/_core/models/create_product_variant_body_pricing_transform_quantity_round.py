from enum import Enum


class CreateProductVariantBodyPricingTransformQuantityRound(str, Enum):
    DOWN = "down"
    UP = "up"

    def __str__(self) -> str:
        return str(self.value)
