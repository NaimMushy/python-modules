from ex0.Card import Card
from ex0.CreatureCard import CreatureCard
from ex1.SpellCard import SpellCard
# from ex1.ArtifactCard import ArtifactCard
from .CardFactory import CardFactory
import random


# creature cards
CREATURES: dict[str, list[str]] = {
    "leg_cards": ["Dragon", "Phoenix", "Elemental Spirit", "Kraken"],
    "srare_cards": ["Unicorn", "Fairy", "Selkie", "Animal Sovereign"],
    "rare_cards": ["Ogre", "Acromentula", "Shapeshifter", "Malicious Spirit"],
    "common_cards": ["Goblin", "Wolf", "Spider", "Zombie"],
    "leg_adjs": [
        "Fire ",
        "Ice ",
        "Wind ",
        "Lightning ",
        "Poison ",
        "Acid ",
        "Shadow "
    ],
    "srare_adjs": ["Sacred ", "Mighty ", "Superb ", "Arcane "],
    "rare_adjs": ["Imposing ", "Stealthy ", "Agile ", "Genius "],
    "common_adjs": ["Warrior ", "Resilient ", "Bloodthirsty ", "Scary "]
}

# spells
SPELLS: dict[str, list[str]] = {
    "offensive_cards": ["Bolt", "Ray", "Ball", "Tornado", "Gun"],
    "healing_cards": ["Balm", "Fountain", "SoothingHug", "Charm"],
    "support_cards": ["Enhancer", "Diminisher"]
}

"""
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
"""


class FantasyCardFactory(CardFactory):
    def __init__(self) -> None:
        self.creatures: dict[str, list[str]] = CREATURES
        self.spells: dict[str, list[str]] = SPELLS
        # self.artifacts: list[list[str | int]] = ARTIFACTS
        # self.elites: list[list[str | int]] = ELITES

        self.leg_attr: dict[str, int | str] = {
            "type": "leg",
            "effect": 13,
            "cost": 11,
            "health": 26,
            "attack": 16,
            "durability": 8
        }
        self.srare_attr: dict[str, int | str] = {
            "type": "srare",
            "effect": 11,
            "cost": 9,
            "health": 21,
            "attack": 11,
            "durability": 6
        }
        self.rare_attr: dict[str, int | str] = {
            "type": "rare",
            "effect": 9,
            "cost": 7,
            "health": 16,
            "attack": 9,
            "durability": 4
        }
        self.common_attr: dict[str, int | str] = {
            "type": "common",
            "effect": 7,
            "cost": 5,
            "health": 11,
            "attack": 7,
            "durability": 2
        }

    def get_element(self) -> str:
        return random.choice([
            "Fire ",
            "Ice ",
            "Wind ",
            "Lightning ",
            "Poison ",
            "Acid ",
            "Shadow "
        ])

    def generate_rarity(
        self,
        rarity: str
    ) -> dict[str, str | dict[str, int | str]]:
        probability: float = random.random()
        if probability < 0.05 or "leg" in rarity:
            return {
                "rarity": "Legendary",
                "cards": "leg_cards",
                "adjs": "leg_adjs",
                "attr": self.leg_attr
            }
        if 0.1 <= probability < 0.2 or "srare" in rarity:
            return {
                "rarity": "Super Rare",
                "cards": "srare_cards",
                "adjs": "srare_adjs",
                "attr": self.srare_attr
            }
        if 0.2 <= probability < 0.5 or "rare" in rarity:
            return {
                "rarity": "Rare",
                "cards": "rare_cards",
                "adjs": "rare_adjs",
                "attr": self.rare_attr
            }
        return {
            "rarity": "Common",
            "cards": "common_cards",
            "adjs": "common_adjs",
            "attr": self.common_attr
        }

    def generate_creature_data(
        self,
        rarity: str = ""
    ) -> list[str | int]:
        card_data = self.generate_rarity(rarity)
        name: str = random.choice(
            self.creatures[card_data["adjs"]]
        ) + random.choice(
            self.creatures[card_data["cards"]]
        )
        cost: int = random.randint(
            card_data["attr"]["cost"] - 4,
            card_data["attr"]["cost"]
        )
        attack: int = random.randint(
            card_data["attr"]["attack"] - 4,
            card_data["attr"]["attack"]
        )
        health: int = random.randint(
            card_data["attr"]["health"] - 4,
            card_data["attr"]["health"]
        )
        return [name, cost, card_data["rarity"], attack, health]

    def generate_spell_data(self, card_rarity: str = "") -> list[str | int]:
        card_data = self.generate_rarity(card_rarity)
        effect_val: int = random.randint(
            card_data["attr"]["effect"] - 4,
            card_data["attr"]["effect"]
        )
        cost: int = random.randint(
            card_data["attr"]["cost"] - 4,
            card_data["attr"]["cost"]
        )
        effect_type: list[str] = random.choice([
            ["offensive", self.get_element(), f"Deals {effect_val} damage to target"],
            ["healing", "Healing ", f"Restores {effect_val} health to target"],
            ["support", "Attack ", f" {effect_val} attack to target"]
        ])
        name: str = effect_type[1] + random.choice(
            self.spells[effect_type[0] + "_cards"]
        )
        if effect_type[0] == "support":
            effect: str = (
                "Adds" if "Enhancer" in name else "Removes"
                + effect_type[2]
            )
        else:
            effect = effect_type[2]
        return [name, cost, card_data["rarity"], effect]

    def create_creature(self, name_or_power: str | int | None = None) -> Card:
        name: str
        cost: int
        rarity: str
        attack: int
        health: int
        if not name_or_power:
            name, cost, rarity, attack, health = self.generate_creature_data()
            return CreatureCard(name, cost, rarity, attack, health)
        if isinstance(name_or_power, str):
            cards: list[str] = [
                key for key in self.creatures.keys()
                if "cards" in key
            ]
            for card_type in cards:
                for name in self.creatures[card_type]:
                    if name in name_or_power:
                        card_rarity: str = card_type
            name, cost, rarity, attack, health = self.generate_creature_data(
                card_rarity
            )
            return CreatureCard(name_or_power, cost, rarity, attack, health)
        if isinstance(name_or_power, int):
            categories: list[dict[str, int | str]] = [
                self.leg_attr,
                self.srare_attr,
                self.rare_attr,
                self.common_attr
            ]
            for category in categories:
                if (
                    category["attack"] - 4 <=
                    name_or_power <
                    category["attack"]
                ):
                    card_rarity = category["type"]
            name, cost, rarity, attack, health = self.generate_creature_data(
                card_rarity
            )
            return CreatureCard(name, cost, rarity, name_or_power, health)

    def create_spell(self, name_or_power: str | int | None = None) -> Card:
        name: str
        cost: int
        rarity: str
        effect: str
        name, cost, rarity, effect = self.generate_spell_data()
        if isinstance(name_or_power, str):
            name = name_or_power
        elif isinstance(name_or_power, int):
            split_effect: list[str] = effect.split(" ", )
            split_effect[1] = str(name_or_power)
            effect = " ".join(split_effect)
        return SpellCard(name, cost, rarity, effect)


def test_factory() -> None:
    factory: FantasyCardFactory = FantasyCardFactory()
    for i in range(5):
        print(factory.create_creature().get_card_info())
        print(factory.create_spell().get_card_info())


if __name__ == "__main__":
    test_factory()
