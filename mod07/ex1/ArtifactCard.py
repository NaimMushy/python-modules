from ex0.Card import Card
import re


class ArtifactCard(Card):
    def __init__(
        self,
        name: str,
        cost: int,
        rarity: str,
        durability: int,
        effect: str
    ) -> None:
        super().__init__(name, cost, rarity)
        self.durability: int = durability
        self.effect: str = effect

    def play(self, game_state: dict) -> dict:
        if self.is_playable(game_state["available_mana"]):
            play_result: dict = {
                "card_played": self.name,
                "mana_used": self.cost,
                "effect": self.effect
            }
            print(f"Play result: {play_result}\n")
            game_state["last_played"] = self.activate_ability()
        else:
            play_result = {}
            print(
                f"Play result: Impossible to play {self.name} with "
                f"{game_state['available_mana']} mana available"
                f" - {self.cost} needed\n"
            )
        return play_result

    def activate_ability(self) -> dict:
        if (match := re.match(
            "([a-z]+): ([-+]?[0-9]+) ([a-z]+) ([a-z ]+?)",
            self.effect,
            re.I
        )):
            permanent: bool = match.group(1) == "Permanent"
            effect_value: int = int(match.group(2))
            effect_type: str = match.group(3)
            repeat_per_turn: bool = match.group(4) == "per turn"
            return {
                "permanent": permanent,
                "effect": [effect_value, effect_type],
                "repeat": repeat_per_turn
            }
        else:
            return {"effect": "unknown"}
