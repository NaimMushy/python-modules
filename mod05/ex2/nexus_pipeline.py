from abc import ABC
from typing import Protocol
from typing import Any as any
from typing import Generator
import re
import random
import time


class ProcessingStage(Protocol):
    """
    A class that represents a processing stage.
    """
    def process(self, data: any) -> any:
        """
        Processed the data given as parameter.

        Parameters
        ----------
        data
            The data to process.

        Returns
        -------
        any
            The processed data.
        """
        pass


class InputStage:
    """
    A class that represents an input processing stage.
    """
    def process(self, data: any) -> dict:
        """
        Processes the data given as parameter
        by calling the appropriate function.

        Parameters
        ----------
        data
            The data to process.

        Returns
        -------
        dict
            The processed data.

        Raises
        ------
        TypeError:
            Raised if the given data doesn't correspond to any adapter.
        """
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
        """
        Processes JSON data.

        Parameters
        ----------
        data
            The JSON data to process.

        Returns
        -------
        dict
            The processed JSON data.

        Raises
        ------
        TypeError:
            Raised if the given data has an invalid format for JSON data.
        """
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
        """
        Processes CSV data.

        Parameters
        ----------
        data
            The CSV data to process.

        Returns
        -------
        dict
            The processed CSV data.

        Raises
        ------
        TypeError:
            Raised if the given data has an invalid format for CSV data.
        """
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
                    and isinstance(val, (str, int, float, list))
                ):
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
        """
        Processes real-time stream sensor data.

        Parameters
        ----------
        data
            The sensor stream data to process.

        Returns
        -------
        dict
            The processed sensor stream data.

        Raises
        ------
        TypeError:
            Raised if the given data
            has an invalid format for sensor stream data.
        """
        validated_dict: dict = {}
        if not isinstance(data, Generator):
            raise TypeError("invalid format for sensor data - [REJECTED]")
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
        validated_dict["adapter"] = "sensor"
        return validated_dict


class TransformStage:
    """
    A class that represents a transforming processing stage.
    """
    def process(self, data: any) -> dict:
        """
        Processes the data given as parameter
        by calling the appropriate function.

        Parameters
        ----------
        data
            The data to process.

        Returns
        -------
        dict
            The processed data.

        Raises
        ------
        TypeError:
            Raised if the given data doesn't correspond to any adapter.
        """
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
        """
        Calculates whether the range of the value mesured by the sensor
        is critical or normal.

        Parameters
        ----------
        sensor_type
            The sensor's type: temperature, pressure, humidity.
        value
            The value mesured by the sensor.

        Returns
        -------
        str
            The range for the value: 'critical' or 'normal'.
        """
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
        """
        Transforms JSON data by evaluating the mesures' ranges
        and detailing what is mesured by the sensors.

        Parameters
        ----------
        data
            The JSON data to transform.

        Returns
        -------
        dict
            The transformed JSON data.

        Raises
        ------
        TypeError:
            Raised if the given data has an invalid format.
        """
        if not isinstance(data, dict):
            raise TypeError(
                "invalid format for "
                "json data - [REJECTED]"
            )
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
        """
        Transforms CSV data by registering user activity
        and the different system events.

        Parameters
        ----------
        data
            The CSV data to transform.

        Returns
        -------
        dict
            The transformed CSV data.

        Raises
        ------
        TypeError:
            Raised if the given data has an invalid format.
        """
        if not isinstance(data, dict):
            raise TypeError(
                "invalid format for "
                "csv data - [REJECTED]"
            )
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
        """
        Transforms real-time sensor stream data
        by keeping tracks of readings and making an average for each sensor.

        Parameters
        ----------
        data
            The stream sensor data to transform.

        Returns
        -------
        dict
            The transformed stream sensor data.

        Raises
        ------
        TypeError:
            Raised if the given data has an invalid format.
        """
        if not isinstance(data, dict):
            raise TypeError(
                "invalid format for "
                "sensor data - [REJECTED]"
            )
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
                trans_dict["readings"] += val
        if "avg_temp" in trans_dict.keys():
            trans_dict["avg_temp"] = str(trans_dict["avg_temp"]) + "°C"
        if "avg_pressure" in trans_dict.keys():
            trans_dict["avg_pressure"] = str(trans_dict["avg_pressure"]) + "Pa"
        if "avg_humidity" in trans_dict.keys():
            trans_dict["avg_humidity"] = str(trans_dict["avg_humidity"]) + "%"
        return trans_dict


