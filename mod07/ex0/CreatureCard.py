from .Card import Card


class CreatureCard(Card):
    def __init__(
        self,
        name: str,
        cost: int,
        rarity: str,
        attack: int,
        health: int
    ) -> None:
        super().__init__(name, cost, rarity)
        self.set_attack(attack)
        self.set_health(health)

    def set_attack(self, new_attack: int) -> None:
        if new_attack >= 0:
            self._attack = new_attack
        else:
            self._attack = 0
            print(f"Error: invalid attack {new_attack} - [REJECTED]")

    def set_health(self, new_health: int) -> None:
        if new_health > 0:
            self._health: int = new_health
        else:
            self._health = 1
            print(f"Error: invalid health {new_health} - [REJECTED]")

    def get_attack(self) -> int:
        return self._attack

    def get_health(self) -> int:
        return self._health

    def get_card_info(self) -> dict:
        return super().get_card_info() | {
            "type": "Creature",
            "attack": self.get_attack(),
            "health": self.get_health()
        }

    def play(self, game_state: dict) -> dict:
        if self.is_playable(game_state["available_mana"]):
            play_result: dict = {
                "card_played": self.name,
                "mana_used": self.cost,
                "effect": "Creature summoned to battlefield"
            }
            print(f"Play result: {play_result}\n")
            game_state["available_mana"] -= self.cost
        else:
            play_result = {}
            print(
                f"Play result: Impossible to play {self.name} with "
                f"{game_state['available_mana']} mana available"
                f" - {self.cost} needed\n"
            )
        return play_result

    def attack_target(self, target) -> dict:
        print(f"{self.name} attacks {target.name}:")
        if target.get_health() - self.get_attack() <= 0:
            combat_over: bool = True
        else:
            combat_over = False
        attack_result: dict = {
            "attacker": self.name,
            "target": target.name,
            "damage_dealt": self.get_attack(),
            "combat_resolved": combat_over
        }
        print(f"Attack result: {attack_result}\n")
        return attack_result
