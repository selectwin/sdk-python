from enum import Enum


class CreateTransactionBodyCustomerGender(str, Enum):
    FEMALE = "female"
    MALE = "male"
    OTHER = "other"

    def __str__(self) -> str:
        return str(self.value)
