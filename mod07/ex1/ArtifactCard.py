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
            "([a-z]+): ([-+][0-9]+) ([a-z ]+)",
            self.effect,
            re.I
        )):
            permanent: bool = match.group(1) == "Permanent"
            effect_value: int = int(match.group(2))
            effect_type: str = match.group(3)
            repeat_per_turn: bool = "per turn" in match.group(3)
            if (
                ("mana cost" in effect_type and effect_value < 0) or
                ("mana cost" not in effect_type and effect_value > 0)
            ):
                target: str = "ally"
            elif "mana" in effect_type and "cost" not in effect_type:
                if effect_value < 0:
                    target = "enemy_deck_mana"
                else:
                    target = "ally_deck_mana"
            else:
                target = "enemy"
            return {
                "permanent": permanent,
                "effect": [effect_type, effect_value],
                "target": target,
                "repeat": repeat_per_turn
            }
        else:
            return {"effect": "unknown"}

    def get_card_info(self) -> dict:
        return super().get_card_info() | {
            "type": "Artifact",
            "durability": self.durability,
            "effect": self.effect
        }
