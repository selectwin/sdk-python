from enum import Enum


class GetCustomerResponse200AddressesItemOwnerType(str, Enum):
    COMPANY = "company"
    CUSTOMER = "customer"
    USER = "user"
    VENDOR = "vendor"

    def __str__(self) -> str:
        return str(self.value)
