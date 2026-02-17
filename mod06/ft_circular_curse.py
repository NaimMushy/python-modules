def main() -> None:

    print("\n=== Circular Curse Breaking ===")

    print("\nTesting ingredient validation:")
    from alchemy.grimoire.validator import validate_ingredients
    for ingredient in ["fire air", "dragon scales"]:
        print(
            f"validate_ingredients({ingredient}): "
            f"{validate_ingredients(ingredient)}"
        )

    print("\nTesting spell recording with validation:")
    from alchemy.grimoire.spellbook import record_spell
    for spell, ingredient in {
            "Fireball": "fire air",
            "Dark Magic": "shadow"
    }.items():
        print(
            f"record_spell({spell}, {ingredient}): "
            f"{record_spell(spell, ingredient)}"
        )

    print("\nTesting late import techniques:")
    for spell, ingredient in {"Lightning": "air"}.items():
        print(
            f"record_spell({spell}, {ingredient}): "
            f"{record_spell(spell, ingredient)}"
        )

    print("\nCircular dependency curse avoided using late imports!")
    print("All spells processed safely!")


if __name__ == "__main__":
    main()
