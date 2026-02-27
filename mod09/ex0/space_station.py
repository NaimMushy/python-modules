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

    def display_station_info(self) -> None:

        print(f"ID: {self.station_id}")
        print(f"Name: {self.name}")
        print(f"Crew: {self.crew_size} people")
        print(f"Power: {self.power_level}%")
        print(f"Oxygen: {self.oxygen_level}%")
        print(
            "Status: "
            f"{'Operational' if self.is_operational else 'Not operational'}"
        )

        if self.notes:
            print(f"Notes: {self.notes}")

        print("")


def main() -> None:

    print("\nSpace Station Data Validation\n")

    station_info: dict = {
        "id": "I88001",
        "name": "International Space Station",
        "crew_size": 6,
        "power_lvl": 85.5,
        "oxygen_lvl": 92.3,
        "lst_maintenance": datetime.now(),
        "operational": True
    }

    for _ in range(2):

        print("=======================================\n")

        try:

            space_station: SpaceStation = SpaceStation(
                station_id=station_info["id"],
                name=station_info["name"],
                crew_size=station_info["crew_size"],
                power_level=station_info["power_lvl"],
                oxygen_level=station_info["oxygen_lvl"],
                last_maintenance=station_info["lst_maintenance"],
                is_operational=station_info["operational"]
            )

        except ValidationError as ve:

            print(f"Expected validation error:\n\n{ve.errors()[0]['msg']}")

        else:

            print("Valid station created:\n")
            space_station.display_station_info()

        station_info["crew_size"] = 30

    print("")


if __name__ == "__main__":

    main()
