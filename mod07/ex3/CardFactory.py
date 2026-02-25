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

        print(f"\n\n{' ' * 9}==== AVAILABLE TYPES ====\n")
        print(f"\n{' ' * 2}----------------------------------------")

        for card_type, card_values in supported_types.items():

            print(f"\n{' ' * 16}[{card_type.upper()}]\n")

            print(f"\n{' ' * 6}=> NAMES:\n")

            for name in card_values["card_names"]:
                print(f"{' ' * 10}< {name} >")

            print(f"\n\n{' ' * 6}=> POWERS:\n")

            power_integers: list[int] = [
                power for power in card_values["card_powers"]
                if isinstance(power, int)
            ]

            print(
                f"{' ' * 10}< from {min(power_integers)} "
                f"to {max(power_integers)} >"
            )

            power_strings: list[str] = [
                power for power in card_values["card_powers"]
                if isinstance(power, str)
            ]

            for power in power_strings:
                print(f"{' ' * 10}< {power} >")

            print(f"\n{' ' * 2}----------------------------------------")
