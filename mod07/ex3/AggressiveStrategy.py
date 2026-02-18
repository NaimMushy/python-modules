from .GameStrategy import GameStrategy
from ex0.Card import Card
from ex0.CreatureCard import CreatureCard
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
        if not game_state["hand"]:
            return {}
        card_chosen: Card = random.choice(game_state["hand"])
        play_result: dict = card_chosen.play(game_state)
        if not play_result:
            return {}
        match card_chosen.__repr__():
            case "spells":
                targets: list[Card] = game_state[
                    card_chosen.get_correct_targets()
                ]
                offensive: bool = (
                    True if "damage" in card_chosen.effect_type
                    else False
                )
                effect_val: int = card_chosen.effect_value
            case "artifacts":
                targets = game_state[
                    card_chosen.activate_ability()["targets"]
                ]
                effect_val = card_chosen.effect_value
                offensive = (
                    True if (
                        "health" in card_chosen.effect
                        and effect_val < 0
                    )
                    else False
                )
            case "creatures":
                targets = [game_state["priority_target"]]
                offensive = True
                effect_val = card_chosen.get_attack()
        return {
            "card_played": card_chosen,
            "targets": (
                [] if not offensive
                else targets
            ),
            "mana_used": card_chosen.cost,
            "damage_dealt": (
                effect_val * (
                    -1 if effect_val < 0
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
