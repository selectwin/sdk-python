from enum import Enum


class ListWebhookEventsResponse200DataItemDispatchesItemStatus(str, Enum):
    CANCELED = "canceled"
    FAILED = "failed"
    PENDING = "pending"
    RETRYING = "retrying"
    SUCCESS = "success"

    def __str__(self) -> str:
        return str(self.value)
