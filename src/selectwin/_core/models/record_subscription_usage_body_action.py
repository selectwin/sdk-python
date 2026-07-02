from enum import Enum


class RecordSubscriptionUsageBodyAction(str, Enum):
    INCREMENT = "increment"
    SET = "set"

    def __str__(self) -> str:
        return str(self.value)
