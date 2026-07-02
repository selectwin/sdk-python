from enum import Enum


class ListWebhookDispatchesResponse200DataItemStatus(str, Enum):
    CANCELED = "canceled"
    FAILED = "failed"
    PENDING = "pending"
    RETRYING = "retrying"
    SUCCESS = "success"

    def __str__(self) -> str:
        return str(self.value)
