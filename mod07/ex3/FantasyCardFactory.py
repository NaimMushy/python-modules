from ex0.Card import Card
from ex0.CreatureCard import CreatureCard
from ex1.SpellCard import SpellCard
from ex1.ArtifactCard import ArtifactCard
from .CardFactory import CardFactory
from typing import Any as any
import random


# creature cards
CREATURES: dict[str, list[str]] = {
    "leg_cards": ["Dragon", "Phoenix", "Elemental Spirit", "Kraken"],
    "srare_cards": ["Unicorn", "Fairy", "Selkie", "Animal Sovereign"],
    "orare_cards": ["Ogre", "Acromentula", "Shapeshifter", "Malicious Spirit"],
    "common_cards": ["Goblin", "Wolf", "Spider", "Zombie"],
    "leg_adjs": [
        "Fire",
        "Ice",
        "Wind",
        "Lightning",
        "Poison",
        "Acid",
        "Shadow",
        "Earth",
        "Psychic"
    ],
    "srare_adjs": ["Sacred", "Mighty", "Superb", "Arcane"],
    "orare_adjs": ["Imposing", "Stealthy", "Agile", "Genius"],
    "common_adjs": ["Warrior", "Resilient", "Bloodthirsty", "Scary"]
}

# spells
SPELLS: dict[str, dict[str, list[str] | str]] = {
    "offensive_cards": {
        "card_names": ["Bolt", "Ray", "Ball", "Tornado", "Gun"],
        "effect_prefix": "Deals",
        "effect_suffix": "damage"
    },
    "healing_cards": {
        "card_names": ["Balm", "Fountain", "Hug", "Charm"],
        "name_prefix": "Healing",
        "effect_prefix": "Restores",
        "effect_suffix": "health"
    },
    "mana_cards": {
        "card_names": ["Curse", "Blessing"],
        "name_prefix": "Mana",
        "effect_suffix": "mana cost"
    },
    "attack_cards": {
        "card_names": ["Buff", "Debuff"],
        "name_prefix": "Attack",
        "effect_suffix": "attack power"
    }
}

# artifact cards
ARTIFACTS: dict[str, list[str] | dict[str, list[str]]] = {
    "objects": [
        "Staff",
        "Ring",
        "Belt",
        "Crystal",
        "Potion",
        "Watch",
        "Earring",
        "Dagger"
    ],
    "adjs_plus": {
        "mana": ["Mana Booster", "Mana Burden"],
        "attack": ["Power", "Atomic", "Strength", "Enchanted"],
        "health": ["Heal", "Soothing", "Blessed"]
    },
    "adjs_minus": {
        "mana": ["Mana Diminisher", "Mana Lightener"],
        "attack": ["Weakness", "Diminisher", "Debuff"],
        "health": ["Cursed", "Poisoning", "Bloodthirsty"]
    }
}


