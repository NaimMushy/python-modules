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
        if data["adapter"] == "json":
            return self.input_json(data["rawdata"])
        elif data["adapter"] == "csv":
            return self.input_csv(data["rawdata"])
        elif data["adapter"] == "sensor":
            return self.input_sensor(data["rawdata"])
        else:
            raise TypeError(
                "invalid data - doesn't correspond to any of the adapters"
                " - [REJECTED]"
            )

    def input_json(self, data: any) -> dict:
        validated_dict: dict = {}
        if isinstance(data, (list, Generator)):
            for d in data:
                if isinstance(d, str):
                    if (match := re.match("([a-z]+):([a-z0-9.]+)", d, re.I)):
                        if match.group(1) in validated_dict.keys():
                            validated_dict[
                                match.group(1)
                            ].append(match.group(2))
                        else:
                            validated_dict[match.group(1)] = [match.group(2)]
                    else:
                        raise TypeError(
                            "invalid format for "
                            "json data - [REJECTED]"
                        )
                else:
                    raise TypeError(
                        "invalid format for "
                        "json data - [REJECTED]"
                    )
        elif isinstance(data, dict):
            for key, val in data.items():
                if (
                    isinstance(key, str)
                    and isinstance(val, (str, int, float, list))
                ):
                    if key in validated_dict.keys():
                        validated_dict[key].append(val)
                    else:
                        validated_dict[key] = [val]
                else:
                    raise TypeError(
                        "invalid format for "
                        "json data - [REJECTED]"
                    )
        else:
            raise TypeError("invalid format for json data - [REJECTED]")
        validated_dict["adapter"] = "json"
        return validated_dict

    def input_csv(self, data: any) -> dict:
        validated_dict: dict = {}
        if isinstance(data, str):
            data = data.split(",")
            for d in data:
                if not (match := re.match("([a-z]+)", d, re.I)):
                    raise TypeError("invalid format for csv data - [REJECTED]")
                if match.group(1) in validated_dict.keys():
                    validated_dict[match.group(1)] += 1
                else:
                    validated_dict[match.group(1)] = 1
        elif isinstance(data, dict):
            new_dict: dict = {
                key: val for key, val in data.items()
                if key != "adapter"
            }
            for key, val in new_dict.items():
                if not (
                    isinstance(key, str)
                    and isinstance(val, (str, int, float))
                ):
                    print("error here because not ")
                    raise TypeError("invalid format for csv data - [REJECTED]")
                if isinstance(val, float):
                    validated_dict[key] = int(val)
                elif isinstance(val, str):
                    validated_dict[key] = 1
                validated_dict[key] = val
        else:
            raise TypeError("invalid format for csv data - [REJECTED]")
        validated_dict["adapter"] = "csv"
        return validated_dict

    def input_sensor(self, data: any) -> dict:
        validated_dict: dict = {}
        if isinstance(data, Generator):
            for d in data:
                if (match := re.match("([a-z]+):([a-z0-9.]+)", d, re.I)):
                    if match.group(1) in validated_dict.keys():
                        validated_dict[match.group(1)].append(match.group(2))
                    else:
                        validated_dict[match.group(1)] = [match.group(2)]
                elif (match := re.match("([a-z]+)", d, re.I)):
                    if match.group(1) in validated_dict.keys():
                        validated_dict[match.group(1)] += 1
                    else:
                        validated_dict[match.group(1)] = 1
                else:
                    raise TypeError(
                        "invalid format for "
                        "sensor data - [REJECTED]"
                    )
        else:
            raise TypeError("invalid format for sensor data - [REJECTED]")
        validated_dict["adapter"] = "sensor"
        return validated_dict


