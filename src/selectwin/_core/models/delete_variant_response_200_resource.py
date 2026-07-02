from enum import Enum


class DeleteVariantResponse200Resource(str, Enum):
    VARIANT = "variant"

    def __str__(self) -> str:
        return str(self.value)
