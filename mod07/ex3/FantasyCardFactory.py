from .CardFactory import CardFactory
import random


# creature cards
CREATURES: list[list[str | int]] = [
    [
        "Dragon",
        5,
        "Legendary",
        7,
        6
    ],
    [
        "Goblin",
        3,
        "Rare",
        5,
        3
    ],
    [
        "Acromentula",
        4,
        "Common",
        4,
        2
    ],
    [
        "Unicorn",
        7,
        "Legendary",
        8,
        10
    ]
]


# artifact cards
ARTIFACTS: list[list[str | int]] = [
    [
        "Mana Crystal",
        2,
        "Rare",
        3,
        "Permanent: +1 mana per turn"
    ],
    [
        "Mana Penalizer",
        2,
        "Rare",
        1,
        "Permanent: +1 mana cost"
    ],
    [
        "Mana Lightener",
        2,
        "Rare",
        1,
        "Permanent: -1 mana cost"
    ],
    [
        "Heal Potion",
        4,
        "Rare",
        3,
        "Permanent: +2 health"
    ],
    [
        "Atomic Laser",
        7,
        "Legendary",
        5,
        "Permanent: -2 health"
    ],
    [
        "Power Ring",
        3,
        "Common",
        2,
        "Permanent: +1 attack"
    ],
    [
        "Weakness Belt",
        3,
        "Common",
        2,
        "Permanent: -1 attack"
    ]
]


# elite cards
ELITES: list[list[str | int | list]] = [
    [
        "Dark Sorcerer",
        3,
        "Super Rare",
        5,
        2,
        20,
        10,
        "long-range",
        [lightning_spell, fire_spell]
    ],
    [
        "Divine Healer",
        2,
        "Legendary",
        1,
        4,
        20,
        15,
        "long-range",
        [healing_spell, super_healing_spell]
    ],
    [
        "Acrobatic Monk",
        3,
        "Super Rare",
        8,
        6,
        10,
        15,
        "melee",
        [attack_buff_spell, attack_debuff_spell]
    ],
    [
        "Forest Elf",
        3,
        "Super Rare",
        4,
        5,
        18,
        12,
        "versatile",
        [lightning_spell, healing_spell, attack_buff_spell]
    ]
]


class FantasyCardFactory(CardFactory):
    def __init__(self) -> None:
        self.creatures: list[list[str | int]] = CREATURES
        self.spells: list[list[str | int]] = SPELLS
        self.artifacts: list[list[str | int]] = ARTIFACTS
        self.elites: list[list[str | int | list[str]]] = ELITES

    def generate_rarity(self) -> str:
        probability: float = random.random()
        if probability < 0.05:
            return "Legendary"
        if 0.1 <= probability < 0.2:
            return "Super Rare"
        if 0.2 <= probability < 0.5:
            return "Rare"
        if 0.5 <= probability <= 1:
            return "Common"
        return "Unknown"

    def generate_spell(self) -> tuple[str, str]:
        rarity: str = self.generate_rarity()
        match rarity:
            case "Legendary":
                effect_val: int = random.randint(7, 11)
                cost: int = random.randint(6, 10)
            case "Super Rare":
                effect_val = random.randint(5, 8)
                cost = random.randint(5, 8)
            case "Rare":
                effect_val = random.randint(3, 6)
                cost = random.randint(3, 6)
            case "Common":
                effect_val = random.randint(1, 4)
                cost = random.randint(1, 4)
        effect_type: str = random.choice("offensive", "healing", "support")
        match effect_type:
            case "offensive":
                name: str = random.choice(
                    ["Fire ", "Ice ", "Lightning ", "Poison ", "Acid "]
                ) + random.choice(
                    ["Bolt", "Ray", "Ball", "Tornado", "Gun"]
                )
                effect: str = f"Deals {effect_val} to target"
            case "healing":
                name = "Healing " + random.choice(
                    ["Balm", "Fountain", "SoothingHug", "Charm"]
                )
                effect = f"Restores {effect_val}"
            case "support":
                name = "Attack " + random.choice(["Enhancer", "Diminisher"])
                effect = (
                    f"{'Adds' if 'Enhancer' in name else 'Removes'} "
                    f"{effect_val} to target"
                )
        return [name, cost, rarity, effect]

    def create_creature(self, name_or_power: str | int | None = None) -> Card:
        if not name_or_power:
            name, cost, rarity, attack, health = random.choice(self.creatures)
            return CreatureCard(name, cost, rarity, attack, health)
        if isinstance(name_or_power, str):
            return CreatureCard(
                name_or_power,
                random.randint(1, 11),
                self.get_rarity(),
                random.randint(1, 16),
                random.randint(1, 21),
            )
        if isinstance(name_or_power, int):
            return CreatureCard(

                    )
