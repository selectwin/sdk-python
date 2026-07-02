from enum import Enum


class GetTransactionResponse200Status(str, Enum):
    ANALYZING = "analyzing"
    APPROVED = "approved"
    AWAITING = "awaiting"
    CANCELED = "canceled"
    CHARGEBACK = "chargeback"
    DISPUTE = "dispute"
    FAILED = "failed"
    FRAUD_REVIEW = "fraud-review"
    PENDING = "pending"
    PRE_AUTHORIZED = "pre-authorized"
    REFUNDED = "refunded"
    REFUSED = "refused"

    def __str__(self) -> str:
        return str(self.value)
