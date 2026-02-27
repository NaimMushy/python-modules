from pydantic import Field, BaseModel, ValidationError, model_validator
from enum import Enum
from datetime import datetime
from typing import Optional as optional
from typing_extensions import Self as self


class ContactType(Enum):

    RADIO = "radio"
    VISUAL = "visual"
    PHYSICAL = "physical"
    TELEPATHIC = "telepathic"


class AlienContact(BaseModel):

    contact_id: str = Field(min_length=5, max_length=15)
    timestamp: datetime
    location: str = Field(min_length=3, max_length=100)
    contact_type: ContactType
    signal_strength: float = Field(ge=0.0, le=10.0)
    duration_minutes: int = Field(ge=1, le=1440)
    witness_count: int = Field(ge=1, le=100)
    message_received: optional[str] = Field(default=None, max_length=500)
    is_verified: bool = Field(default=False)

    @model_validator(mode="after")
    def validate_id(self) -> self:

        if not self.contact_id.startswith("AC"):

            raise ValueError(
                "Contact ID must start with 'AC' (Alien Contact)!"
            )

        return self

    @model_validator(mode="after")
    def validate_physical_contact(self) -> self:

        if self.contact_type == ContactType.PHYSICAL and not self.is_verified:

            raise ValueError("Physical contact report must be verified!")

        return self

    @model_validator(mode="after")
    def validate_telepathic_contact(self) -> self:

        if (
            self.contact_type == ContactType.TELEPATHIC
        ) and (
            self.witness_count < 3
        ):

            raise ValueError(
                "Telepathic contact requires at least 3 witnesses!"
            )

        return self

    @model_validator(mode="after")
    def validate_signal(self) -> self:

        if self.signal_strength > 7.0 and not self.message_received:

            raise ValueError(
                "Strong signals (> 7.0) should include received messages!"
            )

        return self

    def __str__(self) -> str:

        return (
            f"ID: {self.contact_id}\n"
            f"Type: {self.contact_type.name.lower()}\n"
            f"Location: {self.location}\n"
            f"Signal: {self.signal_strength}/10\n"
            f"Duration: {self.duration_minutes} minutes\n"
            f"Witnesses: {self.witness_count}\n"
            f"Message: {self.message_received}\n"
            f"{'[CONTACT VERIFIED]' if self.is_verified else ''}\n"
        )


def main() -> None:

    print("\nAlien Contact Log Validation\n")

    report_info: dict = {
        "contact_id": "AC_2024_001",
        "timestamp": datetime.now(),
        "location": "Area 51, Nevada",
        "contact_type": ContactType.PHYSICAL,
        "signal_strength": 8.5,
        "duration_minutes": 25,
        "witness_count": 5,
        "message_received": "Greetings from Zeta Reticuli",
        "is_verified": True
    }

    for _ in range(2):

        print("====================================\n")

        try:

            contact_report: AlienContact = AlienContact(**report_info)

        except ValidationError as ve:

            print("Expected validation error:\n")
            for err in ve.errors():
                print(err["msg"])

        else:

            print(f"Valid contact report:\n\n{contact_report}")

        report_info["is_verified"] = False

    print("")


if __name__ == "__main__":

    main()
