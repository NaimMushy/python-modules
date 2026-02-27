from typing import Callable as callable
from typing import Any as any
import random


def mage_counter() -> callable:

    counter: int = 0

    def increase_counter() -> int:

        nonlocal counter
        counter += 1

        return counter

    return increase_counter


def spell_accumulator(initial_power: int) -> callable:

    accumulated_power: int = initial_power

    def accumulate(amount: int) -> int:

        nonlocal accumulated_power
        accumulated_power += amount

        return accumulated_power

    return accumulate


def enchantment_factory(enchantment_type: str) -> callable:

    def apply_enchantment(item_name: str) -> str:

        return f"{enchantment_type} {item_name}"

    return apply_enchantment


def memory_vault() -> dict[str, callable]:

    storage: dict = {}

    def store(key: any, value: any) -> None:

        storage[key] = value

    def recall(key: any) -> any:

        return (
            "Memory not found"
            if key not in storage.keys()
            else storage[key]
        )

    return {"store": store, "recall": recall}


def test_counter() -> None:

    print("\n==== Testing mage counter ====\n")

    counter: callable = mage_counter()

    for call in range(random.randint(3, 10)):
        print(f"Call {call + 1}: {counter()}")

    print("")


def test_accumulator() -> None:

    print("\n==== Testing power accumulator ====\n")

    accumulator: callable = spell_accumulator(random.randint(1, 20))

    for _ in range(random.randint(1, 10)):
        print(f"Accumulated power: {accumulator(random.randint(1, 20))}")

    print("")


def test_factory() -> None:

    enchantments: list[str] = [
        "Flaming",
        "Cursed",
        "Blessed",
        "Frozen",
        "Healing",
        "Booster",
        "Weakening",
        "Lightning",
        "Poison",
        "Shadow"
    ]

    items: list[str] = [
        "Sword",
        "Shield",
        "Potion",
        "Ring",
        "Spear",
        "Helmet",
        "Belt",
        "Necklace",
        "Boots",
        "Earring"
    ]

    print("\n==== Testing enchantment factory ====")

    for _ in range(random.randint(1, len(enchantments))):

        enchantment_chosen: str = random.choice(enchantments)

        print(f"\nFactory enchantment type: < {enchantment_chosen} >")

        factory: callable = enchantment_factory(enchantment_chosen)

        for _ in range(random.randint(1, len(items))):
            print(f"Enchanted item: {factory(random.choice(items))}")

    print("")


def test_memory_vault() -> None:

    example_dict: dict[str, str | int] = {
        "world_war_II": "1939-1945",
        "world_war_I": "1914-1918",
        "french_revolution": 1789,
        "youth_revolt": "May 68",
        "bolchevik_revolution": 1917,
        "covid19": 2020
    }

    print("\n==== Testing memory vault system ====\n")

    vault: dict[str, callable] = memory_vault()

    print("[STORING MEMORIES]\n")

    for key, val in example_dict.items():

        vault["store"](key, val)
        print(f"{key} memory stored: {val}")

    print("")

    example_dict["vox_machina_season3"] = 2026

    print("[RECALLING MEMORIES]\n")

    for to_recall in example_dict.keys():

        print(f"{to_recall}: {vault['recall'](to_recall)}")

    print("")


def main() -> None:

    for test in [
        test_counter,
        test_accumulator,
        test_factory,
        test_memory_vault
    ]:
        test()


if __name__ == "__main__":

    main()
