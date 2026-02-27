from enum import Enum
from datetime import datetime
from typing_extensions import Self as self
from pydantic import BaseModel, Field, ValidationError, model_validator


class Rank(Enum):

    CADET = 1
    OFFICER = 2
    LIEUTENANT = 3
    CAPTAIN = 4
    COMMANDER = 5


class CrewMember(BaseModel):

    member_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=2, max_length=50)
    rank: Rank
    age: int = Field(ge=18, le=80)
    specialization: str = Field(min_length=3, max_length=30)
    years_experience: int = Field(ge=0, le=50)
    is_active: bool = Field(default=True)

    def get_member_info(self) -> str:

        return (
            f"{self.name} ({self.rank.name.lower()}) "
            f"- {self.specialization}"
        )


class SpaceMission(BaseModel):

    mission_id: str = Field(min_length=5, max_length=15)
    mission_name: str = Field(min_length=3, max_length=100)
    destination: str = Field(min_length=3, max_length=50)
    launch_date: datetime
    duration_days: int = Field(ge=1, le=3650)
    crew: list[CrewMember] = Field(min_length=1, max_length=12)
    mission_status: str = Field(default="planned")
    budget_millions: float = Field(ge=1.0, le=10000.0)

    @model_validator(mode="after")
    def validate_mission(self) -> self:

        if not self.mission_id.startswith("M"):

            raise ValueError("Mission ID must start with an 'M'!")

        if not (
            any(member.rank in [
                Rank.COMMANDER, Rank.CAPTAIN
            ] for member in self.crew)
        ):

            raise ValueError(
                "Mission must have at least one Commander or Captain!"
            )

        if self.duration_days > 365 and sum(
            1 for member in self.crew if member.years_experience < 5
        ) > len(self.crew) / 2:

            raise ValueError(
                "Long missions must have a more experienced crew! "
                "(50% with 5+ years of experience)"
            )

        if not all(member.is_active for member in self.crew):

            raise ValueError("All members must be active!")

        return self

    def display_mission_info(self) -> None:

        print(f"ID: {self.mission_id}")
        print(f"Mission: {self.mission_name}")
        print(f"Destination: {self.destination}")
        print(f"Launch Date: {self.launch_date}")
        print(f"Duration: {self.duration_days} days")
        print(f"Budget: {self.budget_millions}M")
        print(f"Crew size: {len(self.crew)}")
        print("Crew members:")

        for member in self.crew:
            print(f"- {member.get_member_info()}")

        print("\n")


def main() -> None:

    print("\nSpace Mission Crew Validation\n")

    luke: CrewMember = CrewMember(
        member_id="SC_1",
        name="Luke Skywalker",
        rank=Rank.COMMANDER,
        age=26,
        specialization="Mission Command",
        years_experience=6,
    )

    han: CrewMember = CrewMember(
        member_id="JS_1",
        name="Han Solo",
        rank=Rank.LIEUTENANT,
        age=50,
        specialization="Navigation",
        years_experience=3,
    )

    r2d2: CrewMember = CrewMember(
        member_id="AJ_1",
        name="R2D2",
        rank=Rank.OFFICER,
        age=78,
        specialization="Engineering",
        years_experience=1,
    )

    mission_info: dict = {
        "id": "M2024_UNKNOWN",
        "name": "Unknown Regions Exploration",
        "destination": "Illum, Starkiller Base",
        "launch_date": datetime.now(),
        "duration": 300,
        "budget": 2500.5,
        "crew": [luke, han, r2d2]
    }

    for _ in range(2):

        print("======================================\n")

        try:

            mission: SpaceMission = SpaceMission(
                mission_id=mission_info["id"],
                mission_name=mission_info["name"],
                destination=mission_info["destination"],
                launch_date=mission_info["launch_date"],
                duration_days=mission_info["duration"],
                crew=mission_info["crew"],
                budget_millions=mission_info["budget"]
            )

        except ValidationError as ve:

            print(f"Expected validation error:\n\n{ve.errors()[0]['msg']}")

        else:

            print("Valid mission created:\n")
            mission.display_mission_info()

        luke.rank = Rank.CADET

    print("")


if __name__ == "__main__":

    main()
