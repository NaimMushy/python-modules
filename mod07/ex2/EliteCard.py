from .Combatable import Combatable
from .Magical import Magical
from ex0.Card import Card


class EliteCard(Card, Combatable, Magical):
    def __init__(
        self,
        name: str,
        cost: int,
        rarity: str,
        attack: int,
        combat_type: str
    ) -> None:
        super().__init__(name, cost, rarity)
        self.attack: int = attack
        self.combat_type: str = combat_type

    def attack(self, target) -> dict:
        attack_result: dict = {
            "attacker": self.name,
            "target": target.name
            "damage": self.
                }
