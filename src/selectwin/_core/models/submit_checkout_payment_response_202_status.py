from enum import Enum


class SubmitCheckoutPaymentResponse202Status(str, Enum):
    COMPLETED = "completed"
    FAILED = "failed"
    PENDING = "pending"
    PROCESSING = "processing"
    REQUIRESACTION = "requiresAction"

    def __str__(self) -> str:
        return str(self.value)
