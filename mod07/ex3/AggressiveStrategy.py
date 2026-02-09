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
                hand.remove(item)
        attackers: list[Card] = self.prioritize_targets(hand)
        enemy_targets: list[Card] = self.prioritize_targets(battlefield)
        cards_played: list[str] = []
        targets_attacked: list[str] = []
        mana_used: int = 0
        damage_dealt: int = 0
        if attackers and enemy_targets:
            for card in attackers:
                if card.cost <= 3:
                    target: Card = random.choice(enemy_targets)
                    if isinstance(card, CreatureCard):
                        card.attack_target(target)
                        mana_used += card.cost
                        damage_dealt += card.get_attack()
                        if target.name not in targets_attacked:
                            targets_attacked.append(target.name)
                    elif isinstance(card, EliteCard):
                        active_spells: list[SpellCard] = [
                            spell for spell in hand
                            if isinstance(spell, SpellCard)
                            and spell.name in card.known_spells
                        ]
                        if active_spells:
                            spell_to_cast: SpellCard = (
                                random.choice(active_spells)
                            )
                            cast_result: dict = card.cast_spell(
                                spell_to_cast,
                                enemy_targets
                            )
                            if cast_result["success"]:
                                hand.remove(spell_to_cast)
                                for target in enemy_targets:
                                    if target.name not in targets_attacked:
                                        targets_attacked.append(target.name)
                        else:
                            card.attack(target)
                            damage_dealt += card.get_attack()
                            if target.name not in targets_attacked:
                                targets_attacked.append(target.name)
                    cards_played.append(card.name)
        else:
            card_to_play: Card = random.choice([
                card for card in hand
                if isinstance(card, (SpellCard, ArtifactCard))
            ])
            if (
                isinstance(card_to_play, SpellCard) and
                card_to_play.get_correct_targets(hand, battlefield)
            ):
                targets: list[Card] = card_to_play.get_correct_targets(
                    hand,
                    battlefield
                )
                card_to_play.resolve_effect(targets)
                hand.remove(card)
            if isinstance(card, ArtifactCard):
                effect: str | list = self.activate_ability()["effect"]
                target: str = self.activate_ability()["target"]
                if "enemy" in target:
                    targets: list[Card] = battlefield
                elif "ally" in target:
                    targets = hand
                if "beings" in target:
                    targets = self.prioritize_targets(targets)
                    card.apply_effect(effect, targets)
                for target in targets:
                    if target.name not in targets_attacked:
                        targets_attacked.append(target.name)
                card.durability -= 1
            cards_played.append(card_to_play.name)
            mana_used += card.cost
            for target in targets:
                if target.name not in targets_attacked:
                    targets_attacked.append(target.name)
        return {
            "cards_played": cards_played,
            "mana_used": mana_used,
            "targets_attacked": targets_attacked,
            "damage_dealt": damage_dealt
        }

    def handle_elites(
        elite: EliteCard,
        spells: list[SpellCard],
        targets: list[Card]
    ) -> dict:
        if spells:
            spell_to_cast: SpellCard = random.choice(spells)
            return elite.cast_spell(
                spell_to_cast,
                targets
            )
        else:
            return elite.attack(random.choice(targets))

    def prioritize_targets(self, available_targets: list) -> list:
        return [
            card for card in available_targets
            if isinstance(card, (CreatureCard, EliteCard))
        ]

    def get_strategy_name(self) -> str:
        return "Aggressive Strategy"
