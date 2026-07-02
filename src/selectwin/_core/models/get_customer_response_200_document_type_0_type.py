from enum import Enum


class GetCustomerResponse200DocumentType0Type(str, Enum):
    CNPJ = "cnpj"
    CPF = "cpf"
    PASSPORT = "passport"

    def __str__(self) -> str:
        return str(self.value)
