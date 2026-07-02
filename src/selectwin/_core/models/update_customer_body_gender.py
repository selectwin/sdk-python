from enum import Enum


class UpdateCustomerBodyGender(str, Enum):
    FEMALE = "female"
    MALE = "male"
    OTHER = "other"

    def __str__(self) -> str:
        return str(self.value)
