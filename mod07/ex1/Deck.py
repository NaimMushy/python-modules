from ex0.Card import Card
from ex0.CreatureCard import CreatureCard
from .SpellCard import SpellCard
from .ArtifactCard import ArtifactCard
from typing import Any as any
import random


class Deck:
    def __init__(self) -> None:
        self.stack_cards: list[Card] = []
        self.active_cards: list[Card] = []

    def add_enemy_deck(self, enemy_deck: any) -> None:
        self.enemy_deck: Deck = enemy_deck

    def add_card(self, card: Card) -> None:
        self.stack_cards.append(card)

    def remove_card(self, card_name: str) -> bool:
        for card in self.stack_cards:
            if card_name == card.name:
                self.stack_cards.remove(card)
            return True
        return False

    def shuffle(self) -> None:
        random.shuffle(self.stack_cards)

    def draw_card(self) -> Card:
        card_drawn: Card = self.stack_cards[0]
        self.remove_card(card_drawn.name)
        return card_drawn

    def get_deck_stats(self) -> dict:
        return {
            "total_cards": len(self.stack_cards),
            "creatures": sum(
                1 for card in self.stack_cards
                if isinstance(card, CreatureCard)
            ),
            "spells": sum(
                1 for card in self.stack_cards
                if isinstance(card, SpellCard)
            ),
            "artifacts": sum(
                1 for card in self.stack_cards
                if isinstance(card, ArtifactCard)
            ),
            "avg_cost": round(sum(
                card.cost for card in self.stack_cards
            ) / len(self.stack_cards), 1)
        }

    def display_cards(self) -> None:
        if len(self.active_cards):
            print("=== Active Cards ===\n")
            for card in self.active_cards:
                print(f"{card.get_card_info()}\n")
        if len(self.stack_cards):
            print("=== Stack Cards ===\n")
            for card in self.stack_cards:
                print(f"{card.get_card_info()}\n")
