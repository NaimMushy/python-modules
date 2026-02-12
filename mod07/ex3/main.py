from .AggressiveStrategy import AggressiveStrategy
from .FantasyCardFactory import FantasyCardFactory
from .GameEngine import GameEngine


def main() -> None:
    print("\n=== DataDeck Game Engine ===\n")
    game_engine: GameEngine = GameEngine()
    game_engine.configure_engine(
        FantasyCardFactory(),
        AggressiveStrategy()
    )
    for turn in range(5):
        game_engine.simulate_turn()

    game_engine.get_engine_status()
    print(
        "Abstract Factory + Strategy Pattern: "
        "Maximum flexibility achieved!"
    )


if __name__ == "__main__":
    main()
