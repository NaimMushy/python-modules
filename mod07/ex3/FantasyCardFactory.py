from ex0.Card import Card
from ex0.CreatureCard import CreatureCard
from ex1.SpellCard import SpellCard
from ex1.ArtifactCard import ArtifactCard
from .CardFactory import CardFactory
import random
import sys


# creature cards
CREATURES: dict[str, list[str]] = {
    "leg_cards": ["Dragon", "Phoenix", "Elemental Spirit", "Kraken"],
    "srare_cards": ["Unicorn", "Fairy", "Selkie", "Animal Sovereign"],
    "orare_cards": ["Ogre", "Acromentula", "Shapeshifter", "Malicious Spirit"],
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
    "orare_adjs": ["Imposing ", "Stealthy ", "Agile ", "Genius "],
    "common_adjs": ["Warrior ", "Resilient ", "Bloodthirsty ", "Scary "]
}

# spells
SPELLS: dict[str, dict[str, list[str] | str]] = {
    "offensive_cards": {
        "card_names": ["Bolt", "Ray", "Ball", "Tornado", "Gun"],
        "effect_prefix": "Deals ",
        "effect_suffix": " damage"
    },
    "healing_cards": {
        "card_names": ["Balm", "Fountain", "Hug", "Charm"],
        "name_prefix": "Healing ",
        "effect_prefix": "Restores ",
        "effect_suffix": " health"
    },
    "support_cards": {
        "card_names": ["Enhancer", "Diminisher"],
        "name_prefix": "Mana ",
        "effect_suffix": " mana"
    }
}

