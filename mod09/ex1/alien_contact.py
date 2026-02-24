from pydantic import Field, BaseModel, ValidationError, model_validator
from enum import Enum
from datetime import datetime
from typing import Optional as optional
from typing import Self as self


class ContactType(Enum):
    RADIO = 1
    VISUAL = 2
    PHYSICAL = 3
    TELEPATHIC = 4


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
            raise ValueError("Contact ID must start with 'AC'!")
        return self

    @model_validator(mode="after")
    def validate_physical_contact(self) -> self:
        if self.contact_type == ContactType.PHYSICAL and not self.is_verified:
            raise ValueError("Physical contact report must be verified!")
        return self

    @model_validator(mode="after")
    def validate_telepathic_contact(self) -> self:
        if self.contact_type == ContactType.TELEPATHIC and self.witness_count < 3:
            raise ValueError("Telepathic contact requires at least 3 witnesses!")
        return self

    @model_validator(mode="after")
    def validate_signal(self) -> self:
        if self.signal_strength > 7.0 and not self.message_received:
            raise ValueError("No message received despite strong signal!")
        return self

    def display_report_info(self) -> None:
        print(f"ID: {self.contact_id}")
        print(f"Type: {self.contact_type.name.lower()}")
        print(f"Location: {self.location}")
        print(f"SIgnal: {self.signal_strength}/10")
        print(f"Duration: {self.duration_minutes} minutes")
        print(f"Witnesses: {self.witness_count}")
        print(f"Message: {self.message_received}")
        if self.is_verified:
            print("VERIFIED")


def main() -> None:

    print("Alien Contact Log Validation")

    report_info: dict = {
        "id": "AC_2024_001",
        "timestamp": datetime.now(),
        "location": "Area 51, Nevada",
        "signal": 8.5,
        "duration": 25,
        "witnesses": 5,
        "msg": "Greetings from Zeta Reticuli",
        "verified": True
    }

    for _ in range(2):
        print("====================================")
        try:
            contact_report: AlienContact = AlienContact(
               contact_id=report_info["id"],
               timestamp=report_info["timestamp"],
               location=report_info["location"],
               contact_type=ContactType.PHYSICAL,
               signal_strength=report_info["signal"],
               duration_minutes=report_info["duration"],
               witness_count=report_info["witnesses"],
               message_received=report_info["msg"],
               is_verified=report_info["verified"]
            )
        except ValidationError as ve:
            print(f"Expected validation error:\n{ve}")
        else:
            print("Valid contact report:")
            contact_report.display_report_info()
        report_info["verified"] = False


if __name__ == "__main__":
    main()
