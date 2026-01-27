from .CreatureCard import CreatureCard


def main() -> None:
    """
    Demonstrates basic mechanisms of the Card Foundation.
    """
    print("\n=== DataDeck Card Foundation ===\n")
    print("Testing Abstract Base Class Design:\n")
    game_state: dict = {}
    game_state["available_mana"] = 10
    game_state["creatures"] = []
    game_state["targets"] = []
    fire_dragon = CreatureCard("Fire Dragon", 7, "Legendary", 7, 5)
    goblin_warrior = CreatureCard("Goblin Warrior", 4, "Common", 3, 6)
    game_state["creatures"].append(fire_dragon)
    game_state["creatures"].append(goblin_warrior)
    game_state["targets"].append(goblin_warrior)
    print(f"CreatureCard Info:\n{fire_dragon.get_card_info()}\n")
    print(
        f"Playing Fire Dragon with "
        f"{game_state['available_mana']} mana available:"
    )
    fire_dragon.play(game_state)
    fire_dragon.attack_target(goblin_warrior)
    print(
        "Testing insufficient mana "
        f"({game_state['available_mana']} available):"
    )
    fire_dragon.is_playable(game_state["available_mana"])
    print("\nAbstract pattern successfully demonstrated!")


if __name__ == "__main__":
    main()
