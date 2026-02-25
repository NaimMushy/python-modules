from .CreatureCard import CreatureCard


def main() -> None:

    print("\n==== DataDeck Card Foundation ====\n")

    print("\nTesting Abstract Base Class Design:\n")

    fire_dragon = CreatureCard("Fire Dragon", 7, "Legendary", 7, 5)
    goblin_warrior = CreatureCard("Goblin Warrior", 4, "Common", 3, 6)

    game_state: dict = {
        "available_mana": 10,
    }
    game_state["priority_target"] = goblin_warrior

    print(f"\n{' ' * 8}[CreatureCard Info]\n")

    for info_name, info_val in fire_dragon.get_card_info().items():
        print(f"{' ' * 4}=> {info_name}: {info_name}")

    print(
        f"\n\nPlaying Fire Dragon with "
        f"{game_state['available_mana']} mana available:\n"
    )
    print(
        "Playable: "
        f"{fire_dragon.is_playable(game_state['available_mana'])}\n"
    )

    play_result: dict = fire_dragon.play(game_state)

    game_state["available_mana"] -= play_result["mana_used"]

    print(
        "\nTesting insufficient mana "
        f"({game_state['available_mana']} available):\n"
    )
    print(
        "Playable: "
        f"{fire_dragon.is_playable(game_state['available_mana'])}\n"
    )

    print("\nAbstract pattern successfully demonstrated!\n")


if __name__ == "__main__":
    main()
