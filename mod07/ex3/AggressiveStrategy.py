from .GameStrategy import GameStrategy
from ex0.Card import Card
from ex0.CreatureCard import CreatureCard
from ex1.SpellCard import SpellCard
from ex1.ArtifactCard import ArtifactCard
import random


class AggressiveStrategy(GameStrategy):
    def execute_turn(self, hand: list, battlefield: list) -> dict:
        game_state: dict = {
            "hand": hand[0],
            "all_targets": battlefield[0],
            "ally_beings": hand[1],
            "living_targets": battlefield[1],
            "available_mana": hand[2],
            "enemy_mana": battlefield[2],
            "priority_target": (
                None if not battlefield[1]
                else random.choice(battlefield[1])
            ),
            "cards_to_remove": []
        }
        attacker: Card | None = (
            None if not self.prioritize_targets(game_state["ally_beings"])
            else random.choice(self.prioritize_targets(
                game_state["ally_beings"]
            ))
        )
        if attacker:
            if attacker.play(game_state):
                return {
                    "card_played": attacker,
                    "targets": [game_state["priority_target"]],
                    "mana_used": attacker.cost,
                    "damage_dealt": attacker.get_attack(),
                    "game_state": game_state
                }
        spells_and_crafts: list[Card] = [
            card for card in game_state["hand"]
            if isinstance(card, (SpellCard, ArtifactCard))
        ]
        if not spells_and_crafts:
            print("No spells or artifacts detected in player's hand\n")
            return {}
        card_chosen: Card = random.choice(spells_and_crafts)
        play_result: dict = card_chosen.play(game_state)
        if not play_result:
            return {}
        if isinstance(card_chosen, SpellCard):
            targets: str = card_chosen.get_correct_targets()
            offensive: bool = (
                True if "damage" in card_chosen.effect_type
                else False
            )
        elif isinstance(card_chosen, ArtifactCard):
            targets = card_chosen.activate_ability()["targets"]
            offensive = (
                True if (
                    "health" in card_chosen.effect
                    and card_chosen.effect_value < 0
                )
                else False
            )
        return {
            "card_played": card_chosen,
            "targets": (
                [] if not offensive
                else [
                    target for target in game_state[targets]
                    if targets == "living_targets" or targets == "all_targets"
                ]
            ),
            "mana_used": card_chosen.cost,
            "damage_dealt": (
                card_chosen.effect_value * (
                    -1 if card_chosen.effect_value < 0
                    else 1
                ) if offensive
                else 0
            ),
            "game_state": game_state
        }

    def prioritize_targets(self, available_targets: list) -> list:
        return [
            card for card in available_targets
            if isinstance(card, CreatureCard)
            and card.cost <= 4
        ]

    def get_strategy_name(self) -> str:
        return "Aggressive Strategy"
