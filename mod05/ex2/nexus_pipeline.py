from abc import ABC
from typing import Protocol
from typing import Any as any
from typing import Generator
import re
import random
import time


class ProcessingStage(Protocol):

    def process(self, data: any) -> any:
        pass


class InputStage:

    def process(self, data: any) -> dict:

        match data["adapter"]:

            case "json":
                return self.input_json(data["rawdata"])
            case "csv":
                return self.input_csv(data["rawdata"])
            case "sensor":
                return self.input_sensor(data["rawdata"])
            case _:
                raise TypeError(
                    "Invalid data - Doesn't correspond to any of the adapters"
                    " - [REJECTED]"
                )

    def input_json(self, data: any) -> dict:

        validated_dict: dict = {"adapter": "json"}

        if isinstance(data, (list, Generator)):

            for d in data:

                if not isinstance(d, str) or not (
                    match := re.match("([a-z]+):([a-z0-9.]+)", d, re.I)
                ):
                    raise TypeError(
                        "Invalid format for "
                        "JSON data - [REJECTED]"
                    )

                if match.group(1) not in validated_dict.keys():
                    validated_dict[match.group(1)] = []

                validated_dict[
                    match.group(1)
                ].append(match.group(2))

        elif isinstance(data, dict):

            del data["adapter"]

            for key, val in data.items():

                if (
                    not isinstance(key, str)
                    or not isinstance(val, (str, int, float, list))
                ):
                    raise TypeError(
                        "Invalid format for "
                        "JSON data - [REJECTED]"
                    )

                if key not in validated_dict.keys():
                    validated_dict[key] = []

                validated_dict[key].append(val)

        else:
            raise TypeError("Invalid format for JSON data - [REJECTED]")

        return validated_dict

    def input_csv(self, data: any) -> dict:

        validated_dict: dict = {"adapter": "csv"}

        if isinstance(data, str):

            data = data.split(",")

            for d in data:

                if not (match := re.match("([a-z]+)", d, re.I)):
                    raise TypeError("Invalid format for CSV data - [REJECTED]")

                if match.group(1) not in validated_dict.keys():
                    validated_dict[match.group(1)] = 0

                validated_dict[match.group(1)] += 1

        elif isinstance(data, dict):

            new_dict: dict = {
                key: val for key, val in data.items()
                if key != "adapter"
            }

            for key, val in new_dict.items():

                if not (
                    isinstance(key, str)
                    and isinstance(val, (str, int, float, list))
                ):
                    raise TypeError("Invalid format for CSV data - [REJECTED]")

                validated_dict[key] = (
                    int(val) if isinstance(val, (int, float))
                    else 1
                )

        else:
            raise TypeError("Invalid format for CSV data - [REJECTED]")

        return validated_dict

    def input_sensor(self, data: any) -> dict:

        validated_dict: dict = {"adapter": "sensor"}

        if not isinstance(data, Generator):
            raise TypeError("Invalid format for sensor data - [REJECTED]")

        for d in data:

            if (match := re.match("([a-z]+):([a-z0-9.]+)", d, re.I)):

                if match.group(1) not in validated_dict.keys():
                    validated_dict[match.group(1)] = []

                validated_dict[match.group(1)].append(match.group(2))

            elif (match := re.match("([a-z]+)", d, re.I)):

                if match.group(1) not in validated_dict.keys():
                    validated_dict[match.group(1)] = 0

                validated_dict[match.group(1)] += 1

            else:
                raise TypeError(
                    "Invalid format for "
                    "sensor data - [REJECTED]"
                )

        return validated_dict


