def main() -> None:
    print("\n=== Import Transmutation Mastery ===")
    print("\nmethod 1: full module import:")
    import alchemy.elements
    print(f"alchemy.elements.create_fire(): {alchemy.elements.create_fire()}")
    print("\nmethod 2: specific function import:")
    from alchemy.elements import create_water
    print(f"create_water(): {create_water()}")
    print("\nmethod 3: aliased import:")
    from alchemy.potions import healing_potion as heal
    print(f"heal(): {heal()}")
    print("\nmethod 4: multiple imports:")
    from alchemy.elements import create_earth, create_fire
    from alchemy.potions import strength_potion
    print(f"create_earth(): {create_earth()}")
    print(f"create_fire(): {create_fire()}")
    print(f"strength_potion(): {strength_potion()}")
    print("\nall import transmutation methods mastered!")


if __name__ == "__main__":
    main()
