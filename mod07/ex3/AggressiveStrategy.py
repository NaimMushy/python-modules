from .GameStrategy import GameStrategy
from ex0.Card import Card
from ex0.CreatureCard import CreatureCard
from ex1.SpellCard import SpellCard
from ex1.ArtifactCard import ArtifactCard
from ex2.EliteCard import EliteCard
import random


class AggressiveStrategy(GameStrategy):
    def execute_turn(self, hand: list, battlefield: list) -> dict:
        for item in hand:
            if not isinstance(item, Card):
                available_mana: int = item
                hand.remove(item)
        attackers: list[Card] = self.prioritize_targets(hand)
        enemy_targets: list[Card] = self.prioritize_targets(battlefield)
        cards_played: list[str] = []
        targets_attacked: list[str] = []
        damage_dealt: int = 0
        if attackers and enemy_targets:
            for card in attackers:
                if card.cost <= 3:
                    target: Card = random.choice(enemy_targets)
                    if isinstance(card, CreatureCard):
                        card.attack_target(target)
                    elif isinstance(card, EliteCard):
                        card.attack(target)
                    damage_dealt += card.get_attack()
                    cards_played.append(card.name)
                    if target.name not in targets_attacked:
                        targets_attacked.append(target.name)
        else:
            for card in hand:
                if (
                    isinstance(card, SpellCard) and
                    card.get_correct_targets(hand, battlefield)
                ):
                    card.resolve_effect(
                        card.get_correct_targets(hand, battlefield)
                    )
                    hand.remove(card)
                if isinstance(card, ArtifactCard):
                    effect: str | list = self.activate_ability()["effect"]
                    target: str = self.activate_ability()["target"]
                    if "enemy" in target:
                        targets: list[Card] = battlefield
                    elif "ally" in target:
                        targets = hand
                    if "beings" in target:
                        card.apply_effect(
                            effect,
                            self.prioritize_targets(targets)
                        )
                    else:
                        card.apply_effect(effect, targets)
                    card.durability -= 1

    def prioritize_targets(self, available_targets: list) -> list:
        return [
            card for card in available_targets
            if isinstance(card, (CreatureCard, EliteCard))
        ]

    def get_strategy_name(self) -> str:
        return "Aggressive Strategy"
