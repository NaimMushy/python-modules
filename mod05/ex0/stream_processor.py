from abc import ABC, abstractmethod
from typing import Any as any
import re


class DataProcessor(ABC):

    def __init__(self) -> None:
        print(
            "Initializing "
            f"{self.__class__.__name__.replace('Processor', '')} "
            "Processor..."
        )

    @abstractmethod
    def process(self, data: any) -> str:
        pass

    @abstractmethod
    def validate(self, data: any) -> bool:
        pass

    def format_output(self, result: str) -> str:
        return "Output: " + result


class NumericProcessor(DataProcessor):

    def process(self, data: any) -> str:

        if self.validate(data):
            if not isinstance(data, list):
                data = [data]
            return (
                "Processed "
                f"{len(data)} numeric value{'s' if len(data) > 1 else ''}, "
                f"sum={sum(data)}, "
                f"avg = {round(sum(data) / len(data), 1)}"
            )

        else:
            raise TypeError("Invalid type for literal integer - [REJECTED]")

    def validate(self, data: any) -> bool:

        if isinstance(data, list):
            return (
                True if (isinstance(d, int) for d in data)
                else False
            )

        elif isinstance(data, int):
            return True

        else:
            return False


class TextProcessor(DataProcessor):

    def process(self, data: any) -> str:

        if self.validate(data):
            word_count: int = len(data.split())
            return (
                f"Processed text: {len(data)} "
                f"character{'s' if len(data) > 1 else ''}, "
                f"{word_count} word{'s' if word_count > 1 else ''}"
            )

        else:
            raise TypeError("Invalid type for literal string - [REJECTED]")

    def validate(self, data: any) -> bool:

        if isinstance(data, str):
            return True

        else:
            return False


class LogProcessor(DataProcessor):

    def process(self, data: any) -> str:

        if self.validate(data):

            if (match := re.match("([a-z]+): ([a-z ]+)", data, re.I)):
                log_type: str = match.group(1)
                return (
                    f"[{log_type if log_type != 'ERROR' else 'ALERT'}] "
                    f"{log_type} level detected: "
                    f"{match.group(2)}"
                )

            else:
                raise TypeError("Invalid type for log entry - [REJECTED]")

        else:
            raise TypeError("Invalid type for log entry - [REJECTED]")

    def validate(self, data: any) -> bool:

        if isinstance(data, str):
            return (
                True if (re.match("([a-z]+):([a-z ]+)", data, re.I))
                else False
            )

        else:
            return False


def single_processing(proc: DataProcessor, data: any) -> None:

    print(f"Processing data: {data}")
    try:
        print(
            f"Validation: {proc.__class__.__name__.replace('Processor', '')} "
            f"{'entry' if isinstance(proc, LogProcessor) else 'data'} "
            f"{'verified' if proc.validate(data) else 'rejected'}"
        )
        print(f"{proc.format_output(proc.process(data))}\n")
    except TypeError as te:
        print(f"Caught TypeError: {te}")


def multiple_processing(
    processors: list[DataProcessor],
    data: list[any]
) -> None:

    print("Processing multiple data types through same interface...")

    for proc in range(len(processors)):
        try:
            print(f"Result {proc + 1}: {processors[proc].process(data[proc])}")
        except TypeError as te:
            print(f"Caught TypeError: {te}")


def main() -> None:

    print("=== CODE NEXUS - DATA PROCESSOR FOUNDATION ===\n")

    num_test: any = "blabla"
    text_test: any = [4, 5, 8]
    log_test: any = "not a log entry"

    num_proc: NumericProcessor = NumericProcessor()
    single_processing(num_proc, num_test)

    text_proc: TextProcessor = TextProcessor()
    single_processing(text_proc, text_test)

    log_proc: LogProcessor = LogProcessor()
    single_processing(log_proc, log_test)

    print("=== Polymorphic Processing Demo ===\n")

    multiple_processing(
        [num_proc, text_proc, log_proc],
        [num_test, text_test, log_test]
    )

    print("\nFoundation system online - Nexus ready for advanced streams")


if __name__ == "__main__":
    main()
