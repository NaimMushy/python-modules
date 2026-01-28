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
            print(f"Play result: {play_result}\n")
            if (
                "damage" in self.effect_type or
                "Removes" in self.effect_type
            ):
                game_state["last_played"] = self.resolve_effect([
                    card for card in game_state["enemy_deck"].active_cards
                    if card.__repr__() == "CreatureCard"
                ])
            else:
                game_state["last_played"] = self.resolve_effect([
                    card for card in game_state["player_deck"].active_cards
                    if card.__repr__() == "CreatureCard"
                ])
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
                    return {"effect": "unknown"}
            return {"effect": [effect_type, effect_value]}
        else:
            return {"effect": "unknown"}