class TransformStage:

    def process(self, data: any) -> dict:

        match data["adapter"]:

            case "json":
                return self.transform_json(data)
            case "csv":
                return self.transform_csv(data)
            case "sensor":
                return self.transform_sensor(data)
            case _:
                raise TypeError(
                    "Invalid data - Doesn't correspond to any of the adapters"
                    " - [REJECTED]"
                )

    def get_range(self, sensor_type: str, value: str) -> str:

        match sensor_type:

            case "temp":
                sensor_range: tuple[int, int] = (-10, 40)
            case "pressure":
                sensor_range = (0, 2000)
            case "humidity":
                sensor_range = (10, 80)
            case _:
                sensor_range = (0, 100)

        return (
            "normal"
            if sensor_range[0] <= float(value) <= sensor_range[1]
            else "critical"
        )

    def transform_json(self, data: any) -> dict:

        if not isinstance(data, dict):
            raise TypeError(
                "Invalid format for "
                "JSON data - [REJECTED]"
            )

        trans_dict: dict = {"adapter": "json"}

        for key, val in data.items():

            if val[0] == "temp":
                trans_dict[key] = "temperature"

            elif key == "value":

                if "sensor" in data.keys():
                    trans_dict[key] = 0

                    for value in val:
                        trans_dict["range"] = self.get_range(
                            data["sensor"], value
                        )
                        trans_dict[key] += round(float(value), 1)

            elif key == "unit":

                trans_dict[key] = (
                    ("°" + val[0])
                    if val[0] == "C" or val[0] == "F"
                    else val[0]
                )

            else:
                trans_dict[key] = val

        return trans_dict

    def transform_csv(self, data: any) -> dict:

        if not isinstance(data, dict):
            raise TypeError(
                "Invalid format for "
                "CSV data - [REJECTED]"
            )

        trans_dict: dict = {"adapter": "csv"}

        if "user" not in data.keys() and "user_activity" not in data.keys():
            trans_dict["user_activity"] = "not detected"

        for key, val in data.items():

            if "user" in key:
                trans_dict["user_activity"] = (
                    "logged" if val > 0
                    else "not detected"
                )

            elif key != "adapter":
                trans_dict[key] = val

        return trans_dict

    def transform_sensor(self, data: any) -> dict:

        if not isinstance(data, dict):
            raise TypeError(
                "Invalid format for "
                "sensor data - [REJECTED]"
            )

        del data["adapter"]
        trans_dict: dict = {
            "adapter": "sensor",
            "readings": 0
        }

        for key, val in data.items():

            if isinstance(val, list):

                for mesure in val:

                    if self.get_range(key, mesure) == "critical":
                        if "critical" not in trans_dict.keys():
                            trans_dict["critical"] = []
                        trans_dict["critical"].append(
                            key + ":" + str(round(float(mesure), 1))
                        )

                    if "avg_"+key not in trans_dict.keys():
                        trans_dict["avg_"+key] = 0

                    trans_dict["avg_"+key] += round(float(mesure), 1)
                    trans_dict["readings"] += 1

                if len(val) > 1 and "avg_"+key in trans_dict.keys():

                    trans_dict["avg_"+key] = round(
                        trans_dict["avg_"+key] / len(val), 1
                    )

            else:
                trans_dict[key] = val
                trans_dict["readings"] += val

        if "avg_temp" in trans_dict.keys():
            trans_dict["avg_temp"] = str(trans_dict["avg_temp"]) + "°C"

        if "avg_pressure" in trans_dict.keys():
            trans_dict["avg_pressure"] = str(trans_dict["avg_pressure"]) + "Pa"

        if "avg_humidity" in trans_dict.keys():
            trans_dict["avg_humidity"] = str(trans_dict["avg_humidity"]) + "%"

        return trans_dict


class OutputStage:

    def process(self, data: any) -> str:

        match data["adapter"]:

            case "json":
                return self.output_json(data)
            case "csv":
                return self.output_csv(data)
            case "sensor":
                return self.output_sensor(data)
            case _:
                raise TypeError(
                    "Invalid data - Doesn't correspond to any of the adapters"
                    " - [REJECTED]"
                )

    def output_json(self, data: any) -> str:

        if not isinstance(data, dict):
            raise TypeError(
                "Invalid format for "
                "JSON data - [REJECTED]"
            )

        output_string: str = ""

        del data["adapter"]

        output_string += (
            "Processed sensor reading"
            if "sensor" not in data.keys()
            else f"Processed {data['sensor']} reading"
        )

        output_string += (
            ": No reading value provided"
            if "value" not in data.keys()
            else f": {data['value']}"
        )

        if "unit" in data.keys():
            output_string += data["unit"]

        if "range" in data.keys():
            output_string += f" ({data['range']} range)"

        for key, val in data.items():

            output_string += (
                f" - {key}: {val}"
                if key not in ["sensor", "value", "unit", "range"]
                else ""
            )

        return output_string

    def output_csv(self, data: any) -> str:

        if not isinstance(data, dict):
            raise TypeError(
                "Invalid format for "
                "CSV data - [REJECTED]"
            )

        output_string: str = ""
        output_string += f"User activity {data['user_activity']}: "

        new_dict: dict = {
            key: val for key, val in data.items()
            if key not in ["user_activity", "adapter"]
        }

        if not new_dict:
            output_string += "No additional data provided"
            return output_string

        count: int = 0

        for key, val in new_dict.items():

            count += 1
            output_string += (
                f"{val} {key}"
                + (
                    "s" if isinstance(val, list) or val > 1
                    else ""
                )
                + " processed"
            )
            output_string += (" - " if count < len(new_dict) else "")

        return output_string

    def output_sensor(self, data: any) -> str:

        if not isinstance(data, dict):
            raise TypeError(
                "Invalid format for "
                "sensor data - [REJECTED]"
            )

        output_string: str = f"Stream summary: {data['readings']} readings"

        new_dict: dict = {
            key: val for key, val in data.items()
            if key not in ["adapter", "readings"]
        }

        for key, val in new_dict.items():
            output_string += f" - {key}: {val}"

        return output_string


