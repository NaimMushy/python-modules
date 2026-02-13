from .AggressiveStrategy import AggressiveStrategy
from .FantasyCardFactory import FantasyCardFactory
from .GameEngine import GameEngine
import sys


DEFAULT_TURN_NB: int = 5


def main() -> None:
    print("\n=== DataDeck Game Engine ===\n")
    game_engine: GameEngine = GameEngine()
    game_engine.configure_engine(
        FantasyCardFactory(),
        AggressiveStrategy()
    )
    if len(sys.argv) >= 2:
        try:
            turn_number: int = int(sys.argv[1])
        except ValueError:
            print("Caught ValueError: Integer required for number of turns!")
    else:
        print(
            "No specific number of turns provided - "
            f"Resorting to default number {DEFAULT_TURN_NB}"
        )
        turn_number = DEFAULT_TURN_NB

    continuing: bool = (
        True if input("\n-> STARTING GAME? (y/n): ") in ["y", ""]
        else False
    )
    while continuing and turn_number > game_engine.turns_simulated + 1:
        print("")
        game_engine.simulate_turn()
        continuing = (
            True if input(
                f"\n[{game_engine.turns_simulated}/{turn_number}]"
                " -> NEXT TURN? (y/n): "
            ) in ["y", ""]
            else False
        )

    game_engine.get_engine_status()
    print(
        "Abstract Factory + Strategy Pattern: "
        "Maximum flexibility achieved!"
    )


if __name__ == "__main__":
    main()
