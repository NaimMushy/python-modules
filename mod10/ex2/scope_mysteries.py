from typing import Callable as callable
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
        nonlocal enchantment_type
        return f"{enchantment_type} {item_name}"

    return apply_enchantment


def memory_vault() -> dict[str, callable]:

    storage: dict = {}

    def store(key: any, value: any) -> None:
        nonlocal storage
        storage[key] = value

    def recall(key: any) -> any:
        nonlocal storage
        if key not in storage.keys():
            return "Memory not found"
        return storage[key]

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

    keys: list[str] = [
        "worldwarII",
        "worldwarI",
        "frenchrevolution",
        "youthrevolt",
        "bolchevikrevolution",
        "covid19"
    ]

    values: list[str, int] = [
        "1939-1945",
        "1914-1918",
        1789,
        "May 68",
        1917,
        2020
    ]

    print("\n==== Testing memory vault system ====\n")

    vault: dict[str, callable] = memory_vault()

    print("[STORING MEMORIES]\n")

    for to_store in range(len(keys)):
        vault["store"](keys[to_store], values[to_store])
        print(f"{keys[to_store]} memory stored: {values[to_store]}")

    print("")

    keys.append("voxmachinaseason4")

    print("[RECALLING MEMORIES]\n")

    for to_recall in keys:
        print(f"{to_recall}: {vault['recall'](to_recall)}")

    print("")


def main() -> None:

    for test in [test_counter, test_accumulator, test_factory, test_memory_vault]:
        test()


if __name__ == "__main__":
    main()
