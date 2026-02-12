from .GameStrategy import GameStrategy
from ex0.Card import Card
from ex0.CreatureCard import CreatureCard
from ex1.SpellCard import SpellCard
from ex1.ArtifactCard import ArtifactCard
from ex1.Deck import Deck
from ex2.EliteCard import EliteCard
import random


class AggressiveStrategy(GameStrategy):
    def execute_turn(self, hand: list, battlefield: list) -> dict:
        game_state: dict = {
            "hand": hand[0],
            "all_targets": battlefield[0],
            "available_mana": hand[1],
            "enemy_mana": battlefield[1],
            "ally_beings": hand[2],
            "living_targets": battlefield[2],
            "priority_target": (
                None if not battlefield[2]
                else random.choice(battlefield[2])
            ),
            "cards_to_remove": []
        }
        turn_result: dict = {
            "cards_played": [],
            "targets_attacked": [],
            "mana_used": 0,
            "damage_dealt": 0
        }
        if not game_state["hand"] and not game_state["all_targets"]:
            return turn_result
        attacker: Card | None = (
            None if not self.prioritize_targets(game_state["ally_beings"])
            else random.choice(self.prioritize_targets(
                game_state["ally_beings"]
            ))
        )
        if attacker:
            attack_result: dict = attacker.play(game_state)
            if attack_result:
                if attacker.name not in turn_result["cards_played"]:
                    turn_result["cards_played"].append(attacker.name)
                if (
                    game_state["priority_target"].name
                    not in turn_result["targets_attacked"]
                ):
                    turn_result["targets_attacked"].append(
                        game_state["priority_target"].name
                    )
                turn_result["mana_used"] += attacker.cost
                turn_result["damage_dealt"] += attacker.get_attack()
                game_state["available_mana"] -= attacker.cost
        card_to_play: Card = random.choice([
            card for card in hand
            if isinstance(card, (SpellCard, ArtifactCard))
        ])
        if not card_to_play:
            return turn_result
        play_result: dict = card_to_play.play(game_state)
        if not play_result:
            return turn_result
        targets: list[Card] = []
        if isinstance(card_to_play, SpellCard):
            spell_targets: list[Card] = card_to_play.get_correct_targets(
                game_state
            )
            if spell_targets and (
                spell_targets == game_state["living_targets"]
                or spell_targets == game_state["all_targets"]
            ):
                targets = spell_targets
                turn_result["damage_dealt"] += card_to_play.get_effect_value()
        elif isinstance(card_to_play, ArtifactCard):
            artifact_target: str = card_to_play.activate_ability()["target"]
            if "mana" not in artifact_target and "enemy" in artifact_target:
                targets = (
                    game_state["living_targets"] if "beings" in artifact_target
                    else game_state["all_targets"]
                )
                turn_result["damage_dealt"] += card_to_play.get_effect_value()
        if card_to_play.name not in turn_result["cards_played"]:
            turn_result["cards_played"].append(card_to_play.name)
        turn_result["mana_used"] += play_result["mana_used"]
        for target in targets:
            if target.name not in turn_result["targets_attacked"]:
                turn_result["targets_attacked"].append(target.name)
        return turn_result

    def prioritize_targets(self, available_targets: list) -> list:
        return [
            card for card in available_targets
            if isinstance(card, CreatureCard)
            and card.cost <= 7
        ]

    def get_strategy_name(self) -> str:
        return "Aggressive Strategy"
