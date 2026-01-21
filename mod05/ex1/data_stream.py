from abc import ABC, abstractmethod
from typing import Any, Optional, Union as any, optional, union


class DataStream(ABC):
    def __init__(self, stream_id: str) -> None:
        self.stream_id: str = stream_id
        self._stats: dict[str, union[str, int, float]] = {}

    @abstractmethod
    def process_batch(self, data_batch: list[any]) -> str:
        pass

    def filter_data(
        self,
        data_batch: list[any],
        criteria: optional[str] = None
    ) -> list[any]:
        if criteria:
            filtered_data: list[any] = [
                data for data in data_batch if criteria in data
            ]
        else:
            filtered_data = data_batch
        return filtered_data

    def get_stats(self) -> dict[str, union[str, int, float]]:
        return self._stats


class SensorStream(DataStream):
    def __init__(self, stream_id: str) -> None:
        super().__init__(stream_id)
        self._stats["readings"] = 0
        self._stats["critical"] = 0
        print("initializing sensor stream...")
        print(f"stream ID: {self.stream_id} - type: environmental data")

    def process_batch(self, data_batch: list[any]) -> str:
        for data in data_batch:
            env_var: any = data.split(":")[0]
            if not isinstance(env_var, str):
                raise TypeError(
                    "invalid type for environment variable "
                    "(string) - [REJECTED]\n"
                )
            val: any = data.split(":")[1]
            if not isinstance(val, [int, float]):
                raise TypeError(
                    "invalid type for mesured environment data "
                    "(integer or float) - [REJECTED]\n"
                )
            mesure_critical(env_var, val)


