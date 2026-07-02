from enum import Enum


class UpdateAddressPatchResponse200OwnerType(str, Enum):
    COMPANY = "company"
    CUSTOMER = "customer"
    USER = "user"
    VENDOR = "vendor"

    def __str__(self) -> str:
        return str(self.value)
