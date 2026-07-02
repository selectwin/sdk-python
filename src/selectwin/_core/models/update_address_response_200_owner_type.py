from enum import Enum


class UpdateAddressResponse200OwnerType(str, Enum):
    COMPANY = "company"
    CUSTOMER = "customer"
    USER = "user"
    VENDOR = "vendor"

    def __str__(self) -> str:
        return str(self.value)
