from .CardFactory import CardFactory
from .GameStrategy import GameStrategy
from ex1.Deck import Deck
import random


MAX_DECK_SIZE: int = 16


class GameEngine:
    def configure_engine(
        self,
        factory: CardFactory,
        strategy: GameStrategy
    ) -> None:
        print("\n=== DataDeck Game Engine ===\n")

        self.factory: CardFactory = factory
        self.strategy: GameStrategy = strategy
        self.turns_simulated: int = 0
        self.total_damage: int = 0
        self.cards_created: int = 0

        print(
            f"Configuring {self.factory.get_factory_type()} Card Game..."
        )
        print(f"Factory: {self.factory.__class__.__name__}")
        print(f"Strategy: {self.strategy.__class__.__name__}")
        self.factory.display_supported_types()

        self.player1: Deck = self.create_deck(random.randint(1, MAX_DECK_SIZE))
        self.player2: Deck = self.create_deck(random.randint(1, MAX_DECK_SIZE))

    def create_deck(self, size: int) -> Deck:
        deck: Deck = Deck()
        cards: list[Card] = self.factory.create_themed_deck(size)["total_cards"]
        for card in cards:
            deck.add_card(card)
        return deck

    def simulate_turn(self) -> dict:
        print(f"Simulating {self.strategy.get_strategy_type()} turn...\n")

        self.player1, self.player2 = self.player2, self.player1

        for draw in range(3):
            card_drawn: Card = self.player1.draw_card()
            if card_drawn not in self.player1.hand:
                self.player1.hand.append(card_drawn)
            if isinstance(card_drawn, (CreatureCard)):
                self.player1.living_beings.append(card_drawn)

        turn_result: dict = self.strategy.execute_turn(
            [
                self.player1.hand,
                self.player1.living_beings,
                self.player1.available_mana,
            ],
            [
                self.player2.hand,
                self.player2.living_beings,
                self.player2.available_mana
            ]
        )
