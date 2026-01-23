from abc import ABC, abstractmethod
from typing import Any as any
from typing import Optional as optional
from typing import Union as union
import re


SENSOR_BATCH: list[any] = ["temp:22.5", "humidity:65", "pressure:1013"]
TRANS_BATCH: list[any] = ["buy:100", "sell:150", "buy:75"]
EVENT_BATCH: list[any] = ["login", "error", "logout"]
MIXED_BATCH: list[any] = [
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


class DataStream(ABC):
    """
    A class that represents a data stream.
    """
    def __init__(self, stream_id: str) -> None:
        """
        Initializes the data stream's properties.

        Parameters
        ----------
        stream_id
            The stream's ID.
        """
        self.stream_id: str = stream_id
        self._stats: dict[str, any] = {}

    @abstractmethod
    def process_batch(self, data_batch: list[any]) -> str:
        """
        Processes the data batch given as parameter.

        Parameters
        ----------
        data_batch
            The data batch to process.

        Returns
        -------
        str
            The processed data.
        """
        pass

    def filter_data(
        self,
        data_batch: list[any],
        criteria: optional[str] = None
    ) -> list[any]:
        """
        Filters a data batch based on a specific criteria.

        Parameters
        ----------
        data_batch
            The data batch to filter.
        criteria
            The criteria used to filter the batch.

        Returns
        -------
        list[any]
            The filtered data batch.
        """
        if not criteria:
            return data_batch
        filtered_data: list[any] = [
                data for data in data_batch if criteria in data
            ]
        return filtered_data

    def get_stats(self) -> dict[str, union[str, int, float]]:
        """
        Gives the analyzed stats of the data batch.

        Returns
        -------
        dict[str, union[str, int, float]]
            The dictionary containing the analyzed stats of the data batch.
        """
        stats: dict[str, any] = {}
        for key, val in self._stats.items():
            if isinstance(val, list):
                stats[key] = sum(val)
            else:
                stats[key] = val
        return stats


class SensorStream(DataStream):
    """
    A class that represents a sensor stream.
    """
    def __init__(self, stream_id: str, silent_mode: bool = True) -> None:
        """
        Initialized the sensor stream's properties.

        Parameters
        ----------
        stream_id
            The stream's ID.
        silent_mode
            Whether or not the initialization of the stream is announced.
        """
        super().__init__(stream_id)
        if not silent_mode:
            print("initializing sensor stream...")
            print(f"stream ID: {self.stream_id} - type: environmental data")

    def add_to_stats(
        self,
        env_var: str,
        mesure: any
    ) -> None:
        """
        Adds the stats from the processed data to the stream's stats.

        Parameters
        ----------
        env_var
            The environment variable mesured in the data.
        mesure
            The mesure noted in the data.
        """
        if env_var not in self._stats.keys():
            self._stats[env_var] = [mesure]
        else:
            self._stats[env_var].append(mesure)
        if "readings" in self._stats.keys():
            self._stats["readings"] += 1
        else:
            self._stats["readings"] = 1

    def reset_stats(self) -> None:
        """
        Resets the stream's stats in between batches.
        """
        for prev_stat in self._stats.keys():
            if isinstance(self._stats[prev_stat], list):
                self._stats[prev_stat] = []
            else:
                self._stats[prev_stat] = 0

    def validate_batch(self, data: any) -> tuple[str, int | float]:
        """
        Verifies whether or not the data is of the correct format.

        Parameters
        ----------
        data
            The data to validate.

        Returns
        -------
        tuple[str, int | float]
            The verified data separated as environment variable and mesure.

        Raises
        ------
        TypeError:
            Raised if the data given isn't formatted correctly.
        """
        if (match := re.match("([a-z]+):([0-9.]+)", data, re.I)):
            env_var: str = match.group(1)
            if env_var == "temp":
                mesure: float | int = float(match.group(2))
            else:
                mesure = int(match.group(2))
            return env_var, mesure
        else:
            raise TypeError(
                "invalid type for sensor data "
                "(string, float/int required)"
                " - [REJECTED]\n"
            )

    def process_batch(self, data_batch: list[any]) -> str:
        """
        Processed the data batch given as parameter.

        Parameters
        ----------
        data_batch
            The data batch to process.

        Returns
        -------
        str
            The processed data batch.
        """
        self.reset_stats()
        for data in data_batch:
            try:
                validated_data: tuple[
                    str, union[int, float]
                ] = self.validate_batch(data)
            except TypeError as te:
                print(f"caught TypeError: {te}")
            else:
                self.add_to_stats(validated_data[0], validated_data[1])
        return f"processing sensor batch: {data_batch}"

    def filter_data(
        self,
        data_batch: list[any],
        criteria: optional[str] = None
    ) -> list[any]:
        """
        Filters a data batch based on a specific criteria.

        Parameters
        ----------
        data_batch
            The data batch to filter.
        criteria
            The criteria used to filter the batch.

        Returns
        -------
        list[any]
            The filtered data batch.
        """
        if not criteria:
            return data_batch
        filtered_batch: list[any] = []
        for data in data_batch:
            try:
                validated_data: tuple[
                    str, union[int, float]
                ] = self.validate_batch(data)
            except TypeError as te:
                print(f"caught TypeError: {te}")
            else:
                env_var: str = validated_data[0]
                mesure: int | float = validated_data[1]
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
        """
        Gives the analyzed stats of the data batch.

        Returns
        -------
        dict[str, union[str, int, float]]
            The dictionary containing the analyzed stats of the data batch.
        """
        stats: dict[str, union[str, int, float]] = {}
        for env_var, mesure in self._stats.items():
            if isinstance(mesure, list):
                if len(mesure):
                    stats["avg_" + env_var] = round(
                        sum(mesure) / len(mesure), 1
                    )
            else:
                if mesure != 0:
                    stats[env_var] = mesure
        return stats


class TransactionStream(DataStream):
    """
    A class that represents a transaction stream.
    """
    def __init__(self, stream_id: str, silent_mode: bool = True) -> None:
        """
        Initialized the transaction stream's properties.

        Parameters
        ----------
        stream_id
            The stream's ID.
        silent_mode
            Whether or not the initialization of the stream is announced.
        """
        super().__init__(stream_id)
        if not silent_mode:
            print("initializing transaction stream...")
            print(f"stream ID: {self.stream_id} - type: financial data")

    def add_to_stats(self, op: str, op_val: int) -> None:
        """
        Adds the stats from the processed data to the stream's stats.

        Parameters
        ----------
        op
            The financial operation processed in the data.
        op_val
            The value of the financial operation processed.
        """
        if op not in self._stats.keys():
            self._stats[op] = [op_val]
        else:
            self._stats[op].append(op_val)
        if "operations" in self._stats.keys():
            self._stats["operations"] += 1
        else:
            self._stats["operations"] = 1

    def reset_stats(self) -> None:
        """
        Resets the stream's stats in between batches.
        """
        for prev_stat in self._stats.keys():
            if isinstance(self._stats[prev_stat], list):
                self._stats[prev_stat] = []
            else:
                self._stats[prev_stat] = 0

    def validate_batch(self, data: any) -> tuple[str, int]:
        """
        Verifies whether or not the data is of the correct format.

        Parameters
        ----------
        data
            The data to validate.

        Returns
        -------
        tuple[str, int | float]
            The verified data separated as financial operation and value.

        Raises
        ------
        TypeError:
            Raised if the data given isn't formatted correctly.
        """
        if (match := re.match("([a-z]+):([0-9]+)", data, re.I)):
            op: str = match.group(1)
            op_val: int = int(match.group(2))
            return op, op_val
        else:
            raise TypeError(
                "invalid type for financial data "
                "(string, int required)"
                " - [REJECTED]\n"
            )

    def process_batch(self, data_batch: list[any]) -> str:
        """
        Processed the data batch given as parameter.

        Parameters
        ----------
        data_batch
            The data batch to process.

        Returns
        -------
        str
            The processed data batch.
        """
        self.reset_stats()
        for data in data_batch:
            try:
                validated_data: tuple[
                    str, int
                ] = self.validate_batch(data)
            except TypeError as te:
                print(f"caught TypeError: {te}")
            else:
                self.add_to_stats(validated_data[0], validated_data[1])
        return f"processing transaction batch: {data_batch}"

    def filter_data(
        self,
        data_batch: list[any],
        criteria: optional[str] = None
    ) -> list[any]:
        """
        Filters a data batch based on a specific criteria.

        Parameters
        ----------
        data_batch
            The data batch to filter.
        criteria
            The criteria used to filter the batch.

        Returns
        -------
        list[any]
            The filtered data batch.
        """
        if not criteria:
            return data_batch
        filtered_batch: list[any] = []
        for data in data_batch:
            try:
                validated_data: tuple[
                    str, int
                ] = self.validate_batch(data)
            except TypeError as te:
                print(f"caught TypeError: {te}")
            else:
                op: str = validated_data[0]
                op_val: int = validated_data[1]
                if (
                    criteria == "high-priority" and op_val >= 150
                ) or criteria == op or criteria == str(op_val):
                    filtered_batch.append(op+":"+str(op_val))
        return filtered_batch

    def get_stats(self) -> dict[str, union[str, int, float]]:
        """
        Gives the analyzed stats of the data batch.

        Returns
        -------
        dict[str, union[str, int, float]]
            The dictionary containing the analyzed stats of the data batch.
        """
        stats: dict[str, any] = {}
        stats["net_flow"] = 0
        for op, op_val in self._stats.items():
            if isinstance(op_val, list) and len(op_val):
                if op == "buy":
                    stats["net_flow"] += sum(op_val)
                elif op == "sell":
                    stats["net_flow"] -= sum(op_val)
            else:
                if op_val != 0:
                    stats[op] = op_val
        if stats["net_flow"] >= 0:
            stats["net_flow"] = "+" + str(stats["net_flow"])
        else:
            stats["net_flow"] = "-" + str(stats["net_flow"])
        return stats


class EventStream(DataStream):
    """
    A class that represents an event stream.
    """
    def __init__(self, stream_id: str, silent_mode: bool = True) -> None:
        """
        Initialized the event stream's properties.

        Parameters
        ----------
        stream_id
            The stream's ID.
        silent_mode
            Whether or not the initialization of the stream is announced.
        """
        super().__init__(stream_id)
        if not silent_mode:
            print("initializing event stream...")
            print(f"stream ID: {self.stream_id} - type: system events")

    def add_to_stats(self, event: str) -> None:
        """
        Adds the stats from the processed data to the stream's stats.

        Parameters
        ----------
        event
            The event processed in the data.
        """
        if event not in self._stats.keys():
            self._stats[event] = 1
        else:
            self._stats[event] += 1
        if "events" in self._stats.keys():
            self._stats["events"] += 1
        else:
            self._stats["events"] = 1

    def reset_stats(self) -> None:
        """
        Resets the stream's stats in between batches.
        """
        for prev_stat in self._stats.keys():
            self._stats[prev_stat] = 0

    def validate_batch(self, data) -> str:
        """
        Verifies whether or not the data is of the correct format.

        Parameters
        ----------
        data
            The data to validate.

        Returns
        -------
        tuple[str, int | float]
            The verified data separated as a system event.

        Raises
        ------
        TypeError:
            Raised if the data given isn't formatted correctly.
        """
        if not isinstance(data, str):
            raise TypeError(
                "invalid type for system events "
                "(string required)"
                " - [REJECTED]\n"
            )
        else:
            return data

    def process_batch(self, data_batch: list[any]) -> str:
        """
        Processed the data batch given as parameter.

        Parameters
        ----------
        data_batch
            The data batch to process.

        Returns
        -------
        str
            The processed data batch.
        """
        self.reset_stats()
        for data in data_batch:
            try:
                event: str = self.validate_batch(data)
            except TypeError as te:
                print(f"caught TypeError: {te}")
            else:
                self.add_to_stats(event)
        return f"processing event batch: {data_batch}"

    def filter_data(
        self,
        data_batch: list[any],
        criteria: optional[str] = None
    ) -> list[any]:
        """
        Filters a data batch based on a specific criteria.

        Parameters
        ----------
        data_batch
            The data batch to filter.
        criteria
            The criteria used to filter the batch.

        Returns
        -------
        list[any]
            The filtered data batch.
        """
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
                ) or criteria == event:
                    filtered_batch.append(event)
        return filtered_batch

    def get_stats(self) -> dict[str, union[str, int, float]]:
        """
        Gives the analyzed stats of the data batch.

        Returns
        -------
        dict[str, union[str, int, float]]
            The dictionary containing the analyzed stats of the data batch.
        """
        stats: dict[str, union[str, int, float]] = {
            e: nb for e, nb in self._stats.items()
        }
        return stats


