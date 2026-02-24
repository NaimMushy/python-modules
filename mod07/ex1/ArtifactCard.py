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

        super().__init__(name, cost, rarity, "artifacts")
        self.durability: int = durability
        self.effect: str = effect
        self.effect_value: int = self.get_effect_value()

    def play(self, game_state: dict) -> dict:

        if not self.is_playable(game_state["available_mana"]):

            print(
                f"\nImpossible to play {self.name} "
                f"with {game_state['available_mana']} available: "
                f"{self.cost} needed\n"
            )
            return {}

        print(f"\n-> Playing Artifact {self.name}...\n")

        targets: str = self.activate_ability()["targets"]

        if not game_state[targets]:

            print(f"No available targets for {self.name}\n")
            return {}

        if "mana" in targets:

            game_state[targets] += self.effect_value

            print(
                f"Effect < {'+' if self.effect_value > 0 else ''}"
                f"{self.effect_value} available mana > "
                f"applied to {targets.replace('_', ' ')}\n"
            )

            if game_state[targets] < 0:
                game_state[targets] = 0

        else:
            self.apply_effect(game_state[targets])

        self.durability -= 1

        play_result: dict = {
            "card_played": self.name,
            "mana_used": self.cost,
            "effect": self.effect
        }

        print(f"Play result: {play_result}\n")

        if self.durability <= 0:
            print(
                f"Artifact {self.name} "
                "destroyed - Durability depleted\n"
            )
            game_state["cards_to_remove"].append(self)

        return play_result

    def get_effect_value(self) -> int:

        if (match := re.match(
            "[a-z]+: ([-+][0-9]+) [a-z ]+",
            self.effect,
            re.I
        )):
            return int(match.group(1))

        return 0

    def activate_ability(self) -> dict:

        if "attack" in self.effect or "health" in self.effect:
            targets: str = (
                "ally_beings" if self.effect_value > 0
                else "living_targets"
            )

        elif "mana cost" in self.effect:
            targets = (
                "hand" if self.effect_value < 0
                else "all_targets"
            )

        else:
            targets = (
                "available_mana" if self.effect_value > 0
                else "enemy_mana"
            )

        return {
            "effect": self.effect,
            "targets": targets
        }

    def apply_effect(self, targets: list[Card]) -> None:

        if not targets:

            print(f"No available targets for {self.name}\n")
            return None

        sign: str = "+" if self.effect_value > 0 else ""

        if "health" in self.effect:

            for target in targets:
                target.set_health(target.get_health() + self.effect_value)
                print(
                    f"Effect < {sign}"
                    f"{self.effect_value} health points > "
                    f"applied to {target.name}"
                )

        elif "attack" in self.effect:

            for target in targets:
                target.set_attack(
                    target.get_attack() + self.effect_value
                )
                print(
                    f"Effect < {sign}"
                    f"{self.effect_value} attack > "
                    f"applied to {target.name}"
                )

        elif "mana cost" in self.effect:

            for target in targets:
                target.cost += self.effect_value
                print(
                    f"Effect < {sign}"
                    f"{self.effect_value} mana cost > "
                    f"applied to {target.name}"
                )

                if target.cost < 0:
                    target.cost = 0

        print("")

    def get_card_info(self) -> dict:

        return super().get_card_info() | {
            "type": "Artifact",
            "durability": self.durability,
            "effect": self.effect
        }
