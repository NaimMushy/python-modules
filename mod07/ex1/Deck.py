from ex0.Card import Card
from .SpellCard import SpellCard
from .ArtifactCard import ArtifactCard
import random


class Deck:
    def __init__(self, player: str = "Anonymous") -> None:

        self.stack_cards: list[Card] = []
        self.hand: list[Card] = []
        self.living_beings: list[Card] = []
        self.collection: dict[str, list[Card]] = {}
        self.available_mana: int = 40
        self.player: str = player.capitalize()

    def add_card(self, card: Card) -> None:

        self.stack_cards.append(card)

        if card.card_type in self.collection.keys():
            self.collection[card.card_type].append(card)

        else:
            self.collection[card.card_type] = [card]

    def remove_card(self, card_name: str) -> bool:

        for card in self.stack_cards:

            if card_name == card.name:
                self.stack_cards.remove(card)

            return True

        return False

    def remove_from_all(self, card: Card) -> None:

        if card in self.stack_cards:
            self.stack_cards.remove(card)

        if card in self.hand:
            self.hand.remove(card)

        if card in self.living_beings:
            self.living_beings.remove(card)

        if card in self.collection[card.card_type]:
            self.collection[card.card_type].remove(card)

    def shuffle(self) -> None:

        random.shuffle(self.stack_cards)

    def draw_card(self) -> Card | None:

        if not self.stack_cards:

            print("Impossible to draw a card: Stack empty!\n")
            return None

        card_drawn: Card = self.stack_cards[0]

        print(
            f"{' ' * 2}Drew: {card_drawn.name} "
            f"({card_drawn.get_card_info()['type']})\n"
        )

        self.remove_card(card_drawn.name)
        self.hand.append(card_drawn)

        if not isinstance(card_drawn, (SpellCard, ArtifactCard)):
            self.living_beings.append(card_drawn)

        return card_drawn

    def get_deck_stats(self) -> dict:

        stats: dict = {}

        stats["total_cards"] = len(self.stack_cards) + len(self.hand)

        avg_cost: int = 0

        for key, val in self.collection.items():

            stats[key] = len(val)

            for card in val:
                avg_cost += card.cost

        stats["avg_cost"] = round(avg_cost / stats["total_cards"], 1)

        return stats

    def display_cards(self) -> None:

        if len(self.hand):

            print("=== Active Cards ===\n")
            for card in self.hand:
                print(f"{card.get_card_info()}\n")

        if len(self.stack_cards):

            print("=== Stack Cards ===\n")
            for card in self.stack_cards:
                print(f"{card.get_card_info()}\n")

    def display_hand(self) -> None:

        print("\nHand: [", end="")

        fst: bool = True

        for card in self.hand:

            if not fst:
                print(", ", end="")

            print(f"{card.name} ({card.cost})", end="")
            fst = False

        print("]\n")

    def check_card_health(self) -> None:

        for card in self.living_beings:

            if not card.get_health():

                print(
                    f"{card.__class__.__name__.replace('Card', '')} "
                    f"{card.name} has been defeated - Destroying the card\n"
                )
                self.remove_from_all(card)
