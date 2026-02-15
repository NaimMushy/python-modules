from abc import ABC, abstractmethod
from typing import Any as any
from typing import Optional as optional
from typing import Union as union
import re


class DataStream(ABC):

    def __init__(
        self,
        stream_id: str,
        data_type: str = "Any",
        data_name: str = "data"
    ) -> None:

        self.stream_id: str = stream_id
        self.stats: dict[str, any] = {}
        self.data_name: str = data_name

        print(
            "Initializing "
            f"{self.__class__.__name__.replace('Stream', '')} Stream..."
        )
        print(f"Stream ID: {stream_id} - Type: {data_type}\n")

    @abstractmethod
    def process_batch(self, data_batch: list[any]) -> str:
        pass

    def filter_data(
        self,
        data_batch: list[any],
        criteria: optional[str] = None
    ) -> list[any]:

        return (
            data_batch if not criteria
            else [data for data in data_batch if criteria in data]
        )

    def get_stats(self) -> dict[str, union[str, int, float]]:

        return {
            key: (
                val if not isinstance(val, list)
                else sum(val)
            ) for key, val in self.stats.items()
        }

    def display_stats(self) -> None:

        print(
            f"- {self.__class__.__name__.replace('Stream', '')} "
            f"data: {self.stats[self.data_name]} {self.data_name} processed"
        )


class SensorStream(DataStream):

    def __init__(self, stream_id: str) -> None:

        super().__init__(stream_id, "Environmental Data", "readings")

    def add_to_stats(
        self,
        env_var: str,
        mesure: any
    ) -> None:

        if env_var not in self.stats.keys():
            self.stats[env_var] = []
        self.stats[env_var].append(mesure)

        if self.data_name not in self.stats.keys():
            self.stats[self.data_name] = 0
        self.stats[self.data_name] += 1

    def reset_stats(self) -> None:

        for prev_stat in self.stats.keys():
            self.stats[prev_stat] = (
                [] if isinstance(self.stats[prev_stat], list)
                else 0
            )

    def validate_batch(self, data: any) -> tuple[str, union[int, float]]:

        if (match := re.match("([a-z]+):([0-9.]+)", data, re.I)):
            env_var: str = match.group(1)
            mesure: union[int, float] = (
                float(match.group(2)) if env_var == "temp"
                else int(match.group(2))
            )
            return env_var, mesure

        else:
            raise TypeError(
                "Invalid type for sensor data "
                "(string/float/int required)"
                " - [REJECTED]\n"
            )

    def process_batch(self, data_batch: list[any]) -> str:

        self.reset_stats()

        for data in data_batch:

            try:
                self.add_to_stats(*self.validate_batch(data))
            except TypeError as te:
                print(f"Caught TypeError: {te}")

        return f"Processing sensor batch: {data_batch}"

    def filter_data(
        self,
        data_batch: list[any],
        criteria: optional[str] = None
    ) -> list[any]:

        if not criteria:
            return data_batch

        filtered_batch: list[any] = []

        for data in data_batch:

            env_var: str
            mesure: union[float, int]

            try:
                env_var, mesure = self.validate_batch(data)

            except TypeError as te:
                print(f"Caught TypeError: {te}")

            else:

                if (criteria == "high-priority" and (
                    env_var == "temp" and mesure > 40
                ) or (
                    env_var == "humidity" and mesure > 80
                ) or (
                    env_var == "pressure" and mesure > 2000
                )) or criteria == env_var or criteria == str(mesure):

                    filtered_batch.append(env_var+":"+str(mesure))

        return filtered_batch

    def get_stats(self) -> dict[str, union[str, int, float]]:

        stats: dict[str, union[str, int, float]] = {}

        for env_var, mesure in self.stats.items():

            if isinstance(mesure, list) and len(mesure):
                stats["avg_" + env_var] = round(
                    sum(mesure) / len(mesure), 1
                )
            elif mesure != 0 or env_var == self.data_name:
                stats[env_var] = mesure

        return stats

    def display_stats(self, display_mode: str = "detailed") -> None:

        if display_mode == "detailed":
            print(
                f"Sensor analysis: "
                f"{self.stats[self.data_name]} {self.data_name} "
                "processed", end=""
            )

            for key, val in {
                key: val for key, val in self.get_stats().items()
                if "avg" in key
            }.items():
                print(f", {key.replace('_', ' ')}: {val}", end="")

            print("\n")

        else:
            super().display_stats()