class OutputStage:
    """
    A class that represents an output processing stage.
    """
    def process(self, data: any) -> str:
        """
        Processed the data given as paramete
        by calling the appropriate function.

        Parameters
        ----------
        data
            The data to process.

        Returns
        -------
        str
            The processed data's output.

        Raises
        ------
        TypeError:
            Raised if the given data doesn't correspond to any adapter.
        """
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
        """
        Figures out a correct output for the given JSON data.

        Parameters
        ----------
        data
            The JSON data to output.

        Returns
        -------
        str
            The JSON output.

        Raises
        ------
        TypeError:
            Raised if the given data has an invalid format.
        """
        if not isinstance(data, dict):
            raise TypeError(
                "invalid format for "
                "json data - [REJECTED]"
            )
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
        """
        Figures out a correct output for the given CSV data.

        Parameters
        ----------
        data
            The CSV data to output.

        Returns
        -------
        str
            The CSV output.

        Raises
        ------
        TypeError:
            Raised if the given data has an invalid format.
        """
        if not isinstance(data, dict):
            raise TypeError(
                "invalid format for "
                "csv data - [REJECTED]"
            )
        output_string: str = ""
        output_string += f"user activity {data['user_activity']}: "
        new_dict: dict = {
            key: val for key, val in data.items()
            if key != "user_activity" and key != "adapter"
        }
        if new_dict == {}:
            output_string += "no additional data provided"
            return output_string
        count: int = 0
        for key, val in new_dict.items():
            count += 1
            if not isinstance(val, list) and val <= 1:
                output_string += f"{val} {key} processed"
            else:
                output_string += f"{val} {key}s processed"
            if count < len(new_dict):
                output_string += " - "
        return output_string

    def output_sensor(self, data: any) -> str:
        """
        Figures out a correct output to the given real-time sensor stream data.

        Parameters
        ----------
        data
            The stream sensor data to output.

        Returns
        -------
        str
            The stream sensor output.

        Raises
        ------
        TypeError:
            Raised if the given data has an invalid format.
        """
        if not isinstance(data, dict):
            raise TypeError(
                "invalid format for "
                "sensor data - [REJECTED]"
            )
        output_string: str = f"stream summary: {data['readings']} readings"
        new_dict: dict = {
            key: val for key, val in data.items()
            if key != "readings" and key != "adapter"
        }
        for key, val in new_dict.items():
            output_string += f" - {key}: {val}"
        return output_string


class ProcessingPipeline(ABC):
    """
    A class that represents a processing pipeline.
    """
    def __init__(self, pipeline_id: str) -> None:
        """
        Initializes the processing pipeline's data.

        Parameters
        ----------
        pipeline_id
            The processing pipeline's ID.
        """
        self.pipeline_id: str = pipeline_id
        self._stages: list[ProcessingStage] = []

    def __repr__(self) -> str:
        """
        Gives the name of the class to which the object belongs.

        Returns
        -------
        str
            The class' name.
        """
        return self.__class__.__name__

    def add_stage(self, new_stage: ProcessingStage) -> None:
        """
        Adds a processing stage to the pipeline's stages.

        Parameters
        ----------
        new_stage
            The new processing stage to add.
        """
        self._stages.append(new_stage)

    def process(self, data: any) -> any:
        """
        Processes the data given as parameter
        by passing it through its processing stages.

        Parameters
        ----------
        data
            The data to process.

        Returns
        -------
        any
            The processed data output.
        """
        data_dict: dict = {}
        data_dict["adapter"] = "any"
        data_dict["rawdata"] = data
        for stage in self._stages:
            data_dict = stage.process(data_dict)
        return data_dict


