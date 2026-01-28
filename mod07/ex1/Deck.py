from ex0.Card import Card
import random


class Deck:
    def __init__(self) -> None:
        self.cards: list[Card] = []
        self.active_cards: list[Card] = []

    def add_card(self, card: Card) -> None:
        self.cards.append(card)

    def remove_card(self, card_name: str) -> bool:
        for card in self.cards:
            if card_name == card.name:
                self.cards.remove(card)
            return True
        return False

    def shuffle(self) -> None:
        new_deck: list[Card] = []
        for card_index in range(len(self.cards)):
            new_deck[card_index] = random.choice(self.cards)
            self.remove_card(new_deck[card_index].name)
        self.cards = new_deck

    def draw_card(self) -> Card:
        card_drawn: Card = random.choice(self.cards)
        self.remove_card(card_drawn.name)
        return card_drawn

    def get_deck_stats(self) -> dict:
        return {
            "total_cards": len(self.cards),
            "creatures": sum(
                1 for card in self.cards if card.__repr__() == "CreatureCard"
            ),
            "spells": sum(
                1 for card in self.cards if card.__repr__() == "SpellCard"
            ),
            "artifacts": sum(
                1 for card in self.cards if card.__repr__() == "ArtifactCard"
            ),
            "avg_cost": round(sum(
                card.cost for card in self.cards
            ) / len(self.cards), 1)
        }
