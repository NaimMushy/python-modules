from abc import ABC, abstractmethod
from typing import Any as any
from ex0.Card import Card


class CardFactory(ABC):

    @abstractmethod
    def create_creature(self, name_or_power: str | int | None = None) -> Card:
        pass

    @abstractmethod
    def create_spell(self, name_or_power: str | int | None = None) -> Card:
        pass

    @abstractmethod
    def create_artifact(self, name_or_power: str | int | None = None) -> Card:
        pass

    @abstractmethod
    def create_themed_deck(self, size: int) -> dict:
        pass

    @abstractmethod
    def get_supported_types(self) -> dict:
        pass

    def get_factory_type(self) -> str:
        return self.__class__.__name__.replace("CardFactory", "")

    def display_supported_types(self) -> None:

        supported_types: dict[str, dict[str, any]] = self.get_supported_types()

        print("\n\n=== AVAILABLE TYPES ===\n")

        for card_type, card_values in supported_types.items():

            print(f"\n{card_type.capitalize()}:\n")

            print("\n-> NAMES:\n")

            for name in card_values["card_names"]:
                print(f"< {name} >")

            print("\n\n-> POWERS:\n")

            power_integers: list[int] = [
                power for power in card_values["card_powers"]
                if isinstance(power, int)
            ]

            print(f"< from {min(power_integers)} to {max(power_integers)} >")

            power_strings: list[str] = [
                power for power in card_values["card_powers"]
                if isinstance(power, str)
            ]

            if power_strings:

                print("< ", end="")

                for power in power_strings:

                    if power != power_strings[0]:
                        print(", ", end="")

                    print(f"{power}", end="")

                print(" >")

            print("\n")
