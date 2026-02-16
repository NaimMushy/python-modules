def main() -> None:
    print("\n=== Pathway Debate Mastery ===")
    print("\nTesting absolute imports (from basic.py):")
    from alchemy.transmutation.basic import lead_to_gold, stone_to_gem
    print(f"lead_to_gold(): {lead_to_gold()}")
    print(f"stone_to_gem(): {stone_to_gem()}")
    print("\nTesting relative imports (from advanced.py):")
    from alchemy.transmutation.advanced import (
        philosophers_stone,
        elixir_of_life
    )
    print(f"philosophers_stone(): {philosophers_stone()}")
    print(f"elixir_of_life(): {elixir_of_life()}")
    import alchemy.transmutation
    print("\nTesting package access:")
    print(
        "alchemy.transmutation.lead_to_gold(): "
        f"{alchemy.transmutation.lead_to_gold()}"
    )
    print(
        "alchemy.transmutation.philosophers_stone(): "
        f"{alchemy.transmutation.philosophers_stone()}"
    )
    print("\nBoth pathways work! Absolute: clear, Relative: concise")


if __name__ == "__main__":
    main()