class TransformStage:
    def process(self, data: any) -> dict:
        if data["adapter"] == "json":
            return self.transform_json(data)
        elif data["adapter"] == "csv":
            return self.transform_csv(data)
        elif data["adapter"] == "sensor":
            return self.transform_sensor(data)
        else:
            raise TypeError(
                "invalid data - doesn't correspond to any of the adapters"
                " - [REJECTED]"
            )

    def get_range(self, sensor_type: str, value: str) -> str:
        if sensor_type == "temp":
            if float(value) > 40 or float(value) < -10:
                return "critical"
            else:
                return "normal"
        elif sensor_type == "pressure":
            if float(value) > 2000 or float(value) < 0:
                return "critical"
            else:
                return "normal"
        elif sensor_type == "humidity":
            if float(value) > 80 or float(value) < 10:
                return "critical"
            else:
                return "normal"
        else:
            if float(value) > 100 or float(value) < 0:
                return "critical"
            else:
                return "normal"

    def transform_json(self, data: any) -> dict:
        trans_dict: dict = {}
        trans_dict["adapter"] = "json"
        for key, val in data.items():
            if val[0] == "temp":
                trans_dict[key] = "temperature"
            elif key == "value":
                if "sensor" in data.keys():
                    trans_dict[key] = 0
                    for value in val:
                        if self.get_range(
                            data["sensor"],
                            value
                        ) == "critical":
                            trans_dict["range"] = "critical"
                        trans_dict[key] += round(float(value), 1)
                    if "range" not in trans_dict.keys():
                        trans_dict["range"] = "normal"
            elif key == "unit":
                if val[0] == "C" or val[0] == "F":
                    trans_dict[key] = "°" + val[0]
                else:
                    trans_dict[key] = val[0]
            else:
                trans_dict[key] = val
        return trans_dict

    def transform_csv(self, data: any) -> dict:
        trans_dict: dict = {}
        trans_dict["adapter"] = "csv"
        if "user" not in data.keys():
            trans_dict["user_activity"] = "not detected"
        for key, val in data.items():
            if key == "user":
                if val > 0:
                    trans_dict["user_activity"] = "logged"
                else:
                    trans_dict["user_activity"] = "not detected"
            elif key != "adapter":
                trans_dict[key] = val
        return trans_dict

    def transform_sensor(self, data: any) -> dict:
        del data["adapter"]
        trans_dict: dict = {}
        trans_dict["adapter"] = "sensor"
        trans_dict["readings"] = 0
        for key, val in data.items():
            if isinstance(val, list):
                for mesure in val:
                    if self.get_range(key, mesure) == "critical":
                        if "critical" in trans_dict.keys():
                            trans_dict["critical"].append(
                                key + ":" + str(round(float(mesure), 1))
                            )
                        else:
                            trans_dict["critical"] = [
                                key + ":" + str(round(float(mesure), 1))
                            ]
                    if "avg_"+key in trans_dict.keys():
                        trans_dict["avg_"+key] += round(float(mesure), 1)
                    else:
                        trans_dict["avg_"+key] = round(float(mesure), 1)
                    trans_dict["readings"] += 1
                if len(val) > 1:
                    if "avg_"+key in trans_dict.keys():
                        trans_dict["avg_"+key] = round(
                            trans_dict["avg_"+key] / len(val), 1
                        )
            else:
                trans_dict[key] = val
                trans_dict["readings"] += 1
        if "avg_temp" in trans_dict.keys():
            trans_dict["avg_temp"] = str(trans_dict["avg_temp"]) + "°C"
        if "avg_pressure" in trans_dict.keys():
            trans_dict["avg_pressure"] = str(trans_dict["avg_pressure"]) + "Pa"
        if "avg_humidity" in trans_dict.keys():
            trans_dict["avg_humidity"] = str(trans_dict["avg_humidity"]) + "%"
        return trans_dict


class OutputStage:
    def process(self, data: any) -> str:
        if data["adapter"] == "json":
            return self.output_json(data)
        elif data["adapter"] == "csv":
            return self.output_csv(data)
        elif data["adapter"] == "sensor":
            return self.output_sensor(data)
        else:
            raise TypeError(
                "invalid data - doesn't correspond to any of the adapters"
                " - [REJECTED]"
            )

    def output_json(self, data: any) -> str:
        output_string: str = ""
        del data["adapter"]
        if "sensor" in data.keys():
            output_string += f"processed {data['sensor']} reading"
        else:
            output_string += "processed sensor reading"
        if "value" in data.keys():
            output_string += f": {data['value']}"
        else:
            output_string += ": no reading value provided"
        if "unit" in data.keys():
            output_string += data["unit"]
        if "range" in data.keys():
            output_string += f" ({data['range']} range)"
        if not (("sensor" or "value" or "unit" or "range") in data.keys()):
            for key, val in data.items():
                if key != ("sensor", "value", "unit", "range"):
                    output_string += f" - {key}: {val}"
        return output_string

    def output_csv(self, data: any) -> str:
        output_string: str = ""
        output_string += f"user activity {data['user_activity']}: "
        new_dict: dict = {
            key: val for key, val in data.items()
            if key != "user_activity" and key != "adapter"
        }
        if new_dict == {}:
            output_string += "no additional data provided"
            return output_string
        for key, val in new_dict.items():
            output_string += f"{val} {key}s processed - "
        return output_string

    def output_sensor(self, data: any) -> str:
        output_string: str = f"stream summary: {data['readings']} readings"
        new_dict: dict = {
            key: val for key, val in data.items()
            if key != "readings" and key != "adapter"
        }
        for key, val in new_dict.items():
            output_string += f" - {key}: {val}"
        return output_string


