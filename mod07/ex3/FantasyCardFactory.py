from ex0.Card import Card
from ex0.CreatureCard import CreatureCard
from ex1.SpellCard import SpellCard
from ex1.ArtifactCard import ArtifactCard
from .CardFactory import CardFactory
import random


# creature cards
CREATURES: dict[str, list[str]] = {
    "leg_cards": ["Dragon", "Phoenix", "Elemental Spirit", "Kraken"],
    "srare_cards": ["Unicorn", "Fairy", "Selkie", "Animal Sovereign"],
    "rare_cards": ["Ogre", "Acromentula", "Shapeshifter", "Malicious Spirit"],
    "common_cards": ["Goblin", "Wolf", "Spider", "Zombie"],
    "leg_attr": [
        "Fire ",
        "Ice ",
        "Wind ",
        "Lightning ",
        "Poison ",
        "Acid ",
        "Shadow "
    ],
    "srare_attr": ["Sacred ", "Mighty ", "Superb ", "Arcane "],
    "rare_attr": ["Imposing ", "Stealthy ", "Agile ", "Genius "],
    "common_attr": ["Warrior ", "Resilient ", "Bloodthirsty ", "Scary "]
}

# spells
SPELLS: dict[str, list[str]] = {
    "offensive_cards": ["Bolt", "Ray", "Ball", "Tornado", "Gun"],
    "healing_cards": ["Balm", "Fountain", "SoothingHug", "Charm"],
    "support_cards": ["Enhancer", "Diminisher"]
}

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
        self.creatures: dict[str, list[str]] = CREATURES
        self.spells: dict[str, list[str]] = SPELLS
        self.artifacts: list[list[str | int]] = ARTIFACTS
        self.elites: list[list[str | int]] = ELITES

        self.leg_attr: dict[str, int] = {
            "effect": 13,
            "cost": 11,
            "health": 26,
            "attack": 16,
            "durability": 8
        }
        self.srare_attr: dict[str, int] = {
            "effect": 11,
            "cost": 9,
            "health": 21,
            "attack": 11,
            "durability": 6
        }
        self.rare_attr: dict[str, int] = {
            "effect": 9,
            "cost": 7,
            "health": 16,
            "attack": 9,
            "durability": 4
        }
        self.common_attr: dict[str, int] = {
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
        card_category: str = ""
    ) -> tuple[str, tuple[str, str]]:
        probability: float = random.random()
        if probability < 0.05 or "leg" in card_category:
            return "Legendary", ["leg_attr", "leg_cards"]
        if 0.1 <= probability < 0.2 or "srare" in card_category:
            return "Super Rare", ["srare_attr", "srare_cards"]
        if 0.2 <= probability < 0.5 or "rare" in card_category:
            return "Rare", ["rare_attr", "rare_cards"]
        if 0.5 <= probability <= 1 or "common" in card_category:
            return "Common", ["common_attr", "common_cards"]
        return "Unknown"

    def generate_creature_data(
        self,
        card_category: str = ""
    ) -> list[str | int]:
        rarity, rarity_keys = self.generate_rarity(card_category)
        name: str = random.choice(
            self.creatures[rarity_keys[0]]
        ) + random.choice(
            self.creatures[rarity_keys[1]]
        )
        cost, attack, health = (
            self.rarity_keys[0]["cost"],
            self.rarity_keys[0]["attack"],
            self.rarity_keys[0]["health"]
        )
        return [name, cost, rarity, attack, health]

    def generate_spell(self) -> list[str | int]:
        rarity, rarity_keys = self.generate_rarity()
        effect_val: int = random.randint(
            self.rarity_keys[0]["effect"] - 4,
            self.rarity_keys[0]["effect"]
        )
        cost: int = random.randint(
            self.rarity_keys[0]["cost"] - 4,
            self.rarity_keys[0]["cost"]
        )
        effect_type: list[str] = random.choice(
            ["offensive", self.get_element(), f"Deals {effect_val} to target"],
            ["healing", "Healing ", f"Restores {effect_val}"],
            ["support", "Attack ", f" {effect_val} to target"]
        )
        name: str = effect_type[1] + random.choice(
            self.spells[effect_type[0] + "_cards"]
        )
        if effect_type == "support":
            effect: str = (
                'Adds' if "Enhancer" in name else 'Removes'
            ) + effect_type[2]
        else:
            effect = effect_type[2]
        return [name, cost, rarity, effect]

    def create_creature(self, name_or_power: str | int | None = None) -> Card:
        if not name_or_power:
            name, cost, rarity, attack, health = self.generate_creature_data()
            return CreatureCard(name, cost, rarity, attack, health)
        if isinstance(name_or_power, str):
            card_category: str = (
                cards for cards in self.creatures.keys()
                for card in cards
                if card in name_or_power
            )
            name, cost, rarity, attack, health = self.generate_creature_data(
                card_category
            )
            return CreatureCard(name_or_power, cost, rarity, attack, health)
        if isinstance(name_or_power, int):
            card_category = (
                category for category in ["leg", "srare", "rare", "common"]
                if self.categories+"_attr"["attack"] - 4
                <= name_or_power < self.categories+"_attr"["attack"]
            )
            name, cost, rarity, attack, health = self.generate_creature_data(
                card_category
            )
            return CreatureCard(name, cost, rarity, name_or_power, health)
