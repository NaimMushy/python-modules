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

        super().__init__(name, cost, rarity, "creatures")
        self.set_attack(attack)
        self.set_health(health)

    def set_attack(self, new_attack: int) -> None:

        if isinstance(new_attack, int) and new_attack >= 0:
            self.__attack: int = new_attack

        else:
            self.__attack = 0

    def set_health(self, new_health: int) -> None:

        if isinstance(new_health, int) and new_health >= 0:
            self.__health: int = new_health

        else:
            self.__health = 0

    def get_attack(self) -> int:

        return self.__attack

    def get_health(self) -> int:

        return self.__health

    def get_card_info(self) -> dict:

        return super().get_card_info() | {
            "type": "Creature",
            "attack": self.get_attack(),
            "health": self.get_health()
        }

    def play(self, game_state: dict) -> dict:

        if not self.is_playable(game_state["available_mana"]):

            print(
                f"\nImpossible to play {self.name} with "
                f"{game_state['available_mana']} mana available"
                f" - {self.cost} needed\n"
            )
            return {}

        print(f"\n-> Playing Creature {self.name}...\n")

        if not game_state["priority_target"]:

            print(f"No available target for {self.name} to attack\n")
            return {}

        play_result: dict = {
            "card_played": self.name,
            "mana_used": self.cost,
            "effect": "Creature summoned to battlefield",
        }

        self.attack_target(game_state["priority_target"])

        print(f"Play result: {play_result}\n")

        return play_result

    def attack_target(self, target) -> dict:

        print(f"{self.name} attacks {target.name}:")

        target.set_health(target.get_health() - self.get_attack())

        attack_result: dict = {
            "attacker": self.name,
            "target": target.name,
            "damage_dealt": self.get_attack(),
            "combat_resolved": target.get_health() == 0
        }

        print(f"Attack result: {attack_result}\n")

        return attack_result