class ProcessingPipeline(ABC):

    def __init__(self, pipeline_id: str) -> None:

        self.pipeline_id: str = pipeline_id
        self.stages: list[ProcessingStage] = []

    def __repr__(self) -> str:

        return self.__class__.__name__

    def add_stage(self, new_stage: ProcessingStage) -> None:

        self.stages.append(new_stage)

    def process(self, data: any) -> any:

        data_dict: dict = {
            "adapter": "any",
            "rawdata": data
        }

        stage_count: int = 0

        for stage in self.stages:

            stage_count += 1

            try:
                data_dict = stage.process(data_dict)
            except TypeError as te:
                print(f"ERROR detected in stage {stage_count}: {te}")
                return "Error recovery needed"

        return data_dict


class JSONAdapter(ProcessingPipeline):

    def process(self, data: any) -> any:

        data_dict: dict = {
            "adapter": "json",
            "rawdata": data
        }

        stage_count: int = 0

        for stage in self.stages:

            stage_count += 1

            try:
                data_dict = stage.process(data_dict)
            except TypeError as te:
                print(f"ERROR detected in stage {stage_count}: {te}")
                return "Error recovery needed"

        return data_dict


class CSVAdapter(ProcessingPipeline):

    def process(self, data: any) -> any:

        data_dict: dict = {
            "adapter": "csv",
            "rawdata": data
        }

        stage_count: int = 0

        for stage in self.stages:

            stage_count += 1

            try:
                data_dict = stage.process(data_dict)
            except TypeError as te:
                print(f"ERROR detected in stage {stage_count}: {te}")
                return "Error recovery needed"

        return data_dict


class StreamAdapter(ProcessingPipeline):

    def process(self, data: any) -> any:

        data_dict: dict = {
            "adapter": "sensor",
            "rawdata": data
        }

        stage_count: int = 0

        for stage in self.stages:

            stage_count += 1

            try:
                data_dict = stage.process(data_dict)
            except TypeError as te:
                print(f"ERROR detected in stage {stage_count}: {te}")
                return "Error recovery needed"

        return data_dict