class FantasyCardFactory(CardFactory):
    def __init__(self) -> None:
        self.creatures: dict[str, list[str]] = CREATURES
        self.spells: dict[str, dict[str, list[str] | str]] = SPELLS
        self.artifacts: dict[str, list[str] | dict[str, list[str]]] = ARTIFACTS

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
            "Fire",
            "Ice",
            "Wind",
            "Lightning",
            "Poison",
            "Acid",
            "Shadow",
            "Psychic"
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
        ) + " " + name
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
        if not card_category:
            card_category = random.choice([cat for cat in self.spells.keys()])
        if not name:
            name = random.choice(self.spells[card_category]["card_names"])
        name = (
            (self.spells[card_category]["name_prefix"] + " " + name)
            if "offensive" not in card_category
            else self.get_element() + " " + name
        )
        prefix: str = (
            ("Adds" if "Curse" in name or "Buff" in name else "Removes")
            if "attack" in card_category or "mana" in card_category
            else self.spells[card_category]["effect_prefix"]
        )
        effect_type = (
            prefix
            + " "
            + str(power)
            + " "
            + self.spells[card_category]["effect_suffix"]
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
            effect: str = random.choice([
                cat for cat in self.artifacts["adjs_plus"].keys()
            ])
        artifact_property: str = "adjs_" + random.choice(["plus", "minus"])
        name = random.choice(
            self.artifacts[artifact_property][effect]
        ) + " " + name
        sign: str = ("+" if "plus" in artifact_property else "-")
        effect = "Permanent: " + sign + str(power) + " " + effect
        if "Lightener" in name or "Burden" in name:
            effect += " cost"
        return [name, cost, card_data["rarity"], durability, effect]

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
                for category in [
                    self.leg_attr,
                    self.srare_attr,
                    self.orare_attr,
                    self.common_attr
                ]:
                    if (
                        category["attack"][0] <=
                        name_or_power <
                        category["attack"][1]
                    ):
                        card_category = category["type"]
                        print(f"CATEGORY: {card_category}\n\n")
            attack = name_or_power
        name, cost, rarity, attack, health = self.generate_creature_data(
            name, attack, card_category
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
                if name_or_power in card_type:
                    card_category = card_type
                    break
                card_name: dict = self.spells[card_type]
                if (
                    name_or_power in card_name["card_names"]
                ) or (
                    name_or_power in card_name["effect_suffix"]
                ):
                    card_category = card_type
                    name = name_or_power
        elif isinstance(name_or_power, int):
            if name_or_power >= self.leg_attr["effect"]:
                card_category = "leg"
            else:
                for category in [
                    self.leg_attr,
                    self.srare_attr,
                    self.orare_attr,
                    self.common_attr
                ]:
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
                card_category = name_or_power
        elif isinstance(name_or_power, int):
            if name_or_power >= self.leg_attr["effect"][1]:
                card_category = "leg"
            else:
                for category in [
                    self.leg_attr,
                    self.srare_attr,
                    self.orare_attr,
                    self.common_attr
                ]:
                    if (
                        category["effect"][0] <=
                        name_or_power <
                        category["effect"][1]
                    ):
                        card_category = category["type"]
            effect = name_or_power
        name, cost, rarity, durability, effect = self.generate_artifact_data(
            name, effect, card_category
        )
        return ArtifactCard(name, cost, rarity, durability, effect)

    def create_themed_deck(self, size: int) -> dict:
        all_cards: dict[str, list[Card]] = {}
        if size:
            print(f"\n=== CREATING DECK OF {size} CARDS ===\n\n")
            all_cards["total_cards"] = []
        for card in range(size):
            card_type, card_values = random.choice([
                (types, type_values)
                for types, type_values in self.get_supported_types().items()
            ])
            card_created: Card = card_values["creation_func"](
                random.choice([
                    card_values["card_names"],
                    card_values["card_powers"],
                    None
                ])
            )
            if card_type not in all_cards.keys():
                all_cards[card_type] = []
            all_cards["total_cards"].append(card_created)
            all_cards[card_type].append(card_created)
            print(f"[CARD CREATED]: {card_created.get_card_info()}\n")
        return all_cards

    def get_supported_types(self) -> dict[str, dict[str, any]]:
        return {
            "creatures": {
                "card_names": [
                    name for card_type in self.creatures.keys()
                    if "cards" in card_type
                    for name in self.creatures[card_type]
                ],
                "card_powers": [
                    power for power in range(1, self.leg_attr["attack"][1])
                ],
                "creation_func": self.create_creature,
            },
            "spells": {
                "card_names": [
                    name for card_types in self.spells.keys()
                    for name in self.spells[card_types]["card_names"]
                ],
                "card_powers": [
                    power for power in range(1, self.leg_attr["effect"][1])
                ] + [
                    power.replace("_cards", "") for power in self.spells.keys()
                ] + [
                    self.spells[card_type]["effect_suffix"]
                    for card_type in self.spells.keys()
                ],
                "creation_func": self.create_spell
            },
            "artifacts": {
                "card_names": self.artifacts["objects"],
                "card_powers": [
                    power for power in range(1, self.leg_attr["effect"][1])
                ] + [
                    power for power in self.artifacts["adjs_plus"].keys()
                ],
                "creation_func": self.create_artifact
            }
        }