class StreamProcessor:
    """
    A class that represents a stream processor.
    """
    def process_stream(
        self,
        data_batch: list[any],
        criteria: optional[str] = None
    ) -> dict[str, int]:
        """
        Processes a batch of mixed data and redirects it to the appropriate stream.

        Parameters
        ----------
        data_batch
            The mixed data batch to process.
        criteria
            The optional criteria to filter the data.

        Returns
        -------
        dict[str, int]
            The dictionary containing the results of each stream processing.
        """
        results: dict[str, any] = {}
        sensor = SensorStream("R2D2")
        sensor_data_batch: list[any] = []
        transaction = TransactionStream("K-Tching")
        trans_data_batch: list[any] = []
        event = EventStream("E-T")
        event_data_batch: list[any] = []
        for data in data_batch:
            if "buy" in data or "sell" in data:
                trans_data_batch.append(data)
            elif "temp" in data or "humidity" in data or "pressure" in data:
                sensor_data_batch.append(data)
            elif (
                "login" in data
            ) or (
                "error" in data
            ) or (
                "warning" in data
            ) or (
                "logout" in data
            ):
                event_data_batch.append(data)
            else:
                print(
                    f"error: this data {data} doesn't correspond "
                    "to a specific data processor - [IGNORED]\n"
                )
        sensor.process_batch(
            sensor.filter_data(sensor_data_batch, criteria)
        )
        transaction.process_batch(
            transaction.filter_data(trans_data_batch, criteria)
        )
        event.process_batch(
            event.filter_data(event_data_batch, criteria)
        )
        results["sensor"] = sensor.get_stats()["readings"]
        results["transaction"] = transaction.get_stats()["operations"]
        results["event"] = event.get_stats()["events"]
        return results


