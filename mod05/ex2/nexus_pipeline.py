from abc import ABC, abstractmethod
from typing import Protocol
from typing import Any as any


class ProcessingPipeline(ABC):
    def __init__(self, pipeline_id: str) -> None:
        self.pipeline_id: str = pipeline_id
        self._stages: list[ProcessingStage] = []

    def add_stage(self, new_stage: ProcessingStage) -> None:
        self._stages.append(new_stage)

    def process(self, data: any) -> any:
        pass


class JSONAdapter(ProcessingPipeline):
    def process(self, data: any) -> any:
        

class CSVAdapter(ProcessingPipeline):
    def process(self, data: any) -> any:


class StreamAdapter(ProcessingPipeline):
    def process(self, data: any) -> any:


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
        if isinstance(data, list):
            for d in data:
                if (match := re.match("([a-z]+):([a-z0-9.]+)", d, re.I)):
                    validated_dict[match.group(1)] = match.group(2)
                else:
                    raise TypeError("invalid format for json data - [REJECTED]")
        elif isinstance(data, dict):
            for key, val in data.items():
                if isinstance(key, str) and isinstance(val, [str, int, float]):
                    if key in validated_dict.keys():
                        validated_dict[key].append(val)
                    else:
                        validated_dict[key] = [val]
                else:
                    raise TypeError("invalid format for json data - [REJECTED]")
        else:
            raise TypeError("invalid format for json data - [REJECTED]")
        validated_dict["adapter"] = "json"
        return validated_dict

    def input_csv(self, data: any) -> dict:
        validated_dict: dict = {}
        if isinstance(data, str):
            data["rawdata"] = data["rawdata"].split(",")
            for d in data:
                if (match := re.match("[a-z]+", d, re.I)):
                    if match.group(1) in validated_dict.keys():
                        validated_dict[match.group(1)] += 1
                    else:
                        validated_dict[match.group(2)] = 1
                else:
                    raise TypeError("invalid format for csv data - [REJECTED]")
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
                else:
                    raise TypeError("invalid format for sensor data - [REJECTED]")
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

    def transform_json(self, data: any) -> dict:
        for key, val in data.items():
            if val == "temp":

class OutputStage:
    def process(self, data: any) -> str:
