from pydantic import BaseModel, Field, ValidationError
from datetime import datetime
from typing import Optional as optional


class SpaceStation(BaseModel):

    station_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=1, max_length=50)
    crew_size: int = Field(ge=1, le=20)
    power_level: float = Field(ge=0.0, le=100.0)
    oxygen_level: float = Field(ge=0.0, le=100.0)
    last_maintenance: datetime
    is_operational: bool = Field(default=True)
    notes: optional[str] = Field(default=None, max_length=200)

    def __str__(self) -> str:

        return (
            f"ID: {self.station_id}\n"
            f"Name: {self.name}\n"
            f"Crew: {self.crew_size} people\n"
            f"Power: {self.power_level}%\n"
            f"Oxygen: {self.oxygen_level}%\n"
            "Status: "
            f"{'Operational' if self.is_operational else 'Not operational'}\n"
            f"{'Notes: ' + self.notes if self.notes else ''}"
        )


def main() -> None:

    print("\nSpace Station Data Validation\n")

    station_info: dict = {
        "station_id": "I88001",
        "name": "International Space Station",
        "crew_size": 6,
        "power_level": 85.5,
        "oxygen_level": 92.3,
        "last_maintenance": datetime.now(),
        "is_operational": True
    }

    for _ in range(2):

        print("=======================================\n")

        try:

            space_station: SpaceStation = SpaceStation(**station_info)

        except ValidationError as ve:

            print("Expected validation error:\n")
            for err in ve.errors():
                print(err["msg"])

        else:

            print(f"Valid station created:\n\n{space_station}")

        station_info["crew_size"] = 30

    print("")


if __name__ == "__main__":

    main()
