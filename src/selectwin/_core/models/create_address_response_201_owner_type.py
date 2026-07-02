from enum import Enum


class CreateAddressResponse201OwnerType(str, Enum):
    COMPANY = "company"
    CUSTOMER = "customer"
    USER = "user"
    VENDOR = "vendor"

    def __str__(self) -> str:
        return str(self.value)