# artifact cards
ARTIFACTS: dict[str, list[str] | dict[str, list[str]]] = {
    "objects": ["Staff", "Ring", "Belt", "Crystal", "Potion", "Watch", "Earring", "Dagger"],
    "adjs_plus": {
        "mana": ["Mana Lightener", "Mana Burden"],
        "attack": ["Power", "Atomic", "Strength", "Enchanted"],
        "health": ["Heal", "Soothing", "Blessed"]
    },
    "adjs_minus": {
        "mana": ["Mana Diminisher", "Mana Booster"],
        "attack": ["Weakness", "Diminisher", "Debuff"],
        "health": ["Cursed", "Poisoning", "Bloodthirsty"]
    }
}
"""
    "mana_artifacts": 
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
        self.artifacts: dict[str, list[str] | dict[str, list[str]]] = ARTIFACTS
        # self.elites: list[list[str | int]] = ELITES

        self.cost_range: int = 3
        self.effect_range: int = 3
        self.attack_range: int = 5
        self.health_range: int = 5
        self.durab_range: int = 2

        self.common_attr: dict[str, tuple[int, int] | str] = {
            "type": "common",
            "effect": (1, self.effect_range + 1),
            "cost": (1, self.cost_range + 1),
            "attack": (1, self.attack_range + 1),
            "health": (1, self.health_range * 2 + 1),
            "durability": (1, self.durab_range + 1)
        }
        self.orare_attr: dict[str, tuple[int, int] | str] = {
            "type": "rare",
            "effect": (self.effect_range, self.effect_range * 2 + 1),
            "cost": (self.cost_range, self.cost_range * 2 + 1),
            "attack": (self.attack_range, self.attack_range * 2 + 1),
            "health": (self.health_range * 2, self.health_range * 3 + 1),
            "durability": (self.durab_range, self.durab_range * 2 + 1)
        }
        self.srare_attr: dict[str, tuple[int, int] | str] = {
            "type": "srare",
            "effect": (self.effect_range * 2, self.effect_range * 3 + 1),
            "cost": (self.cost_range * 2, self.cost_range * 3 + 1),
            "attack": (self.attack_range * 2, self.attack_range * 3 + 1),
            "health": (self.health_range * 3, self.health_range * 4 + 1),
            "durability": (self.durab_range * 2, self.durab_range * 3 + 1)
        }
        self.leg_attr: dict[str, tuple[int, int] | str] = {
            "type": "leg",
            "effect": (self.effect_range * 3, self.effect_range * 4 + 1),
            "cost": (self.cost_range * 3, self.cost_range * 4 + 1),
            "attack": (self.attack_range * 3, self.attack_range * 4 + 1),
            "health": (self.health_range * 4, self.health_range * 5 + 1),
            "durability": (self.durab_range * 3, self.durab_range * 4 + 1)
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
        card_category: str
    ) -> dict[str, str | dict[str, tuple[int, int] | str]]:
        probability: float = random.random()
        if probability < 0.05 or "leg" in card_category:
            return {
                "rarity": "Legendary",
                "cards": "leg_cards",
                "adjs": "leg_adjs",
                "attr": self.leg_attr
            }
        if 0.1 <= probability < 0.2 or "srare" in card_category:
            return {
                "rarity": "Super Rare",
                "cards": "srare_cards",
                "adjs": "srare_adjs",
                "attr": self.srare_attr
            }
        if 0.2 <= probability < 0.5 or "orare" in card_category:
            return {
                "rarity": "Rare",
                "cards": "orare_cards",
                "adjs": "orare_adjs",
                "attr": self.orare_attr
            }
        return {
            "rarity": "Common",
            "cards": "common_cards",
            "adjs": "common_adjs",
            "attr": self.common_attr
        }

    def generate_creature_data(
        self,
        name: str = "",
        power: int = 0,
        card_category: str = ""
    ) -> list[str | int]:
        card_data = self.generate_rarity(card_category)
        if not name:
            name = random.choice(self.creatures[card_data["cards"]])
        name = random.choice(
            self.creatures[card_data["adjs"]]
        ) + name
        cost: int = random.randint(
            card_data["attr"]["cost"][0],
            card_data["attr"]["cost"][1]
        )
        if not power:
            power = random.randint(
                card_data["attr"]["attack"][0],
                card_data["attr"]["attack"][1]
            )
        health: int = random.randint(
            card_data["attr"]["health"][0],
            card_data["attr"]["health"][1]
        )
        return [name, cost, card_data["rarity"], power, health]

    def generate_spell_data(
        self,
        name: str = "",
        power: int = 0,
        card_category: str = ""
    ) -> list[str | int]:
        card_data = self.generate_rarity(card_category)
        if not power:
            power = random.randint(
                card_data["attr"]["effect"][0],
                card_data["attr"]["effect"][1]
            )
        cost: int = random.randint(
            card_data["attr"]["cost"][0],
            card_data["attr"]["cost"][1]
        )
        effect_type: str = card_category
        if not effect_type:
            effect_type = random.choice([cat for cat in self.spells.keys()])
        if not name:
            name = random.choice(self.spells[effect_type]["card_names"])
        if effect_type != "offensive_cards":
            name = self.spells[effect_type]["name_prefix"] + name
        else:
            name = self.get_element() + " " + name
        if effect_type == "support_cards":
            self.spells[effect_type]["effect_prefix"] = (
                "Adds " if "Enhancer" in name else "Removes "
            )
        effect_type = (
            self.spells[effect_type]["effect_prefix"]
            + str(power)
            + self.spells[effect_type]["effect_suffix"]
            + " to target"
        )
        return [name, cost, card_data["rarity"], effect_type]

    def generate_artifact_data(
        self,
        name: str = "",
        power: int = 0,
        card_category: str = ""
    ) -> list[str | int]:
        card_data = self.generate_rarity(card_category)
        if not power:
            power = random.randint(
                card_data["attr"]["effect"][0],
                card_data["attr"]["effect"][1]
            )
        cost: int = random.randint(
            card_data["attr"]["cost"][0],
            card_data["attr"]["cost"][1]
        )
        durability: int = random.randint(
            card_data["attr"]["durability"][0],
            card_data["attr"]["durability"][1]
        )
        if not name:
            name = random.choice(self.artifacts["objects"])
        if not card_category:
            artifact_categories: list[str] = [
                cat for cat in self.artifacts["adjs_plus"].keys()
            ]
            effect: str = random.choice(artifact_categories)
        artifact_property: str = "adjs_" + random.choice("plus", "minus")
        name = random.choice(
            self.artifacts[artifact_property][effect]
        ) + " " + name
        sign: str = ("+" if "plus" in artifact_property else "-")
        effect = "Permanent: " + sign + str(power) + " " + effect
        if "Diminisher" in name or "Burden" in name:
            effect += " cost"
        return [name, cost, card_data["rarity"], effect, durability]

    def create_creature(self, name_or_power: str | int | None = None) -> Card:
        name: str = ""
        cost: int
        rarity: str
        attack: int = 0
        health: int
        card_category: str = ""
        if isinstance(name_or_power, str):
            cards: list[str] = [
                key for key in self.creatures.keys()
                if "cards" in key
            ]
            for card_type in cards:
                for card_name in self.creatures[card_type]:
                    print(f"CARD NAME: {card_name}\n\n")
                    if card_name in name_or_power:
                        card_category = card_type
                        print(f"CATEGORY: {card_category}\n\n")
            name = name_or_power
        if isinstance(name_or_power, int):
            if name_or_power >= self.leg_attr["attack"][1]:
                card_category = "leg"
            else:
                categories: list[dict[str, tuple[int, int] | str]] = [
                    self.leg_attr,
                    self.srare_attr,
                    self.orare_attr,
                    self.common_attr
                ]
                for category in categories:
                    if (
                        category["attack"][0] <=
                        name_or_power <
                        category["attack"][1]
                    ):
                        card_category = category["type"]
                        print(f"CATEGORY: {card_category}\n\n")
            effect = name_or_power
        name, cost, rarity, attack, health = self.generate_creature_data(
            name, effect, card_category
        )
        return CreatureCard(name, cost, rarity, attack, health)

    def create_spell(self, name_or_power: str | int | None = None) -> Card:
        name: str = ""
        cost: int
        rarity: str
        effect: str = 0
        card_category: str = ""
        if isinstance(name_or_power, str):
            for card_type in [key for key in self.spells.keys()]:
                if card_type in name_or_power:
                    card_category = card_type
                    break
                for card_name in self.spells[card_type]:
                    if card_name in name_or_power:
                        card_category = card_type
                        name = name_or_power
        elif isinstance(name_or_power, int):
            if name_or_power >= self.leg_attr["effect"]:
                card_category = "leg"
            else:
                categories: list[dict[str, tuple[int, int] | str]] = [
                    self.leg_attr,
                    self.srare_attr,
                    self.orare_attr,
                    self.common_attr
                ]
                for category in categories:
                    if (
                        category["effect"][0] <=
                        name_or_power <
                        category["effect"][1]
                    ):
                        card_category = category["type"]
            effect = name_or_power
        name, cost, rarity, effect = self.generate_spell_data(
            name, effect, card_category
        )
        return SpellCard(name, cost, rarity, effect)

    def create_artifact(self, name_or_power: str | int | None = None) -> Card:
        name: str = ""
        cost: int
        rarity: str
        effect: str = ""
        durability: int
        card_category: str = ""
        if isinstance(name_or_power, str):
            if name_or_power in self.artifacts["objects"]:
                name = name_or_power
            elif name_or_power in [
                cat for cat in self.artifacts["abjs_plus"].keys()
            ]:
                card_category = name_or_power + "_cards"
        elif isinstance(name_or_power, int):
            if name_or_power >= self.leg_attr["effect"][1]:
                card_category = "leg"
            else:
                categories: list[dict[str, tuple[int, int] | str]] = [
                    self.leg_attr,
                    self.srare_attr,
                    self.orare_attr,
                    self.common_attr
                ]
                for category in categories:
                    if (
                        category["effect"][0] <=
                        name_or_power <
                        category["effect"][1]
                    ):
                        card_category = category["type"]
            effect = name_or_power
        name, cost, rarity, effect, durability = self.generate_artifact_data(
            name, effect, card_category
        )
        return ArtifactCard(name, cost, rarity, effect, durability)

    def create_themed_deck(self, size: int) -> dict:
        all_cards: list[Card] = []
        for card in range(size):
            card_type = random.choice([
                "creature",
                "spell",
                "artifact"
            ])
            match card_type:
                case "creature":
                    card_name: str = random.choice((
                        self.creatures["leg_cards"] +
                        self.creatures["srare_cards"] +
                        self.creatures["orare_cards"] +
                        self.creatures["common_cards"]
                    ))
                    card_power: int | str = random.randint(
                        1, self.leg_attr["attack"][1]
                    )
                    creation_func = self.create_creature
                case "spell":
                    card_name = random.choice((
                        self.spells["offensive_cards"]["card_names"] +
                        self.spells["healing_cards"]["card_names"] +
                        self.spells["support_cards"]["card_names"]
                    ))
                    card_power = random.choice([
                        random.randint(1, self.leg_attr["effect"][1]),
                        random.choice("offensive", "healing", "support")
                    ])
                    creation_func = self.create_spell
                case "artifact":
                    card_name = random.choice(self.artifacts["objects"])
                    card_power = random.choice([
                        random.randint(1, self.leg_attr["effect"][1]),
                        random.choice([
                            cat for cat in self.artifacts["adjs_plus"].keys()
                        ])
                    ])
                    creation_func = self.create_artifact
            all_cards.append(creation_func(
                random.choice([card_name, card_power, None])
            ))
        return {
            "total_cards": all_cards,
            "creature_cards": [
                card for card in all_cards
                if isinstance(card, CreatureCard)
            ],
            "spell_cards": [
                card for card in all_cards
                if isinstance(card, SpellCard)
            ],
            "artifact_cards": [
                card for card in all_cards
                if isinstance(card, ArtifactCard)
            ]
        }


def test_factory() -> None:
    if len(sys.argv) == 1:
        print(FantasyCardFactory.create_themed_deck(random.choice(1, 11)))
        return None
    for arg in sys.argv:
        try:
            print(
                FantasyCardFactory.create_themed_deck(int(arg))
            )
        except ValueError as ve:
            print(f"Caught ValueError while parsing arguments: {ve}")


if __name__ == "__main__":
    test_factory()
