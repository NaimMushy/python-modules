import random


def artifact_sorter(artifacts: list[dict]) -> list[dict]:

    return sorted(
        artifacts,
        key=lambda artifact: artifact["power"], reverse=True
    )


def power_filter(mages: list[dict], min_power: int) -> list[dict]:

    return list(filter(lambda mage: mage["power"] >= min_power, mages))


def spell_transformer(spells: list[str]) -> list[str]:

    return list(map(lambda spell: "* " + spell + " *", spells))


def mage_stats(mages: list[dict]) -> dict:

    return {
        "max_power": max(mages, key=lambda mage: mage["power"])["power"],
        "min_power": min(mages, key=lambda mage: mage["power"])["power"],
        "avg_power": round(
            sum(mage["power"] for mage in mages) / len(mages),
            2
        )
    }


def test_artifact_sorter(artifacts: list[dict]) -> None:

    print("\n==== Testing artifact sorter ====\n")

    artifacts = artifact_sorter(artifacts)

    rand: int = random.randint(0, len(artifacts) - 2)

    print(
        f"{artifacts[rand]['name']} ({artifacts[rand]['power']} power) "
        f"comes before {artifacts[rand + 1]['name']} "
        f"({artifacts[rand + 1]['power']} power)\n"
    )


def test_spell_transformer() -> None:

    names: list[str] = [
        "Fire Ball",
        "Lightning Bolt",
        "Shadow Ray",
        "Healing Fountain",
        "Ice Cage",
        "Water Tornado"
    ]
    spells: list[str] = []

    for _ in range(10):
        spells.append(random.choice(names))

    spells = spell_transformer(spells)

    print("\n==== Testing spell transformer ====\n")

    for spell in spells:
        print(spell)

    print("")


def test_filter_mages(
    mages: list[dict],
    min_power: int = random.randint(15, 40)
) -> None:

    print("\n==== Testing mage filtering ====\n")

    for loop in range(2):

        print(
            ("Mages before power filtering:\n")
            if loop == 0
            else (
                "\nMages after power filtering with "
                f"{min_power} minimum power:\n"
            )
        )

        for mage in mages:
            print(f"- {mage['name']}: {mage['power']} power")

        mages = power_filter(mages, min_power)

    print("")


def get_mage_stats(mages: list[dict]) -> None:

    print("\n==== Displaying mage power stats ====\n")

    stats = mage_stats(mages)

    print(f"Maximum power: {stats['max_power']}")
    print(f"Minimum power: {stats['min_power']}")
    print(f"Average power: {stats['avg_power']:.2f}\n")


def main() -> None:

    prefixes: list[str] = [
        "Cursed", "Healing", "Blessed", "Weakening", "Strengthening"
    ]
    art_names: list[str] = [
        "Ring", "Crown", "Sword", "Belt", "Necklace", "Jewel", "Staff"
    ]
    types: list[str] = ["Damage", "Heal", "Buff", "Debuff"]

    artifacts: list[dict] = []

    for _ in range(10):

        artifacts.append({
            "name": random.choice(prefixes) + " " + random.choice(art_names),
            "power": random.randint(30, 100),
            "type": random.choice(types)
        })

    mage_names: list[str] = [
        "Wizard", "Sorcerer", "Mage", "Witch", "Sorceress"
    ]
    elements: list[str] = [
        "Fire", "Water", "Ice", "Shadow", "Lightning", "Poison"
    ]

    mages: list[dict] = []

    for mage in range(10):

        mages.append({
            "name": random.choice(mage_names) + str(mage + 1),
            "power": random.randint(5, 50),
            "element": random.choice(elements)
        })

    test_artifact_sorter(artifacts)

    test_filter_mages(mages)

    test_spell_transformer()

    get_mage_stats(mages)


if __name__ == "__main__":

    main()