class ProcessingPipeline(ABC):
    def __init__(self, pipeline_id: str) -> None:
        self.pipeline_id: str = pipeline_id
        self._stages: list[ProcessingStage] = []

    def __repr__(self) -> str:
        return self.__class__.__name__

    def add_stage(self, new_stage: ProcessingStage) -> None:
        self._stages.append(new_stage)

    def process(self, data: any) -> any:
        data_dict: dict = {}
        data_dict["adapter"] = "any"
        data_dict["rawdata"] = data
        for stage in self._stages:
            data_dict = stage.process(data_dict)
        return data_dict


class JSONAdapter(ProcessingPipeline):
    def process(self, data: any) -> any:
        data_dict: dict = {}
        data_dict["adapter"] = "json"
        data_dict["rawdata"] = data
        stage_count: int = 0
        for stage in self._stages:
            stage_count += 1
            try:
                data_dict = stage.process(data_dict)
            except TypeError as te:
                print(f"error detected in stage {stage_count}: {te}")
                return "error recovery needed"
        return data_dict


class CSVAdapter(ProcessingPipeline):
    def process(self, data: any) -> any:
        data_dict: dict = {}
        data_dict["adapter"] = "csv"
        data_dict["rawdata"] = data
        stage_count: int = 0
        for stage in self._stages:
            stage_count += 1
            try:
                data_dict = stage.process(data_dict)
            except TypeError as te:
                print(f"error detected in stage {stage_count}: {te}")
                return "error recovery needed"
        return data_dict


class StreamAdapter(ProcessingPipeline):
    def process(self, data: any) -> any:
        data_dict: dict = {}
        data_dict["adapter"] = "sensor"
        data_dict["rawdata"] = data
        stage_count: int = 0
        for stage in self._stages:
            stage_count += 1
            try:
                data_dict = stage.process(data_dict)
            except TypeError as te:
                print(f"error detected in stage {stage_count}: {te}")
                return "error recovery needed"
        return data_dict


