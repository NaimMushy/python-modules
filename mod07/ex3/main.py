from .AggressiveStrategy import AggressiveStrategy
from .FantasyCardFactory import FantasyCardFactory
from .GameEngine import GameEngine


def main() -> None:

    print("\n==== DataDeck Game Engine ====\n")

    game_engine: GameEngine = GameEngine()

    game_engine.configure_engine(
        FantasyCardFactory(),
        AggressiveStrategy()
    )

    default_turn_nb: int = 10

    try:

        turn_number: int = int(input(
            "\n\nEnter the number of turns to simulate: "
        ))

    except ValueError:

        print(
            f"\nInvalid value given for number of turns"
            f" - Resorting to default number [{default_turn_nb}]\n"
        )
        turn_number = default_turn_nb

    continuing: bool = (
        True if input("\n\n-> STARTING GAME? (Y/n): ") in ["y", "Y", ""]
        else False
    )

    while continuing and turn_number > game_engine.turns_simulated:

        print("")

        game_engine.simulate_turn()

        if turn_number > game_engine.turns_simulated:

            continuing = (
                True if input(
                    f"\n[{game_engine.turns_simulated}/{turn_number}]"
                    " -> NEXT TURN? (Y/n): "
                ) in ["y", "Y", ""]
                else False
            )

    game_engine.get_engine_status()

    print(
        "\nAbstract Factory + Strategy Pattern: "
        "Maximum flexibility achieved!\n"
    )


if __name__ == "__main__":
    main()
