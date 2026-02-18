import random
from typing import Callable as callable


def spell_combiner(spell1: callable, spell2: callable) -> callable:

    random_target: str = random.choice([
        "Dragon",
        "Unicorn",
        "Goblin",
        "Kraken",
        "Fairy"
    ])

    def combine_spells() -> tuple[str, str]:
        return (spell1(random_target), spell2(random_target))

    return combine_spells


def power_amplifier(base_spell: callable, multiplier: int) -> callable:

    def amplifier() -> int:
        return base_spell() * multiplier

    return amplifier


def conditional_caster(condition: callable, spell: callable) -> callable:

    random_target: str = random.choice([
        "Dragon",
        "Unicorn",
        "Goblin",
        "Kraken",
        "Fairy"
    ])

    def cast() -> str:
        if condition(random_target):
            return spell(random_target)
        else:
            return "Spell fizzled"

    return cast


def spell_sequence(spells: list[callable]) -> callable:

    random_target: str = random.choice([
        "Dragon",
        "Unicorn",
        "Goblin",
        "Kraken",
        "Fairy"
    ])

    def cast_all() -> list[str]:
        return [
            spell(random_target) for spell in spells
        ]

    return cast_all


def fireball(target: str) -> str:
    return f"Fireball hits {target}"


def healing_spell(target: str) -> str:
    return f"Heals {target}"


def lightning_bolt(target: str) -> str:
    return f"Strikes {target}"


def attack_booster(target: str) -> str:
    return f"Boosts {target}'s attack power"


def base_spell() -> int:
    return 42


def condition(target: str) -> bool:

    if target in ["Fairy", "Unicorn"]:
        return False
    return True


def test_combiner(spells: list[callable]) -> None:

    spell1: callable = random.choice(spells)
    spell2: callable = random.choice(spells)

    print("\n==== Testing spell combiner ====")
    combined: callable = spell_combiner(spell1, spell2)

    print(f"Combined spell result: {combined()[0]}, {combined()[1]}\n")


def test_amplifier() -> None:

    print("\n==== Testing power amplifier ====")
    print(
        f"Original: {base_spell()} "
        f"- Amplified: {power_amplifier(base_spell, random.randint(1, 5))()}\n"
    )


def test_condition(spells: list[callable]) -> None:

    spell_chosen: callable = random.choice(spells)

    print("\n==== Testing conditional cast ====")
    print(f"Cast result: {conditional_caster(condition, spell_chosen)()}\n")


def test_sequence(spells: list[callable]) -> None:

    print("\n==== Testing spell sequence ====")

    for result in spell_sequence(spells)():
        print(f"Result: {result}")

    print("")


def main() -> None:

    spells: list[callable] = [fireball, healing_spell, lightning_bolt, attack_booster]

    test_combiner(spells)

    test_amplifier()

    test_condition(spells)

    test_sequence(spells)


if __name__ == "__main__":
    main()
