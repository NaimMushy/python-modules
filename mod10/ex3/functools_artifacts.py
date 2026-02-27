import operator
import functools
import random
from typing import Callable as callable


def spell_reducer(spells: list[int], operation: str) -> int:

    match operation:

        case "add":
            operator_func: callable = operator.add

        case "multiply":
            operator_func = operator.mul

        case "max":
            operator_func = max

        case "min":
            operator_func = min

    return functools.reduce(lambda x, y: operator_func(x, y), spells)


def partial_enchanter(base_enchantment: callable) -> dict[str, callable]:

    elements: list[str] = [
        "fire",
        "ice",
        "water",
        "earth",
        "air",
        "light",
        "shadow",
        "poison",
        "lightning"
    ]

    enchanted: dict[str, callable] = {}

    for _ in range(random.randint(1, 10)):

        element_chosen: str = random.choice(elements)
        enchanted[element_chosen+"_enchant"] = functools.partial(
            base_enchantment,
            50,
            element_chosen
        )

    return enchanted


@functools.lru_cache
def memoized_fibonacci(n: int) -> int:

    return (
        n if n < 2 else
        memoized_fibonacci(n - 1) + memoized_fibonacci(n - 2)
    )


@functools.singledispatch
def spell_dispatcher(value: int | str | list[str | int]) -> callable:

    return spell_dispatcher(value)


@spell_dispatcher.register(int)
def _(value: int) -> None:

    print(f"Damage spell: Deals {value} damage to target")


@spell_dispatcher.register(str)
def _(value: str) -> None:

    print(f"Enchanted spell: {value}")


@spell_dispatcher.register(list)
def _(values: list[str | int]) -> None:

    print(f"Casting multiple spells ({len(values)}):\n")

    for value in values:
        spell_dispatcher(value)


def test_reducer() -> None:

    spells: list[int] = [
        random.randint(1, 20) for _ in range(random.randint(1, 10))
    ]

    print("\n==== Testing spell reducer ====\n")

    print(f"Sum: {spell_reducer(spells, 'add')}")
    print(f"Product: {spell_reducer(spells, 'multiply')}")
    print(f"Max: {spell_reducer(spells, 'max')}")
    print(f"Min: {spell_reducer(spells, 'min')}")

    print("")


def base_enchantment(power: int, element: str, target: str) -> None:

    print(
        f"{element.capitalize()} enchantment deals "
        f"{power} damage to {target}"
    )


def test_enchanter() -> None:

    print("\n==== Testing partial enchanter ====\n")

    enchanted: dict[str, callable] = partial_enchanter(base_enchantment)

    possible_targets: list[str] = [
        "Dragon",
        "Unicorn",
        "Giant",
        "Acromentula",
        "Selkie",
        "Kraken",
        "Goblin",
        "Fairy"
    ]

    for enchant, specialized in enchanted.items():

        print(f"{enchant}: ", end="")
        specialized(random.choice(possible_targets))

    print("")


def test_mem_fibonacci() -> None:

    print("\n==== Testing memoized fibonacci ====\n")

    for _ in range(random.randint(1, 10)):

        nth_nb: int = random.randint(1, 10)
        print(f"{nth_nb}th fibonacci number: {memoized_fibonacci(nth_nb)}")

    print("")


def test_dispatcher() -> None:

    enchantments: list[str] = [
        "Fireball",
        "Lightning Bolt",
        "Poison Cloud",
        "Shadow Ray",
        "Wind Tornado",
        "Water Tsunami",
        "Ice Cage"
    ]

    damage_spell: int = random.randint(1, 20)

    enchantment_spell: str = random.choice(enchantments)

    multi_casting: list[str | int] = []

    for _ in range(random.randint(1, 10)):

        multi_casting.append(random.choice(
            (random.choice(enchantments), random.randint(1, 20))
        ))

    print("\n==== Testing spell dispatcher ====\n")

    for _ in range(random.randint(1, 10)):

        spell_dispatcher(random.choice((
            damage_spell,
            enchantment_spell,
            multi_casting
        )))

        print("")


def main() -> None:

    for test in [
        test_reducer,
        test_enchanter,
        test_mem_fibonacci,
        test_dispatcher
    ]:
        test()


if __name__ == "__main__":

    main()
