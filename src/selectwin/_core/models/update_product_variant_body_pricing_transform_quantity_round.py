from enum import Enum


class UpdateProductVariantBodyPricingTransformQuantityRound(str, Enum):
    DOWN = "down"
    UP = "up"

    def __str__(self) -> str:
        return str(self.value)
