from .CardFactory import CardFactory
from .GameStrategy import GameStrategy
from ex0.Card import Card
from ex1.Deck import Deck
import random


MAX_DECK_SIZE: int = 21


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
        print(f"Strategy: {self.strategy.__class__.__name__}\n")
        self.factory.display_supported_types()

        deck_size: int = random.randint(3, MAX_DECK_SIZE)

        self.player1: Deck = self.create_deck(deck_size)
        self.player2: Deck = self.create_deck(deck_size)

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

        for turn in range(2):
            print(f"< Player {self.player1.player}'s turn >\n")

            cards_played: list[Card] = []
            targets_attacked: list[str] = []
            total_mana_used: int = 0
            total_damage: int = 0
            draw_number: int = (
                3 if len(self.player1.stack_cards) >= 3
                else len(self.player1.stack_cards)
            )

            if not draw_number:
                print(f"No cards left to draw for {self.player1.player}!")
            else:
                for draw in range(draw_number):
                    self.player1.draw_card()

            self.player1.display_hand()

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
                    if turn_result["card_played"] not in cards_played:
                        cards_played.append(turn_result["card_played"])
                    targets_attacked += [
                        target.name for target in turn_result["targets"]
                        if target.name not in targets_attacked
                    ]
                    self.player2.check_card_health()
                    total_damage += turn_result["damage_dealt"]
                    total_mana_used += turn_result["mana_used"]

            actions_result: dict = {
                "cards_played": [card.name for card in cards_played],
                "mana_used": total_mana_used,
                "targets_attacked": targets_attacked,
                "damage_dealt": total_damage
            }
            self.turns_simulated += 1
            self.total_damage += total_damage
            print("\nTurn execution:")
            print(f"Strategy: {self.strategy.get_strategy_name()}")
            print(f"Actions: {actions_result}\n")
            if (
                not self.player2.hand and not self.player2.stack_cards
            ) or not self.player2.available_mana:
                print(f"\n=== [END] Player {self.player1.player} has won!!! ===")
                break
            if not self.player1.available_mana:
                print(f"\n=== [END] Player {self.player2.player} has won!!! ===")
                break
            else:
                self.player1.available_mana += 5
                self.player1, self.player2 = self.player2, self.player1
        return actions_result

    def get_engine_status(self) -> dict:
        report: dict = {
            "turns_simulated": self.turns_simulated,
            "strategy_used": self.strategy.get_strategy_name(),
            "total_damage": self.total_damage,
            "cards_created": self.cards_created
        }
        print(f"\nGame Report:\n{report}\n")
        return report
