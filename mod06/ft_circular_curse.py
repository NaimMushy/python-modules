def testing_validation() -> None:
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


def testing_record_spell_with_validation() -> None:
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


def testing_late_import() -> None:
    print("\ntesting late import techniques:")
    from alchemy.grimoire.spellbook import record_spell
    print(
        "record_spell('lightning', 'air'): "
        f"{record_spell('lightning', 'air')}"
    )
    print("\ncircular dependency curse avoided using late imports!")


def main() -> None:
    print("\n=== Circular Curse Breaking ===")
    testing_validation()
    testing_record_spell_with_validation()
    testing_late_import()
    print("all spells processed safely!")


if __name__ == "__main__":
    main()
