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

        super().__init__(name, cost, rarity, "spells")
        self.effect_type: str = effect_type
        self.effect_value: int = 0

        if (match := re.match(
            "[a-z]+ ([0-9]+) ([a-z]+) [a-z ]+",
            self.effect_type,
            re.I
        )):
            self.effect_value = (

                int(match.group(1)) if (
                    "Restores" in self.effect_type
                    or "Adds" in self.effect_type
                ) else -int(match.group(1))

            )

    def play(self, game_state: dict) -> dict:

        if not self.is_playable(game_state["available_mana"]):

            print(
                f"\nImpossible to play {self.name} "
                f"with {game_state['available_mana']} available: "
                f"{self.cost} needed\n"
            )
            return {}

        print(f"\n-> Playing Spell {self.name}...\n")

        targets: list[Card] = game_state[self.get_correct_targets()]

        if not targets:

            print(f"No targets available for {self.name}\n")
            return {}

        play_result: dict = {
            "card_played": self.name,
            "mana_used": self.cost,
            "effect": self.effect_type
        }

        self.resolve_effect(targets)

        print(f"Play result: {play_result}\n")

        game_state["cards_to_remove"].append(self)

        return play_result

    def get_correct_targets(self) -> str:

        if "mana cost" in self.effect_type:

            return (
                "hand" if "Removes" in self.effect_type
                else "all_targets"
            )

        if "attack" in self.effect_type:

            return (
                "ally_beings" if "Adds" in self.effect_type
                else "living_targets"
            )

        if "damage" in self.effect_type:

            return "living_targets"

        return "ally_beings"

    def resolve_effect(self, targets: list) -> dict:

        if not targets:

            print(f"No targets available for {self.name}\n")
            return {"effect": "unknown", "target": None}

        for target in targets:

            if "damage" in self.effect_type or "health" in self.effect_type:
                target.set_health(
                    target.get_health() + self.effect_value
                )

            elif "attack" in self.effect_type:
                target.set_attack(
                    target.get_attack() + self.effect_value
                )

            elif "mana" in self.effect_type:
                target.cost += self.effect_value
                if target.cost < 0:
                    target.cost = 0

            else:
                return {"effect": "unknown", "targets": None}

            print(
                f"Spell effect < {self.effect_type} > "
                f"applied to {target.name}"
            )

        print("")

        return {
            "effect": self.effect_type,
            "targets": [target.name for target in targets]
        }

    def get_card_info(self) -> dict:

        return super().get_card_info() | {
            "type": "Spell",
            "effect": self.effect_type
        }
