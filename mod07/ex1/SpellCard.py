from ex0.Card import Card
import re


class SpellCard(Card):
    def __init__(
        self,
        name: str,
        cost: int,
        rarity: str,
        effect_type: str
    ) -> None:
        super().__init__(name, cost, rarity)
        self.effect_type: str = effect_type

    def play(self, game_state: dict) -> dict:
        if self.is_playable(game_state["available_mana"]):
            play_result: dict = {
                "card_played": self.name,
                "mana_used": self.cost,
                "effect": self.effect_type
            }
            print(f"Play result: {play_result}")
            self.resolve_effect(game_state["targets"])
        else:
            play_result = {}
            print(
                f"Play result: Impossible to play {self.name} with "
                f"{game_state['available_mana']} mana available"
                f" - {self.cost} needed\n"
            )
        return play_result

    def resolve_effect(self, targets: list) -> dict:
        if (match := re.match(
            "([a-z]+) ([0-9]+) ([a-z ]+) to target",
            self.effect_type,
            re.I
        )):
            for target in targets:
                if match.group(3) == "damage":
                    target.set_health(
                        target.get_health() - match.group(2)
                    )
                elif match.group(3) == "health points":
                    target.set_health(
                        target.get_health() + match.group(2)
                    )
                elif (
                    match.group(1) == "adds" and
                    match.group(3) == "mana cost"
                ):
                    target.set_attack(
                        target.get_attack() + match.group(2)
                    )
                elif (
                    match.group(1) == "removes" and
                    match.group(3) == "mana cost"
                ):
                    target.set_attack(
                        target.get_attack() - match.group(2)
                    )
                else:
                    print("Error: unknown effect type\n")
            return {"effect": self.effect_type}
        else:
            print("Error: unknown effect type\n")
