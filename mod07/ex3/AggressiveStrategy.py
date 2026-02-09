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
        game_state: dict = {}
        for item in hand:
            if not isinstance(item, Card):
                game_state["available_mana"] = item
                hand.remove(item)
        game_state["deck"] = Deck(hand)
        game_state["enemy_deck"] = Deck(battlefield)
        attackers: list[Card] = self.prioritize_targets(hand)
        enemy_targets: list[Card] = self.prioritize_targets(battlefield)
        action_result: dict = {
            "cards_played": [],
            "targets_attacked": [],
            "mana_used": 0,
            "damage_dealt": 0
        }
        if attackers and enemy_targets:
            for card in attackers:
                if action_result["cards_played"]:
                    break
                if card.cost <= 3:
                    game_state["targets"] = [random.choice(enemy_targets)]
                    play_result: dict = card.play(game_state)
                    action_result["cards_played"].append(card.name)
                    if (
                        isinstance(card, EliteCard) and
                        "spell" in play_result["effects"]
                    ):
                        game_state["targets"] = enemy_targets
                    for target in game_state["targets"]:
                        if (
                            target.name not in
                            action_result["targets_attacked"]
                        ):
                            action_result["targets_attacked"].append(
                                target.name
                            )
        card_to_play: Card = random.choice([
            card for card in hand
            if isinstance(card, (SpellCard, ArtifactCard))
        ])
        if not card_to_play:
            return action_result
        if isinstance(card_to_play, SpellCard):
            play_result = card_to_play.resolve_effect(enemy_targets)
            action_result["mana_used"] += (
                0 if play_result["target"]
                else card_to_play.cost
            )
            targets: list[Card] = (
                battlefield
                if card_to_play.get_correct_targets(
                    hand,
                    battlefield
                ) == battlefield
                and play_result["target"]
                else []
            )
        elif isinstance(card, ArtifactCard):
            play_result = card_to_play.play(game_state)
            if not play_result:
                return action_result
            if "mana" not in card_to_play.activate_ability()["target"]:
                if "ally" in card_to_play.activate_ability()["target"]:
                    targets = hand
                else:
                    targets = battlefield
        for target in targets:
            if target.name not in action_result["targets_attacked"]:
                action_result["targets_attacked"].append(target.name)
        return action_result

    def prioritize_targets(self, available_targets: list) -> list:
        return [
            card for card in available_targets
            if isinstance(card, (CreatureCard, EliteCard))
        ]

    def get_strategy_name(self) -> str:
        return "Aggressive Strategy"
