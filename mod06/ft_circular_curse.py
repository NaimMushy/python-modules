def main() -> None:
    """
    Demonstrates how circular curses can be broken with late imports.
    """
    print("\n=== Circular Curse Breaking ===")
    print("\ntesting ingredient validation:")
    from alchemy.grimoire.validator import validate_ingredients
    print(
        "validate_ingredients('fire air'): "
        f"{validate_ingredients('fire air')}"
    )
    print(
        "validate_ingredients('dragon scales'): "
        f"{validate_ingredients('dragon scles')}"
    )
    print("\ntesting spell recording with validation:")
    from alchemy.grimoire.spellbook import record_spell
    print(
        "record_spell('fireball', 'fire air'): "
        f"{record_spell('fireball', 'fire air')}"
    )
    print(
        "record_spell('dark magic', 'shadow'): "
        f"{record_spell('dark magic', 'shadow')}"
    )
    print("\ntesting late import techniques:")
    print(
        "record_spell('lightning', 'air'): "
        f"{record_spell('lightning', 'air')}"
    )
    print("\ncircular dependency curse avoided using late imports!")
    print("all spells processed safely!")


if __name__ == "__main__":
    main()
