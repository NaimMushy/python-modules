from abc import ABC
from typing import Protocol
from typing import Any as any
import random


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
                    if match.group(1) in validated_dict.keys():
                        validated_dict[match.group(1)].append(match.group(2))
                    else:
                        validated_dict[match.group(2)] = [match.group(2)]
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

    def get_range(self, sensor_type: str, value: int | float) -> str:
        if sensor_type == "temp":
            if value > 40 or value < -10:
                return "critical"
            else:
                return "normal"
        elif sensor_type == "pressure":
            if value > 2000 or value < 0:
                return "critical"
            else:
                return "normal"
        elif sensor_type == "humidity":
            if value > 80 or value < 10:
                return "critical"
            else:
                return "normal"
        else:
            if value > 100 or value < 0:
                return "critical"
            else:
                return "normal"

    def transform_json(self, data: any) -> dict:
        trans_dict: dict = {}
        trans_dict["adapter"] = "json"
        for key, val in data.items():
            if val == "temp":
                trans_dict[key] = "temperature"
            elif key == "value":
                if "sensor" in data.keys():
                    trans_dict["range"] = self.get_range(data["sensor"], val)
                trans_dict[key] = val
            elif key == "unit":
                if val == "C" or val == "F":
                    trans_dict[key] = "°" + val
                else:
                    trans_dict[key] = val
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
            else:
                trans_dict[key + "s"] = val
        return trans_dict

    def transform_sensor(self, data: any) -> dict:
        trans_dict: dict = {}
        trans_dict["adapter"] = "sensor"
        trans_dict["readings"] = 0
        for key, val in data.items():
            for mesure in val:
                if self.get_range(mesure, key) == "critical":
                    if "critical" in trans_dict.keys():
                        trans_dict["critical"].append(key+":"+str(mesure))
                    else:
                        trans_dict["critical"] = [key+":"+str(mesure)]
                trans_dict["avg_"+key] += mesure
                trans_dict["readings"] += 1
            if len(val) > 1:
                trans_dict["avg_"+key] /= len(val)
            if key == "temp":
                trans_dict["avg_"+key] = str(trans_dict["avg_"+key]) + "°C"
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
        return output_string

    def output_csv(self, data: any) -> str:
        output_string: str = ""
        output_string += f"user activity {data['user_activity']}: "
        new_dict: dict = {key: val for key, val in data.items() if key != "user_activity"}
        if new_dict == {}:
            output_string += "no additional data provided"
            return output_string
        for key, val in new_dict.items():
            output_string += f"{val} {key} processed - "
        return output_string

    def output_sensor(self, data: any) -> str:
        output_string: str = f"stream summary: {data['readings']} readings"
        new_dict: dict = {key: val for key, val in data.items() if key != "readings"}
        for key, val in new_dict.items():
            output_string += f" - {key}: {val}"
        return output_string


class ProcessingPipeline(ABC):
    def __init__(self, pipeline_id: str) -> None:
        self.pipeline_id: str = pipeline_id
        self._stages: list[ProcessingStage] = []

    def add_stage(self, new_stage: ProcessingStage) -> None:
        self._stages.append(new_stage)

    def process(self, data: any) -> any:
        data_dict: dict = {}
        data_dict["adapter"] = "any"
        data_dict["rawdata"] = data
        results: list = []
        for stage in self._stages:
            data_dict = stage.process(data_dict)
            if isinstance(stage, TransformStage):
                results.append("parsed and structured data")
            else:
                results.append(data_dict)
        return results


class JSONAdapter(ProcessingPipeline):
    def process(self, data: any) -> any:
        data_dict: dict | str = {}
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
        data_dict: dict | str = {}
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
        data_dict: dict | str = {}
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