class TransactionStream(DataStream):

    def __init__(self, stream_id: str) -> None:

        super().__init__(stream_id, "Financial Data", "operations")

    def add_to_stats(self, op: str, op_val: int) -> None:

        if op not in self.stats.keys():
            self.stats[op] = []
        self.stats[op].append(op_val)

        if self.data_name not in self.stats.keys():
            self.stats[self.data_name] = 0
        self.stats[self.data_name] += 1

    def reset_stats(self) -> None:

        self.stats = {
            stat: (
                [] if isinstance(val, list)
                else 0
            ) for stat, val in self.stats.items()
        }

    def validate_batch(self, data: any) -> tuple[str, int]:

        if (match := re.match("([a-z]+):([0-9]+)", data, re.I)):
            op: str = match.group(1)
            op_val: int = int(match.group(2))
            return op, op_val

        else:
            raise TypeError(
                "Invalid type for financial data "
                "(string/int required)"
                " - [REJECTED]\n"
            )

    def process_batch(self, data_batch: list[any]) -> str:

        self.reset_stats()

        for data in data_batch:

            try:
                self.add_to_stats(*self.validate_batch(data))
            except TypeError as te:
                print(f"Caught TypeError: {te}")

        return f"Processing transaction batch: {data_batch}"

    def filter_data(
        self,
        data_batch: list[any],
        criteria: optional[str] = None
    ) -> list[any]:

        if not criteria:
            return data_batch

        filtered_batch: list[any] = []

        for data in data_batch:

            op: str
            op_val: int

            try:
                op, op_val = self.validate_batch(data)
            except TypeError as te:
                print(f"caught TypeError: {te}")
            else:
                if (
                    criteria == "high-priority" and op_val >= 150
                ) or (
                    criteria == op or criteria == str(op_val)
                ):
                    filtered_batch.append(op+":"+str(op_val))

        return filtered_batch

    def get_stats(self) -> dict[str, union[str, int, float]]:

        stats: dict[str, any] = {"net_flow": 0}

        for op, op_val in self.stats.items():

            if isinstance(op_val, list) and len(op_val):
                stats["net_flow"] += (
                    sum(op_val) if op == "buy"
                    else -sum(op_val)
                )
            elif op_val != 0 or op == self.data_name:
                stats[op] = op_val

        stats["net_flow"] = (
            "+" if stats["net_flow"] >= 0
            else "-"
        ) + str(stats["net_flow"])

        return stats

    def display_stats(self, display_mode: str = "detailed") -> None:

        if display_mode == "detailed":
            print(
                f"Transaction analysis: "
                f"{self.stats[self.data_name]} {self.data_name} "
                f"processed, net flow: "
                f"{self.get_stats()['net_flow']} units\n"
            )

        else:
            super().display_stats()


class EventStream(DataStream):

    def __init__(
        self,
        stream_id: str
    ) -> None:

        super().__init__(stream_id, "System Events", "events")

    def add_to_stats(self, event: str) -> None:

        if event not in self.stats.keys():
            self.stats[event] = 0
        self.stats[event] += 1

        if "events" not in self.stats.keys():
            self.stats["events"] = 0
        self.stats["events"] += 1

    def reset_stats(self) -> None:

        self.stats = {
            stat: 0 for stat in self.stats.keys()
        }

    def validate_batch(self, data) -> str:

        if not isinstance(data, str):
            raise TypeError(
                "Invalid type for system events "
                "(string required)"
                " - [REJECTED]\n"
            )

        return data

    def process_batch(self, data_batch: list[any]) -> str:

        self.reset_stats()

        for data in data_batch:

            try:
                self.add_to_stats(self.validate_batch(data))
            except TypeError as te:
                print(f"caught TypeError: {te}")

        return f"Processing event batch: {data_batch}"

    def filter_data(
        self,
        data_batch: list[any],
        criteria: optional[str] = None
    ) -> list[any]:

        if not criteria:
            return data_batch

        filtered_batch: list[any] = []

        for data in data_batch:

            try:
                event: str = self.validate_batch(data)
            except TypeError as te:
                print(f"caught TypeError: {te}")
            else:
                if (
                    criteria == "high-priority" and (
                        event == "error" or event == "warning"
                    )
                ) or (
                    criteria == event
                ):
                    filtered_batch.append(event)

        return filtered_batch

    def get_stats(self) -> dict[str, union[str, int, float]]:

        return self.stats

    def display_stats(self, display_mode: str = "detailed") -> None:

        if display_mode == "detailed":
            print(
                f"Event analysis: "
                f"{self.stats[self.data_name]} {self.data_name}"
                f", {self.stats['error']} error"
                f"{'s' if self.stats['error'] > 1 else ''} detected\n"
            )

        else:
            super().display_stats()


