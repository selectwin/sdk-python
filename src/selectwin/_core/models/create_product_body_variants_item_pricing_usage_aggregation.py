from enum import Enum


class CreateProductBodyVariantsItemPricingUsageAggregation(str, Enum):
    LASTDURINGPERIOD = "lastDuringPeriod"
    LASTEVER = "lastEver"
    MAX = "max"
    SUM = "sum"

    def __str__(self) -> str:
        return str(self.value)
