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
        targets: list[Card] = self.get_correct_targets(
            game_state["deck"].possible_targets,
            game_state["enemy_deck"].possible_targets
        )
        if not targets:
            print(f"No targets available for {self.name}\n")
            return {}
        game_state["deck"].remove_from_all(self)
        play_result: dict = {
            "card_played": self.name,
            "mana_used": self.cost,
            "effect": self.effect_type
        }
        print(f"Playing spell {self.name}...")
        print(f"Play result: {play_result}\n")
        self.resolve_effect(targets)
        return play_result

    def get_correct_targets(
        self,
        ally_targets: list[Card],
        enemy_targets: list[Card]
    ) -> list[Card]:
        if (
            "damage" in self.effect_type or
            "Removes" in self.effect_type
        ):
            return ally_targets
        else:
            return enemy_targets

    def resolve_effect(self, targets: list) -> dict:
        if not targets:
            print(f"No targets available for {self.name}\n")
            return {"effect": "unknown", "target": None}
        if (match := re.match(
            "([a-z]+) ([0-9]+) ([a-z]+) to target",
            self.effect_type,
            re.I
        )):
            effect_type: str = match.group(3)
            if effect_type == "damage" or (
                effect_type == "attack" and match.group(1) == "removes"
            ):
                effect_value: int = -(int(match.group(2)))
            else:
                effect_value = int(match.group(2))
            for target in targets:
                if effect_type == "damage" or effect_type == "health":
                    target.set_health(
                        target.get_health() + effect_value
                    )
                elif effect_type == "attack":
                    target.set_attack(
                        target.get_attack() + effect_value
                    )
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
