from enum import Enum


class CreateSubscriptionBodyCustomerGender(str, Enum):
    FEMALE = "female"
    MALE = "male"
    OTHER = "other"

    def __str__(self) -> str:
        return str(self.value)