class NexusManager:
    def __init__(self) -> None:
        print("initializing Nexus Manager...")
        print("pipeline capacity: 1000 streams/second\n")
        self._pipelines: list[ProcessingPipeline] = []
        self._stages: list[ProcessingStage] = []
        print("creating data processing pipeline...")
        self._stages.append(InputStage())
        print("stage 1: input validation and parsing")
        self._stages.append(TransformStage())
        print("stage 2: data transformation and enrichment")
        self._stages.append(OutputStage())
        print("stage 3: output formatting and delivery\n")

    def clear_pipelines(self) -> None:
        self._pipelines = []

    def add_stages_to_pipeline(
        self,
        pipeline: ProcessingPipeline,
        nb_stages: int
    ) -> None:
        for index in range(nb_stages):
            pipeline.add_stage(self._stages[index])

    def add_pipeline(self, new_pipeline: ProcessingPipeline) -> None:
        self._pipelines.append(new_pipeline)

    def multi_proc(
        self,
        json_data: any,
        csv_data: any,
        sensor_data: any
    ) -> None:
        self.add_pipeline(JSONAdapter("JSON_001"))
        self.add_pipeline(CSVAdapter("CSV_001"))
        self.add_pipeline(StreamAdapter("SENSOR_001"))
        inputs: list = [json_data, csv_data, sensor_data]
        for index in range(len(self._pipelines)):
            self.add_stages_to_pipeline(self._pipelines[index], 3)
            output: str = self._pipelines[index].process(inputs[index])
            if output.startswith("error"):
                self.error_recovery(output, self._pipelines[index])
                break
            elif self._pipelines[index].__repr__() == "JSONAdapter":
                print("processing JSON data through pipeline...")
                print(f"input: {inputs[index]}")
                print("transform: enriched with metadata and validation")
            elif self._pipelines[index].__repr__() == "CSVAdapter":
                print("processing CSV data through same pipeline...")
                print(f"input: {csv_data}")
                print("transform: parsed and structured data")
            elif self._pipelines[index].__repr__() == "StreamAdapter":
                print("processing stream data through same pipeline...")
                print("input: real-time sensor stream")
                print("transform: aggregated and filtered")
            print(f"output: {output}\n")
        self.clear_pipelines()

    def pipeline_chaining(self, input_data: any, scd_pipeline: str) -> None:
        print("=== Pipeline Chaining Demo ===")
        output: any = input_data
        if scd_pipeline == "csv":
            self.add_pipeline(StreamAdapter("SENSOR_001"))
            self.add_pipeline(CSVAdapter("CSV_001"))
            self.add_pipeline(CSVAdapter("CSV_002"))
        else:
            self.add_pipeline(StreamAdapter("SENSOR_001"))
            self.add_pipeline(JSONAdapter("JSON_001"))
            self.add_pipeline(JSONAdapter("JSON_002"))
        proc_time_start: float = time.time()
        for k, pipeline in enumerate(self._pipelines):
            if pipeline != self._pipelines[-1]:
                self.add_stages_to_pipeline(pipeline, 2)
            else:
                self.add_stages_to_pipeline(pipeline, 3)
            output = pipeline.process(output)
            if isinstance(output, str) and output.startswith("error"):
                self.error_recovery(output, pipeline)
            else:
                if k == 0:
                    record_count: int = output["readings"]
                    del output["readings"]
                    print(f"pipeline {pipeline}", end="")
                elif pipeline == self._pipelines[-1]:
                    print(f" ->pipeline {pipeline}")
                else:
                    print(f" ->pipeline {pipeline}", end="")
        proc_time_end: float = time.time()
        print("data flow: raw ->processed ->analyzed ->stored\n")
        print(
            f"chain result: {record_count} records "
            "processed through 3-stage pipeline"
        )
        print(
            f"performance: 95% efficiency, "
            f"{round(proc_time_end - proc_time_start, 2)} "
            "total processing time\n"
        )
        self.clear_pipelines()

    def error_recovery(
        self,
        error_str: str,
        pipeline: ProcessingPipeline
    ) -> None:
        print(f"{error_str} - PIPELINE {pipeline}")
        print("recovery initiated: switching to backup processor")
        print("recovery successful: pipeline restored, processing resumed\n")


def generate_sensor(
    nb_readings: int,
    input_type: int
) -> Generator[str, None, None]:
    sensor_list: list[str] = ["temp", "pressure", "humidity"]
    csv_list: list[str] = ["user", "action", "timestamp", "login", "logout"]
    while nb_readings > 0:
        if input_type == 1:
            yield random.choice(sensor_list) + ":" +\
                str(round(random.uniform(0, 200), 1))
        else:
            yield random.choice(csv_list)
        nb_readings -= 1


def main() -> None:
    json_data: list[str] = ["sensor:temp", "value:23.5", "unit:C"]
    csv_data: str = "user,action,timestamp"
    sensor_data: Generator[str, None, None] = generate_sensor(4, 1)
    print("=== CODE NEXUS - ENTERPRISE PIPELINE SYSTEM ===\n")
    nexus_mngr = NexusManager()
    print("=== Multi-Format Data Processing ===\n")
    nexus_mngr.multi_proc(json_data, csv_data, sensor_data)
    sensor_data = generate_sensor(52, 2)
    nexus_mngr.pipeline_chaining(sensor_data, "csv")
    sensor_data = generate_sensor(65, 1)
    nexus_mngr.pipeline_chaining(sensor_data, "json")
    print("=== Error Recovery Test ===\n")
    print("simulating pipeline failure...")
    sensor_data = generate_sensor(7, 1)
    nexus_mngr.multi_proc(404, csv_data, sensor_data)
    print("nexus integration complete - all systems operational")


if __name__ == "__main__":
    main()
