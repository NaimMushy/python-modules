from ex0.Card import Card
from .Deck import Deck
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
        if not self.is_playable(game_state["available_mana"]):
            print(
                f"Impossible to play {self.name} "
                f"with {game_state['available_mana']} available: "
                f"{self.cost} needed\n"
            )
            return {}
        effect: str | list = self.activate_ability()["effect"]
        target: str = self.activate_ability()["target"]
        if "ally" in target:
            game_state["all_targets"] = game_state["hand"]
            game_state["living_targets"] = game_state["ally_beings"]
        if "beings" in target:
            game_state["all_targets"] = game_state["living_targets"]
        if "mana" in target:
            game_state["enemy_mana"] -= self.effect[1]
            self.durability -= 1
        elif game_state["all_targets"]:
            self.apply_effect(
                effect,
                game_state["all_targets"]
            )
            self.durability -= 1
        else:
            print(f"No targets available for {self.name}\n")
            return {}
        play_result: dict = {
            "card_played": self.name,
            "mana_used": self.cost,
            "effect": self.effect
        }
        print(f"Playing artifact {self.name}...")
        print(f"Play result: {play_result}\n")
        if self.durability <= 0:
            print(
                f"Artifact {self.name} "
                "destroyed - durability depleted\n"
            )
            game_state["cards_to_remove"].append(self)
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
            if "attack" in effect_type or "health" in effect_type:
                target += " beings"
            return {
                "permanent": permanent,
                "effect": [effect_type, effect_value],
                "target": target,
                "repeat": repeat_per_turn
            }
        else:
            return {"effect": "unknown", "target": None}

    def apply_effect(self, effect: list | str, targets: list[Card]) -> None:
        if isinstance(effect, str) and effect == "unknown":
            print("No card effect for this turn\n")
            return None
        if not targets:
            print(f"No available targets for {self.name}\n")
            return None
        if "health" in effect[0]:
            for target in targets:
                target.set_health(target.get_health() + effect[1])
                if isinstance(effect[1], int) and effect[1] > 0:
                    print(
                        f"Effect < +{effect[1]} health points > "
                        f"applied to {target.name}"
                    )
                else:
                    print(
                        f"Effect < {effect[1]} health points > "
                        f"applied to {target.name}"
                    )
        elif "attack" in effect[0]:
            for target in targets:
                target.set_attack(
                    target.get_attack() + effect[1]
                )
                if isinstance(effect[1], int) and effect[1] > 0:
                    print(
                        f"Effect < +{effect[1]} attack > "
                        f"applied to {target.name}"
                    )
                else:
                    print(
                        f"Effect < {effect[1]} attack > "
                        f"applied to {target.name}"
                    )
        elif "mana cost" in effect[0]:
            for target in targets:
                target.cost += effect[1]
                if isinstance(effect[1], int) and effect[1] > 0:
                    print(
                        f"Effect < +{effect[1]} mana cost > "
                        f"applied to {target.name}"
                    )
                else:
                    print(
                        f"Effect < {effect[1]} mana cost > "
                        f"applied to {target.name}"
                    )
        print("")

    def get_card_info(self) -> dict:
        return super().get_card_info() | {
            "type": "Artifact",
            "durability": self.durability,
            "effect": self.effect
        }

    def __repr__(self) -> str:
        return "artifacts"