class NexusManager:
    def __init__(self) -> None:
        print("initializing Nexus Manager...")
        print("pipeline capacity: 1000 streams/second\n")
        self._pipelines: list = []
        self.create_data_pipeline()

    def create_data_pipeline(self) -> None:
        print("creating data processing pipeline...")
        self._json_pipeline = JSONAdapter("JSON_001")
        self._pipelines.append(self._json_pipeline)
        self._csv_pipeline = CSVAdapter("CSV_001")
        self._pipelines.append(self._csv_pipeline)
        self._sensor_pipeline = StreamAdapter("SENSOR_001")
        self._pipelines.append(self._sensor_pipeline)
        for pipeline in self._pipelines:
            pipeline.add_stage(InputStage)
            pipeline.add_stage(TransformStage)
            pipeline.add_stage(OutputStage)
        print("stage 1: input validation and parsing")
        print("stage 2: data transformation and enrichment")
        print("stage 3: output formatting and delivery\n")

    def multi_proc(self, json_data: any, csv_data: any, sensor_data: any) -> None:
        print("=== Multi-Format Data Processing ===\n")
        json_output: str = self._json_pipeline.process(json_data)
        if json_output[:4] == "error":
            self.error_recovery(json_output)
        else:
            print("processing JSON data through pipeline...")
            print(f"input: {json_data}")
            print("transform: enriched with metadata and validation")
            print(f"output: {self._json_pipeline.process(json_data)}\n")
        csv_output: str = self._csv_pipeline.process(csv_data)
        if csv_output[:4] == "error":
            self.error_recovery(csv_output)
        else:
            print("processing CSV data through same pipeline...")
            print(f"input: {csv_data}")
            print("transform: parsed and structured data")
            print(f"output: {self._csv_pipeline.process(csv_data)}\n")
        sensor_output: str = self._sensor_pipeline.process(sensor_data)
        if sensor_output[:4] == "error":
            self.error_recovery(sensor_output)
        else:
            print("processing stream data through same pipeline...")
            print("input: real-time sensor stream")
            print("transform: aggregated and filtered")
            print(f"output: {self._sensor_pipeline.process(sensor_data)}\n")

    def pipeline_chaining(self, )

    def error_recovery(self, error_str: str) -> None:
        print(error_str)
        print("recovery initiated: switching to bqckup processor")
        print("recovery successful: pipeline restored, processing resumed\n")
        

    def process(
        self,
        data: any,
        adapter: str,
        silent_mode: bool = True
    ) -> None:
        if adapter == "json":
            processed_data: any = self._json_pipeline.process(data)
        elif adapter == "csv":
            processed_data = self._csv_pipeline.process(data)
        elif adapter == "sensor":
            processed_data = self._sensor_pipeline.process(data)
        if processed_data == "error recovery needed":
            print("recovery initiated: switching to backup processor")
            print("recovery successful: pipeline restored, processing resumed")
        elif not silent_mode:
            print(f"input: {processed_data[0]}")
            print(f"transform: {processed_data[1]}")
            print(f"output: {processed_data[2]}\n")


def generate_sensor(nb_readings: int) -> Generator[str, None, None]:
    sensor_list: list[str] = ["temp", "pressure", "humidity"]
    while nb_readings > 0:
        yield random.choice(sensor_list) + ":"
        + str(round(random.uniform(0, 200), 1))
        nb_readings -= 1


def main() -> None:
    json_data: list[str] = ["sensor:temp", "value:23.5", "unit:C"]
    csv_data: str = "user,action,timestamp"
    sensor_data: Generator[str, None, None] = generate_sensor(4)
    print("=== CODE NEXUS - ENTERPRISE PIPELINE SYSTEM ===\n")
    nexus_mngr = NexusManager()
    nexus_mngs.multi_proc(json_data, csv_data, sensor_data)
    print("=== Error Recovery Test ===\n")
    print("simulating pipeline failure...")
    sensor_data = generate_sensor(7)
    nexus_mngs.multi_proc(404, csv_data, sensor_data)
    print("nexus integration complete - all systems operational")


if __name__ == "__main__":
    main()
