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

    return lambda: (spell1(random_target), spell2(random_target))


def power_amplifier(base_spell: callable, multiplier: int) -> callable:

    return lambda: base_spell() * multiplier


def conditional_caster(condition: callable, spell: callable) -> callable:

    random_target: str = random.choice([
        "Dragon",
        "Unicorn",
        "Goblin",
        "Kraken",
        "Fairy"
    ])

    return lambda: (
        spell(random_target) if condition(random_target)
        else "Spell fizzled"
    )


def spell_sequence(spells: list[callable]) -> callable:

    random_target: str = random.choice([
        "Dragon",
        "Unicorn",
        "Goblin",
        "Kraken",
        "Fairy"
    ])

    return lambda: [
        spell(random_target) for spell in spells
    ]


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

    return False if target in ["Fairy", "Unicorn"] else True


def test_combiner(spells: list[callable]) -> None:

    spell1: callable = random.choice(spells)
    spell2: callable = random.choice(spells)

    print("\n==== Testing spell combiner ====\n")

    combined: callable = spell_combiner(spell1, spell2)

    print(f"Combined spell result: {combined()[0]}, {combined()[1]}\n")


def test_amplifier() -> None:

    print("\n==== Testing power amplifier ====\n")

    print(
        f"Original: {base_spell()} "
        f"- Amplified: {power_amplifier(base_spell, random.randint(2, 5))()}\n"
    )


def test_condition(spells: list[callable]) -> None:

    spell_chosen: callable = random.choice(spells)

    print("\n==== Testing conditional cast ====\n")

    print(f"Cast result: {conditional_caster(condition, spell_chosen)()}\n")


def test_sequence(spells: list[callable]) -> None:

    print("\n==== Testing spell sequence ====\n")

    for result in spell_sequence(spells)():
        print(f"Result: {result}")

    print("")


def main() -> None:

    spells: list[callable] = [
        fireball, healing_spell, lightning_bolt, attack_booster
    ]

    test_combiner(spells)

    test_amplifier()

    test_condition(spells)

    test_sequence(spells)


if __name__ == "__main__":

    main()