class StreamProcessor:

    def process_single_stream(
        self,
        data_batch: list[any],
        stream: DataStream
    ) -> None:

        print(stream.process_batch(data_batch))
        stream.display_stats()

    def process_stream(
        self,
        data_batches: list[list[any]],
        streams: dict[str, DataStream],
        criteria: optional[str] = None
    ) -> dict[str, int]:

        results: dict[str, list[any]] = {}

        print("Processing mixed stream types through unified interface...\n")

        if criteria:
            print(
                f"Stream filtering active: {criteria.capitalize()} "
                "data only"
            )

        for data_batch in range(len(data_batches)):
            results["sensor"]: list[any] = [
                data for data in data_batches[data_batch]
                if data in ["humidity", "temp", "pressure"]
            ]

            results["trans"]: list[any] = [
                data for data in data_batches[data_batch]
                if data in ["buy", "sell"]
            ]

            results["event"]: list[any] = [
                data for data in data_batches[data_batch]
                if data in ["login", "error", "warning", "logout"]
            ]

            print(f"Batch {data_batch + 1} results:")

            for stream_name, stream in streams.items():
                if criteria:
                    stream.process_batch(
                        stream.filter_data(
                            results[stream_name], criteria
                        )
                    )

                else:
                    stream.process_batch(
                        stream.filter_data(
                            results[stream_name]
                        )
                    )
                    stream.display_stats("concise")

                results[stream_name] = stream.get_stats()[
                    stream.data_name
                ]

            if criteria:

                results["sensor"] = (
                    str(results["sensor"])
                    + " critical sensor alert"
                    + ("s" if results["sensor"] > 1 else "")
                )
                results["trans"] = (
                    str(results["trans"])
                    + " large transaction"
                    + ("s" if results["trans"] > 1 else "")
                )
                results["event"] = (
                    str(results["event"])
                    + " system error"
                    + ("s" if results["event"] > 1 else "")
                )

                print("Filtered results: ", end="")
                fst: bool = True
                for stream_type, stream_result in results.items():
                    if not fst:
                        print(", ", end="")
                    print(stream_result, end="")
                    fst = False

        print("")

        return results


def main() -> None:
    print("=== CODE NEXUS - POLYMORPHIC STREAM SYSTEM ===\n")

    batches: dict[str, list[any]] = {
        "sensor": ["temp:22.5", "humidity:65", "pressure:1013"],
        "trans": ["buy:100", "sell:150", "buy:75"],
        "event": ["login", "error", "logout"]
    }

    mixed_batch: list[any] = [
        "temp:76",
        "error",
        "buy:500",
        "sell:678",
        "pressure:3000",
        "login",
        "warning",
        "buy:50",
        "humidity:44"
    ]

    stream_proc: StreamProcessor = StreamProcessor()

    sensor = SensorStream("SENSOR_001")
    stream_proc.process_single_stream(batches["sensor"], sensor)

    trans = TransactionStream("TRANS_001")
    stream_proc.process_single_stream(batches["trans"], trans)

    event = EventStream("EVENT_001")
    stream_proc.process_single_stream(batches["event"], event)

    streams: dict[str, DataStream] = {
        "sensor": sensor,
        "trans": trans,
        "event": event
    }

    print("=== Polymorphic Stream Processing ===")

    stream_proc.process_stream([mixed_batch], streams)
    stream_proc.process_stream([mixed_batch], streams, "high-priority")

    print("\nAll streams processed successfully - Nexus throughout optimal")


if __name__ == "__main__":
    main()
