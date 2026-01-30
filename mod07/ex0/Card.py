from abc import ABC, abstractmethod


class Card(ABC):
    """
    A class that represents a card.
    """
    def __init__(self, name: str, cost: int, rarity: str) -> None:
        """
        Initializes the card's data.

        Parameters
        ----------
        name
            The card's name.
        cost
            The card's cost to play.
        rarity
            The card's rarity.
        """
        self.name: str = name
        self.cost: int = cost
        self.rarity: str = rarity

    @abstractmethod
    def play(self, game_state: dict) -> dict:
        """
        Plays the card.

        Parameters
        ----------
        game_state
            The game's state.

        Returns
        -------
        dict
            The playing result.
        """
        pass

    def get_card_info(self) -> dict:
        """
        Gets the card's info (its properties).

        Returns
        -------
        dict
            The card's info.
        """
        return {
            "name": self.name,
            "cost": self.cost,
            "rarity": self.rarity
        }

    def is_playable(self, available_mana: int) -> bool:
        """
        Verifies whether or not the card is playable
        based on the available mana given and the card's cost.

        Parameters
        ----------
        available_mana
            The mana available.

        Returns
        -------
        bool
            True if the card is playable, False otherwise.
        """
        if self.cost > available_mana:
            return False
        else:
            return True
