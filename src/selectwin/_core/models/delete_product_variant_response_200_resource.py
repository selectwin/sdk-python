from enum import Enum


class DeleteProductVariantResponse200Resource(str, Enum):
    VARIANT = "variant"

    def __str__(self) -> str:
        return str(self.value)
