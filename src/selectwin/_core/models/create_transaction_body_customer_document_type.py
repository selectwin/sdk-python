from enum import Enum


class CreateTransactionBodyCustomerDocumentType(str, Enum):
    CNPJ = "cnpj"
    CPF = "cpf"
    PASSPORT = "passport"

    def __str__(self) -> str:
        return str(self.value)
