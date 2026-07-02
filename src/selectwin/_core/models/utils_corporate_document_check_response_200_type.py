from enum import Enum


class UtilsCorporateDocumentCheckResponse200Type(str, Enum):
    CNPJ = "cnpj"
    CPF = "cpf"

    def __str__(self) -> str:
        return str(self.value)