class NexusManager:

    def __init__(self) -> None:

        print("Initializing Nexus Manager...")
        print("Pipeline capacity: 1000 streams/second\n")

        self.pipelines: list[ProcessingPipeline] = []
        self.stages: list[ProcessingStage] = []

        print("Creating data processing pipeline...")

        self.stages.append(InputStage())
        print("Stage 1: input validation and parsing")

        self.stages.append(TransformStage())
        print("Stage 2: data transformation and enrichment")

        self.stages.append(OutputStage())
        print("Stage 3: output formatting and delivery\n")

    def clear_pipelines(self) -> None:

        for pipeline in self.pipelines:
            pipeline.stages = []

    def add_stages_to_pipeline(
        self,
        pipeline: ProcessingPipeline,
        nb_stages: int
    ) -> None:

        for index in range(nb_stages):
            pipeline.add_stage(self.stages[index])

    def add_pipeline(self, new_pipeline: ProcessingPipeline) -> None:

        self.pipelines.append(new_pipeline)

    def multi_proc(
        self,
        data: dict[str, any]
    ) -> None:

        print("=== Multi-Format Data Processing ===\n")

        transform_msg: dict[str, str] = {
            "json": "Enriched with metadata and validation",
            "csv": "Parsed and structured data",
            "stream": "Aggregated and filtered"
        }

        for pipeline in self.pipelines:

            self.add_stages_to_pipeline(pipeline, 3)
            data_type: str = pipeline.__repr__().replace("Adapter", "")
            output: str = pipeline.process(data[data_type.lower()])

            if output.startswith("Error"):
                self.error_recovery(output, pipeline)
                break

            print(f"Processing {data_type} data through pipeline...")

            input_data: any = (
                data[data_type.lower()]
                if data_type != 'Stream'
                else 'Real-time sensor stream'
            )

            print(f"Input: {input_data}")
            print(f"Transform: {transform_msg[data_type.lower()]}")
            print(f"Output: {output}\n")

        self.clear_pipelines()

    def pipeline_chaining(
        self,
        input_data: any,
    ) -> None:

        print("=== Pipeline Chaining Demo ===")

        proc_time_start: float = time.time()
        output: any = input_data

        if not isinstance(input_data, Generator):
            record_count: int = (
                (len(input_data))
                if isinstance(input_data, list)
                else len(input_data.split(","))
            )

        for pipeline in self.pipelines:

            self.add_stages_to_pipeline(
                pipeline,
                (2 if pipeline != self.pipelines[-1] else 3)
            )

            output = pipeline.process(output)

            if isinstance(output, str) and output.startswith("Error"):
                self.error_recovery(output, pipeline)

            else:
                if pipeline != self.pipelines[0]:
                    print(" -> ", end="")
                elif "readings" in output.keys():
                    record_count = output["readings"]
                    del output["readings"]
                print(f"Pipeline {pipeline}", end="")

        print("")

        proc_time_end: float = time.time()

        print("Data flow: Raw -> Processed -> Analyzed -> Stored\n")
        print(
            f"Chain result: {record_count} records "
            "processed through 3-stage pipeline"
        )
        print(
            f"Performance: 95% efficiency, "
            f"{round(proc_time_end - proc_time_start, 2)} "
            "total processing time\n"
        )

        self.clear_pipelines()

    def error_recovery(
        self,
        error_str: str,
        pipeline: ProcessingPipeline
    ) -> None:

        print(f"{error_str} - PIPELINE <{pipeline.pipeline_id}>")
        print("Recovery initiated: Switching to backup processor")
        print("Recovery successful: Pipeline restored, processing resumed\n")


def generate_sensor(
    nb_readings: int,
    input_type: str
) -> Generator[str, None, None]:

    sensor_list: list[str] = ["temp", "pressure", "humidity"]
    csv_list: list[str] = ["user", "action", "timestamp", "login", "logout"]

    while nb_readings > 0:

        yield (
            (
                random.choice(sensor_list)
                + ":"
                + str(round(random.uniform(0, 200), 1))
            )
            if input_type == "sensor"
            else random.choice(csv_list)
        )

        nb_readings -= 1


def main() -> None:

    print("=== CODE NEXUS - ENTERPRISE PIPELINE SYSTEM ===\n")

    data: dict[str, any] = {
        "json": ["sensor:temp", "value:23.5", "unit:C"],
        "csv": "user,action,timestamp",
        "stream": generate_sensor(4, "sensor")
    }

    nexus_mngr = NexusManager()

    pipelines: list[ProcessingPipeline] = [
        StreamAdapter("Stream_001"),
        CSVAdapter("CSV_001"),
        JSONAdapter("JSON_001")
    ]

    for pipeline in pipelines:
        nexus_mngr.add_pipeline(pipeline)

    nexus_mngr.multi_proc(data)

    print("Simulating pipeline failure in multi-format data processing...\n")

    data["csv"] = 404
    nexus_mngr.multi_proc(data)

    data["stream"] = generate_sensor(52, "csv")
    nexus_mngr.pipeline_chaining(data["stream"])

    nexus_mngr.pipelines = []

    pipelines[1], pipelines[2] = JSONAdapter("JSON_001"), CSVAdapter("CSV_001")

    for pipeline in pipelines:
        nexus_mngr.add_pipeline(pipeline)

    data["stream"] = generate_sensor(7, "sensor")
    nexus_mngr.pipeline_chaining(data["stream"])

    print("=== Error Recovery Test ===\n")

    print("Simulating pipeline failure...\n")

    data["stream"], data["json"] = generate_sensor(7, "sensor"), 404
    nexus_mngr.multi_proc(data)

    print("Nexus integration complete - All systems operational")


if __name__ == "__main__":
    main()
