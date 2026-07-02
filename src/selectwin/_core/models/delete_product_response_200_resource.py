from enum import Enum


class DeleteProductResponse200Resource(str, Enum):
    PRODUCT = "product"

    def __str__(self) -> str:
        return str(self.value)