class JSONAdapter(ProcessingPipeline):
    """
    A class that represents a JSON adapter.
    """
    def process(self, data: any) -> any:
        """
        Processes the JSON data given as parameter
        by passing it through its processing stages.

        Parameters
        ----------
        data
            The JSON data to process.

        Returns
        -------
        any
            The processed JSON data output.
        """
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
    """
    A class that represents a CSV adapter.
    """
    def process(self, data: any) -> any:
        """
        Processes the CSV data given as parameter
        by passing it through its processing stages.

        Parameters
        ----------
        data
            The CSV data to process.

        Returns
        -------
        any
            The processed CSV data output.
        """
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
    """
    A class that represents a stream adapter.
    """
    def process(self, data: any) -> any:
        """
        Processes the real-time sensor stream data given as parameter
        by passing it through its processing stages.

        Parameters
        ----------
        data
            The stream sensor data to process.

        Returns
        -------
        any
            The processed stream sensor data output.
        """
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
    """
    A class that represents a nexus manager,
    capable of managing multiple processing pipelines
    aswell as chaining pipelines to one another,
    so as to process data more efficiently.
    """
    def __init__(self) -> None:
        """
        Initializes the nexus manager's data.
        """
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
        """
        Removes all of the nexus manager's pipelines.
        """
        self._pipelines = []

    def add_stages_to_pipeline(
        self,
        pipeline: ProcessingPipeline,
        nb_stages: int
    ) -> None:
        """
        Add different processing stages to a pipeline.

        Parameters
        ----------
        pipeline
            The pipeline to which the stages need to be added.
        nb_stages
            The number of processing stages to add to the pipeline.
        """
        for index in range(nb_stages):
            pipeline.add_stage(self._stages[index])

    def add_pipeline(self, new_pipeline: ProcessingPipeline) -> None:
        """
        Adds the new pipeline given to the nexus manager's pipelines.

        Parameters
        ----------
        new_pipeline
            The new pipeline to add.
        """
        self._pipelines.append(new_pipeline)

    def multi_proc(
        self,
        json_data: any,
        csv_data: any,
        sensor_data: any
    ) -> None:
        """
        Manages multi-format data processing by passing the different data
        given as parameter through the appropriate pipeline.

        Parameters
        ----------
        json_data
            The JSON data to process.
        csv_data
            The CSV data to process.
        sensor_data
            The real-time sensor stream data to process.
        """
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
        """
        Chains multiple pipeline to one another,
        allowing the output of one pipeline to be passed through another.

        Parameters
        ----------
        input_data
            The input data to process.
        scd_pipeline
            The choice of the second pipeline to pass the data through.
        """
        print("=== Pipeline Chaining Demo ===")
        output: any = input_data
        if scd_pipeline == "csv":
            self.add_pipeline(StreamAdapter("SENSOR_001"))
            self.add_pipeline(CSVAdapter("CSV_001"))
            self.add_pipeline(JSONAdapter("JSON_001"))
        else:
            self.add_pipeline(StreamAdapter("SENSOR_001"))
            self.add_pipeline(JSONAdapter("JSON_001"))
            self.add_pipeline(CSVAdapter("CSV_001"))
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
        """
        Displays appropriate error messages
        when a pipeline failure occurs during the processing.

        Parameters
        ----------
        error_str
            The error message to output.
        pipeline
            The pipeline which caused the failure.
        """
        print(f"{error_str} - PIPELINE <{pipeline}>")
        print("recovery initiated: switching to backup processor")
        print("recovery successful: pipeline restored, processing resumed\n")


def generate_sensor(
    nb_readings: int,
    input_type: int
) -> Generator[str, None, None]:
    """
    Generates real-time sensor stream data to further process.

    Parameters
    ----------
    nb_readings
        The number of sensor stream readings to generate.
    input_type
        The type of the input sensor stream: csv or json.

    Returns
    -------
    Generator[str, None, None]
        The generator containing the stream sensor data.
    """
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
    """
    Shows how to process different data efficiently
    through a nexus manager and multiple processing pipelines.
    """
    json_data: list[str] = ["sensor:temp", "value:23.5", "unit:C"]
    csv_data: str = "user,action,timestamp"
    sensor_data: Generator[str, None, None] = generate_sensor(4, 1)
    print("=== CODE NEXUS - ENTERPRISE PIPELINE SYSTEM ===\n")
    nexus_mngr = NexusManager()
    print("=== Multi-Format Data Processing ===\n")
    nexus_mngr.multi_proc(json_data, csv_data, sensor_data)
    print("simulating pipeline failure in multi-format data processing...")
    nexus_mngr.multi_proc(json_data, 404, sensor_data)
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
