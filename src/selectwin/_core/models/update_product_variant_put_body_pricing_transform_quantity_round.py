from enum import Enum


class UpdateProductVariantPutBodyPricingTransformQuantityRound(str, Enum):
    DOWN = "down"
    UP = "up"

    def __str__(self) -> str:
        return str(self.value)
