from .CardFactory import CardFactory
from .GameStrategy import GameStrategy
from ex0.Card import Card
from ex0.CreatureCard import CreatureCard
from ex1.Deck import Deck
import random


MAX_DECK_SIZE: int = 16


class GameEngine:
    def configure_engine(
        self,
        factory: CardFactory,
        strategy: GameStrategy
    ) -> None:

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

        self.player1.shuffle()
        self.player2.shuffle()

    def create_deck(self, size: int) -> Deck:
        deck: Deck = Deck(input("Enter player name: "))
        cards: list[Card] = (
            self.factory.create_themed_deck(size)["total_cards"]
        )
        for card in cards:
            deck.add_card(card)
            self.cards_created += 1
        return deck

    def simulate_turn(self) -> dict:
        print(f"Simulating {self.strategy.get_strategy_type()} turn...")

        self.player1, self.player2 = self.player2, self.player1
        cards_played: list[str] = []
        targets_attacked: list[str] = []
        total_mana_used: int = 0

        for draw in range(3):
            card_drawn: Card = self.player1.draw_card()
            if card_drawn not in self.player1.hand:
                self.player1.hand.append(card_drawn)
            if isinstance(card_drawn, (CreatureCard)):
                self.player1.living_beings.append(card_drawn)

        self.display_hand(self.player1)

        for play in range(2):
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
            if turn_result:
                self.player1.available_mana -= turn_result["mana_used"]
                self.player2.available_mana = (
                    turn_result["game_state"]["enemy_mana"]
                )
                for card in turn_result["game_state"]["cards_to_remove"]:
                    self.player1.remove_from_all(card)
                if turn_result["card_played"].name not in cards_played:
                    cards_played.append(turn_result["card_played"].name)
                targets_attacked += [
                    target.name for target in turn_result["targets_attacked"]
                    if target.name not in targets_attacked
                ]
                self.turns_simulated += 1
                self.total_damage += turn_result["damage_dealt"]
                total_mana_used += turn_result["mana_used"]
                self.player2.check_card_health()

        actions_result: dict = {
            "cards_played": cards_played,
            "mana_used": total_mana_used,
            "targets_attacked": targets_attacked,
            "damage_dealt": self.total_damage
        }
        print("Turn execution:")
        print(f"Strategy: {self.strategy.get_strategy_name()}")
        print(f"Actions: {actions_result}\n")
        return actions_result

    def display_hand(self, player: Deck) -> None:
        print("Hand: [", end="")
        fst: bool = True
        for card in player.hand:
            if not fst:
                print(", ", end="")
            print(f"{card.name} ({card.cost})", end="")
            fst = False
        print("]\n")

    def get_engine_status(self) -> dict:
        report: dict = {
            "turns_simulated": self.turns_simulated,
            "strategy_used": self.strategy.get_strategy_name(),
            "total_damage": self.total_damage,
            "cards_created": self.cards_created
        }
        print(f"Game Report:\n{report}")
        return report
