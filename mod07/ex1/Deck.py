from ex0.Card import Card
from typing import Any as any
import random


class Deck:
    def __init__(self) -> None:
        self.stack_cards: list[Card] = []
        self.active_cards: list[Card] = []
        self.possible_targets: list[Card] = []
        self.collection: dict[str, list[Card]] = {}
        self.available_mana: int = 30

    def add_enemy_deck(self, enemy_deck: any) -> None:
        self.enemy_deck: Deck = enemy_deck

    def add_card(self, card: Card) -> None:
        self.stack_cards.append(card)
        if card.__repr__() in self.collection.keys():
            self.collection[card.__repr__()].append(card)
        else:
            self.collection[card.__repr__()] = [card]

    def remove_card(self, card_name: str) -> bool:
        for card in self.stack_cards:
            if card_name == card.name:
                self.stack_cards.remove(card)
            return True
        return False

    def remove_from_all(self, card: Card) -> None:
        if card in self.stack_cards:
            self.stack_cards.remove(card)
        if card in self.active_cards:
            self.active_cards.remove(card)
        if card in self.collection[card.__repr__()]:
            self.collection[card.__repr__()].remove(card)

    def shuffle(self) -> None:
        random.shuffle(self.stack_cards)

    def draw_card(self) -> Card:
        card_drawn: Card = self.stack_cards[0]
        self.remove_card(card_drawn.name)
        return card_drawn

    def get_deck_stats(self) -> dict:
        stats: dict = {}
        stats["total_cards"] = len(self.stack_cards) + len(self.active_cards)
        avg_cost: int = 0
        for key, val in self.collection.items():
            stats[key] = len(val)
            for card in val:
                avg_cost += card.cost
        stats["avg_cost"] = round(avg_cost / stats["total_cards"], 1)
        return stats

    def display_cards(self) -> None:
        if len(self.active_cards):
            print("=== Active Cards ===\n")
            for card in self.active_cards:
                print(f"{card.get_card_info()}\n")
        if len(self.stack_cards):
            print("=== Stack Cards ===\n")
            for card in self.stack_cards:
                print(f"{card.get_card_info()}\n")
