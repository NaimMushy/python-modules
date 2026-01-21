from abc import ABC, abstractmethod
from typing import Any as any
import re


NUM_TEST: list[int] = [16, 4, 32, 44]
TEXT_TEST: str = "i hate whoever thought this module was a good idea"
LOG_TEST: str = "ERROR: my brain is overloading"


class DataProcessor(ABC):
    """
    A class that represents a data processor.
    """
    def __init__(self, output_mode: str = "concise") -> None:
        """
        Initializes the data processor's properties.

        Parameters
        ----------
        output_mode
            The type of output (verbose or concise).
        """
        self.output_mode: str = output_mode
        if output_mode == "verbose":
            print(f"initializing {self.__class__.__name__}...")

    @abstractmethod
    def process(self, data: any) -> str:
        """
        Processes any type of data.

        Parameters
        ----------
        data
            The data to process.

        Returns
        -------
        str
            The processed data.
        """
        pass

    @abstractmethod
    def validate(self, data: any) -> bool:
        """
        Checks whether or not the given data is of the correct type.

        Parameters
        ----------
        data
            The data to verify.

        Returns
        -------
        bool
            True if the data is of the correct type, False otherwise.
        """
        pass

    def format_output(self, result: str) -> str:
        """
        Formats the output string based on the output mode.

        Parameters
        ----------
        result
            The processed data.

        Returns
        -------
        str
            The formatted output string.
        """
        if self.output_mode == "verbose":
            return "output: " + result
        return result


class NumericProcessor(DataProcessor):
    """
    A class that represents a processor for numeric data.
    """
    def process(self, data: any) -> str:
        """
        Processes numeric data.

        Parameters
        ----------
        data
            The numeric data to process.

        Returns
        -------
        str
            The processed numeric data.

        Raises
        ------
        TypeError:
            Raised if the given data is not numeric.
        """
        if self.output_mode == "verbose":
            print(f"processing data: {data}")
        if self.validate(data):
            if not isinstance(data, list):
                data = list(data)
            result_string: str = (
                f"processed {len(data)} numeric values, sum={sum(data)}, "
                f"avg = {round(sum(data) / len(data), 1)}"
            )
            return result_string
        else:
            raise TypeError("invalid type for literal integer - [REJECTED]\n")

    def validate(self, data: any) -> bool:
        """
        Checks whether or not the given data is numeric.

        Parameters
        ----------
        data
            The data to verify.

        Returns
        -------
        bool
            True if the data is numeric, False otherwise.
        """
        if isinstance(data, list):
            if (isinstance(d, int) for d in data):
                if self.output_mode == "verbose":
                    print("validation: numeric data verified")
                return True
            return False
        elif isinstance(data, int):
            if self.output_mode == "verbose":
                print("validation: numeric data verified")
            return True
        else:
            return False


class TextProcessor(DataProcessor):
    """
    A class that represents a processor for text data.
    """
    def process(self, data: any) -> str:
        """
        Processes text data.

        Parameters
        ----------
        data
            The text data to process.

        Returns
        -------
        str
            The processed text data.

        Raises
        ------
        TypeError:
            Raised if the data is not text.
        """
        if self.output_mode == "verbose":
            print(f"processing data: {data}")
        if self.validate(data):
            result_string: str = (
                f"processed text: {len(data)} characters, "
                f"{len(data.split())} words"
            )
            return result_string
        else:
            raise TypeError("invalid type for literal string - [REJECTED]\n")

    def validate(self, data: any) -> bool:
        """
        Checks whether or not the given data is text.

        Parameters
        ----------
        data
            The data to verify.

        Returns
        -------
        bool
            True if the data is text, False otherwise.
        """
        if isinstance(data, str):
            if self.output_mode == "verbose":
                print("validation: text data verified")
            return True
        else:
            return False


class LogProcessor(DataProcessor):
    """
    A class that represents a processor for log entries.
    """
    def process(self, data: any) -> str:
        """
        Processes log entries.

        Parameters
        ----------
        data
            The log entry to process.

        Returns
        -------
        str
            The processed log entry.

        Raises
        ------
        TypeError:
            Raised if the given data is not a log entry.
        """
        if self.output_mode == "verbose":
            print(f"processing data: {data}")
        if self.validate(data):
            if (match := re.match("([a-z]+):([a-z ]+)", data, re.I)):
                log_type: str = match.group(1)
                if log_type == "ERROR":
                    result_string: str = (
                        f"[ALERT] {log_type} level detected: "
                        f"{match.group(2)}"
                    )
                else:
                    result_string = (
                        f"[{log_type}] {log_type} level detected: "
                        f"{match.group(2)}"
                    )
                return result_string
            else:
                raise TypeError("invalid type for log entry - [REJECTED]\n")
        else:
            raise TypeError("invalid type for log entry - [REJECTED]\n")

    def validate(self, data: any) -> bool:
        """
        Checks whether or not the given data is a log entry.

        Parameters
        ----------
        data
            The data to verify.

        Returns
        -------
        bool
            True if the data is a log entry, False otherwise.
        """
        if isinstance(data, str):
            if (re.match("([a-z]+):([a-z ]+)", data, re.I)):
                if self.output_mode == "verbose":
                    print("validation: log entry verified")
                return True
            else:
                return False
        else:
            return False


def main() -> None:
    """
    Tests different data processors.
    """
    print("=== CODE NEXUS - DATA PROCESSOR FOUNDATION ===\n")
    num_proc: NumericProcessor = NumericProcessor("verbose")
    try:
        print(f"{num_proc.format_output(num_proc.process(NUM_TEST))}\n")
    except TypeError as te:
        print(f"caught TypeError: {te}")
    text_proc: TextProcessor = TextProcessor("verbose")
    try:
        print(f"{text_proc.format_output(text_proc.process(TEXT_TEST))}\n")
    except TypeError as te:
        print(f"caught TypeError: {te}")
    log_proc: LogProcessor = LogProcessor("verbose")
    try:
        print(f"{log_proc.format_output(log_proc.process(LOG_TEST))}\n")
    except TypeError as te:
        print(f"caught TypeError: {te}")
    print("=== Polymorphic Processing Demo ===\n")
    print("processing multiple data types through same interface...")
    num_proc.output_mode = "concise"
    text_proc.output_mode = "concise"
    log_proc.output_mode = "concise"
    try:
        result: str = (
            "result 1: "
            + num_proc.format_output(num_proc.process(NUM_TEST))
        )
    except TypeError as te:
        print(f"caught TypeError: {te}")
    else:
        print(result)
    try:
        result = (
            "result 2: "
            + text_proc.format_output(text_proc.process(TEXT_TEST))
        )
    except TypeError as te:
        print(f"caught TypeError: {te}")
    else:
        print(result)
    try:
        result = (
            "result 3: "
            + log_proc.format_output(log_proc.process(LOG_TEST))
        )
    except TypeError as te:
        print(f"caught TypeError: {te}")
    else:
        print(result)
    print("\nfoundation system online - nexus ready for advanced streams")


if __name__ == "__main__":
    main()
