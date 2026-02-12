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
        if not self.is_playable(game_state["available_mana"]):
            print(
                f"Impossible to play {self.name} "
                f"with {game_state['available_mana']} available: "
                f"{self.cost} needed\n"
            )
            return {}
        targets: list[Card] = self.get_correct_targets(game_state)
        if not targets:
            print(f"No targets available for {self.name}\n")
            return {}
        play_result: dict = {
            "card_played": self.name,
            "mana_used": self.cost,
            "effect": self.effect_type
        }
        print(f"Playing spell {self.name}...")
        print(f"Play result: {play_result}\n")
        self.resolve_effect(targets)
        game_state["cards_to_remove"].append(self)
        return play_result

    def get_correct_targets(self, game_state: dict) -> list[Card]:
        if "mana cost" in self.effect_type or "attack" in self.effect_type:
            return (
                game_state["hand"] if "Removes" in self.effect_type
                else game_state["all_targets"]
            )
        if "damage" in self.effect_type:
            return game_state["living_targets"]
        return game_state["ally_beings"]

    def resolve_effect(self, targets: list) -> dict:
        if not targets:
            print(f"No targets available for {self.name}\n")
            return {"effect": "unknown", "target": None}
        if (match := re.match(
            "([a-z ]+) ([0-9]+) ([a-z ]+)",
            self.effect_type,
            re.I
        )):
            effect_type: str = match.group(3).replace(" to target", "")
            effect_type = effect_type.replace(" ", "")
            if "mana" in effect_type:
                effect_type = "mana cost"
            if "damage" in effect_type or (
                ("attack" in effect_type or "mana" in effect_type)
                and "Removes" in match.group(1)
            ):
                effect_value: int = -(int(match.group(2)))
            else:
                effect_value = int(match.group(2))
            for target in targets:
                if "damage" in effect_type or "health" in effect_type:
                    target.set_health(
                        target.get_health() + effect_value
                    )
                elif "attack" in effect_type:
                    target.set_attack(
                        target.get_attack() + effect_value
                    )
                elif "mana" in effect_type:
                    target.cost += effect_value
                else:
                    return {"effect": "unknown", "target": None}
                print(
                    f"Spell effect < {self.effect_type} > "
                    f"applied to {target}\n"
                )
            print("")
            return {
                "effect": [effect_type, effect_value],
                "targets": [target.name for target in targets]
            }
        else:
            return {"effect": "unknown", "target": None}

    def get_card_info(self) -> dict:
        return super().get_card_info() | {
            "type": "Spell",
            "effect": self.effect_type
        }

    def __repr__(self) -> str:
        return "spells"
