from enum import Enum


class UpdateProductPutResponse200Type(str, Enum):
    DIGITAL = "digital"
    OTHER = "other"
    PHYSICAL = "physical"

    def __str__(self) -> str:
        return str(self.value)
