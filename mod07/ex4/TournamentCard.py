from .Rankable import Rankable
from ex2.Combatable import Combatable
from ex0.Card import Card


class TournamentCard(Card, Combatable, Rankable):

    def __init__(
        self,
        name: str,
        attack: int,
        health: int,
        defense: int,
        combat_type: str,
        rating: int
    ) -> None:

        self.name = name
        self.attack_power: int = attack
        self.__health: int = health
        self.defense: int = defense
        self.combat_type: str = combat_type
        self.rating: int = rating
        self.wins: int = 0
        self.losses: int = 0

    def set_health(self, new_health: int) -> None:

        if new_health < self.get_health():
            self.defend(self.get_health() - new_health)

        else:
            self.__health: int = (
                new_health
                if isinstance(new_health, int) and new_health
                else 0
            )

    def get_health(self) -> int:

        return self.__health

    def update_wins(self, wins: int) -> None:

        self.wins += wins

    def update_losses(self, losses: int) -> None:

        self.losses += losses

    def attack(self, target) -> dict:

        target.set_health(
            target.get_health() - self.attack_power
        )

        return {
            "attacker": self.name,
            "target": target.name,
            "damage": self.attack_power,
            "combat_type": self.combat_type
        }

    def defend(self, incoming_damage: int) -> dict:

        if incoming_damage > self.defense:

            damage_taken: int = incoming_damage - self.defense

            self.__health -= (
                damage_taken
                if self.get_health() >= damage_taken
                else self.get_health()
            )

        else:
            damage_taken = 0

        defense_result: dict = {
            "defender": self.name,
            "damage_taken": damage_taken,
            "damage_blocked": self.defense,
            "still_alive": self.get_health() > 0
        }

        return defense_result

    def calculate_rating(self) -> int:

        new_rating: int = self.rating + (
            self.wins * 100
            - self.losses * 100
        )

        return new_rating if new_rating > 0 else 0

    def play(self, game_state: dict) -> dict:

        if not game_state["priority_target"]:
            return {}

        play_result: dict = {
            "card_played": self.name,
            "effect": f"Attacked {game_state['priority_target'].name}",
        }

        self.attack(game_state["priority_target"])

        return play_result

    def get_combat_stats(self) -> dict:

        return {
            "Combatable": ["attack", "defend", "get_combat_stats"]
        }

    def get_tournament_stats(self) -> dict:

        return {
            "interfaces": [base.__name__ for base in type(self).__bases__]
        } | self.get_rank_info()

    def get_card_info(self) -> dict:

        return Card.get_card_info(self) | {
            "attack": self.attack_power,
            "health": self.get_health(),
        } | self.get_tournament_stats()

    def get_rank_info(self) -> dict:

        return {
            "rating": self.calculate_rating(),
            "record": f"{self.wins}-{self.losses}"
        }
