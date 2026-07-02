from enum import Enum


class ListAddressesResponse200DataItemOwnerType(str, Enum):
    COMPANY = "company"
    CUSTOMER = "customer"
    USER = "user"
    VENDOR = "vendor"

    def __str__(self) -> str:
        return str(self.value)
