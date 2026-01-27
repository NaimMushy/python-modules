from ex0.Card import Card


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
                "effect": self.effect_type
            }
            print(f"Play result: {play_result}")
            self.activate_ability()
        else:
            play_result = {}
            print(
                f"Play result: Impossible to play {self.name} with "
                f"{game_state['available_mana']} mana available"
                f" - {self.cost} needed\n"
            )
        return play_result

    def activate_ability(self, game_state: dict) -> dict:
