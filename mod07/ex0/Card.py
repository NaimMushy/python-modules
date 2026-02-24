from abc import ABC, abstractmethod


class Card(ABC):

    def __init__(
        self,
        name: str,
        cost: int,
        rarity: str,
        card_type: str = "cards"
    ) -> None:

        self.name: str = name
        self.cost: int = cost
        self.rarity: str = rarity
        self.card_type: str = card_type

    @abstractmethod
    def play(self, game_state: dict) -> dict:
        pass

    def get_card_info(self) -> dict:

        return {
            "name": self.name,
            "cost": self.cost,
            "rarity": self.rarity
        }

    def is_playable(self, available_mana: int) -> bool:

        if self.cost > available_mana:
            return False

        else:
            return True