def main() -> None:
    """
    Makes use of different data streams
    built on the same base to process data properly,
    thus testing the polymorphic behavior of the streams.
    """
    print("=== CODE NEXUS - POLYMORPHIC STREAM SYSTEM ===\n")
    sensor_stream: SensorStream = SensorStream("SENSOR_001", False)
    print(sensor_stream.process_batch(SENSOR_BATCH))
    sensor_stats: dict[str, union[str, int, float]] = sensor_stream.get_stats()
    print(
        f"sensor analysis: {sensor_stats['readings']} readings processed, "
        f"avg temp: {sensor_stats['avg_temp']}°C\n"
    )
    trans_stream = TransactionStream("TRANS_001", False)
    print(trans_stream.process_batch(TRANS_BATCH))
    trans_stats: dict[str, union[str, int, float]] = trans_stream.get_stats()
    print(
        f"transaction analysis: {trans_stats['operations']} operations, "
        f"net flow: {trans_stats['net_flow']} units\n"
    )
    event_stream = EventStream("EVENT_001", False)
    print(event_stream.process_batch(EVENT_BATCH))
    event_stats: dict[str, union[str, int, float]] = event_stream.get_stats()
    print(
        f"event analysis: {event_stats['events']} events, "
        f"{event_stats['error']} error detected\n"
    )
    print("=== Polymorphic Stream Processing ===")
    print("processing mixed stream types through unified interface...\n")
    stream_proc: StreamProcessor = StreamProcessor()
    results: dict[str, int] = stream_proc.process_stream(MIXED_BATCH)
    print("batch 1 results: ")
    print(f"- sensor data: {results['sensor']} readings processed")
    print(f"- transaction data: {results['transaction']} operations processed")
    print(f"- event data: {results['event']} events processed")
    print("\nstream filtering active: high-priority data only")
    results = stream_proc.process_stream(MIXED_BATCH, "high-priority")
    print(
        f"filtered results: "
        f"{results['sensor']} critical sensor alerts, "
        f"{results['transaction']} large transaction, "
        f"{results['event']} errors or warnings\n"
    )
    print("all streams processed successfully - nexus throughput optimal")


if __name__ == "__main__":
    main()
