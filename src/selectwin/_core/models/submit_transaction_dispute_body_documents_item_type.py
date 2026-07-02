from enum import Enum


class SubmitTransactionDisputeBodyDocumentsItemType(str, Enum):
    COMMUNICATIONPROOF = "communicationProof"
    DELIVERYPROOF = "deliveryProof"
    DELIVERYRECEIPT = "deliveryReceipt"
    FISCALDOCUMENT = "fiscalDocument"
    SHIPMENTPROOF = "shipmentProof"

    def __str__(self) -> str:
        return str(self.value)
