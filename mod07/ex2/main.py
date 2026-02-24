from ex0.Card import Card
from ex0.CreatureCard import CreatureCard
from ex1.SpellCard import SpellCard
from ex1.ArtifactCard import ArtifactCard
from ex1.Deck import Deck
from .EliteCard import EliteCard
from .Combatable import Combatable
from .Magical import Magical
import random


# creature cards
fire_dragon: CreatureCard = CreatureCard(
    "Fire Dragon",
    5,
    "Legendary",
    7,
    6
)
goblin_warrior: CreatureCard = CreatureCard(
    "Goblin Warrior",
    3,
    "Rare",
    5,
    3
)
acromentula: CreatureCard = CreatureCard(
    "Acromentula",
    4,
    "Common",
    4,
    2
)
sacred_unicorn: CreatureCard = CreatureCard(
    "Sacred Unicorn",
    7,
    "Legendary",
    8,
    10
)

# spell cards
lightning_spell: SpellCard = SpellCard(
    "Lightning Bolt",
    4,
    "Rare",
    "Deal 3 damage to target"
)
fire_spell: SpellCard = SpellCard(
    "Fire Torch",
    3,
    "Common",
    "Deal 2 damage to target"
)
healing_spell: SpellCard = SpellCard(
    "Heal Balm",
    5,
    "Super Rare",
    "Restores 4 health to target"
)
super_healing_spell: SpellCard = SpellCard(
    "Heal Fountain",
    7,
    "Legendary",
    "Restores 6 health to target"
)
attack_buff_spell: SpellCard = SpellCard(
    "Attack Enhancer",
    3,
    "Common",
    "Adds 2 attack to target"
)
attack_debuff_spell: SpellCard = SpellCard(
    "Attack Diminisher",
    3,
    "Common",
    "Removes 2 attack to target"
)

# artifact cards
mana_artifact: ArtifactCard = ArtifactCard(
    "Mana Crystal",
    2,
    "Rare",
    3,
    "Permanent: +1 mana per turn"
)
mana_debuff: ArtifactCard = ArtifactCard(
    "Mana Penalizer",
    2,
    "Rare",
    1,
    "Permanent: +1 mana cost"
)
mana_buff: ArtifactCard = ArtifactCard(
    "Mana Lightener",
    2,
    "Rare",
    1,
    "Permanent: -1 mana cost"
)
healing_artifact: ArtifactCard = ArtifactCard(
    "Heal Potion",
    4,
    "Rare",
    3,
    "Permanent: +2 health"
)
damage_artifact: ArtifactCard = ArtifactCard(
    "Atomic Laser",
    7,
    "Legendary",
    5,
    "Permanent: -2 health"
)
attack_booster_artifact: ArtifactCard = ArtifactCard(
    "Power Ring",
    3,
    "Common",
    2,
    "Permanent: +1 attack per turn"
)
attack_diminisher_artifact: ArtifactCard = ArtifactCard(
    "Weakness Belt",
    3,
    "Common",
    2,
    "Permanent: -1 attack per turn"
)

# elite cards
dark_sorcerer: EliteCard = EliteCard(
    "Dark Sorcerer",
    3,
    "Super Rare",
    5,
    2,
    20,
    10,
    "long-range",
    [lightning_spell, fire_spell]
)
divine_healer: EliteCard = EliteCard(
    "Divine Healer",
    2,
    "Super Rare",
    1,
    4,
    20,
    15,
    "long-range",
    [healing_spell, super_healing_spell]
)
acrobatic_monk: EliteCard = EliteCard(
    "Acrobatic Monk",
    3,
    "Super Rare",
    8,
    6,
    10,
    15,
    "melee",
    [attack_buff_spell, attack_debuff_spell]
)
forest_elf: EliteCard = EliteCard(
    "Forest Elf",
    3,
    "Super Rare",
    4,
    5,
    18,
    12,
    "versatile",
    [lightning_spell, healing_spell, attack_buff_spell]
)


def execute_turn(
    deck: Deck,
    enemy_deck: Deck
) -> None:

    deck.draw_card()

    game_state: dict = {
        "hand": deck.hand,
        "all_targets": enemy_deck.hand,
        "available_mana": deck.available_mana,
        "enemy_mana": enemy_deck.available_mana,
        "ally_beings": deck.living_beings,
        "living_targets": enemy_deck.living_beings,
        "priority_target": (
            None if not enemy_deck.living_beings
            else random.choice(enemy_deck.living_beings)
        ),
        "cards_to_remove": []
    }

    play_result: dict = random.choice(game_state["hand"]).play(game_state)

    if not play_result:
        return None

    deck.available_mana -= play_result["mana_used"]

    for card in game_state["cards_to_remove"]:
        deck.remove_from_all(card)

    enemy_deck.check_card_health


def build_decks(deck1: Deck, deck2: Deck) -> None:

    print("\n\nBuilding deck with different card types...\n")

    deck1.add_card(fire_dragon)
    deck1.add_card(sacred_unicorn)
    deck1.add_card(lightning_spell)
    deck1.add_card(super_healing_spell)
    deck1.add_card(attack_buff_spell)
    deck1.add_card(mana_artifact)
    deck1.add_card(healing_artifact)
    deck1.add_card(damage_artifact)
    deck1.add_card(attack_booster_artifact)
    deck1.add_card(dark_sorcerer)
    deck1.add_card(divine_healer)

    deck2.add_card(goblin_warrior)
    deck2.add_card(acromentula)
    deck2.add_card(fire_spell)
    deck2.add_card(attack_debuff_spell)
    deck2.add_card(attack_diminisher_artifact)
    deck2.add_card(acrobatic_monk)
    deck2.add_card(forest_elf)
    deck2.add_card(mana_debuff)
    deck2.add_card(healing_spell)
    deck2.add_card(mana_buff)

    print(f"Deck One stats: {deck1.get_deck_stats()}")
    print(f"Deck Two stats: {deck2.get_deck_stats()}\n")


def main() -> None:

    print("\n==== DataDeck Ability System ====\n\n")

    print("EliteCard capabilities:\n")

    capabilities: dict = {}

    for card_class in [Card, Combatable, Magical]:
        capabilities[card_class.__name__] = [
            method for method in dir(card_class)
            if callable(getattr(card_class, method))
            and not method.startswith("__")
        ]

    for class_name, class_methods in capabilities.items():
        print(f"- {class_name}: {class_methods}")

    print("\n")

    deck1: Deck = Deck(input("Enter name of Player One: "))
    deck2: Deck = Deck(input("Enter name of Player Two: "))

    build_decks(deck1, deck2)

    deck1.shuffle()
    deck2.shuffle()

    print("\nDrawing 3 initial cards:\n")

    for deck in [deck1, deck2]:

        print(f"\n< Player {deck.player} >\n")

        deck.draw_card()
        deck.draw_card()
        deck.draw_card()

    default_turn_nb: int = 5

    try:

        turn_nb: int = int(input(
            "\n\nEnter the number of turns to simulate:"
        ))

    except ValueError:

        print(
            "Invalid value given for number of turns "
            f"- Resorting to default number [{default_turn_nb}]\n"
        )
        turn_nb = default_turn_nb

    print("\n\nDrawing and playing cards:\n")

    for i in range(turn_nb):

        print(f"\n\n==== Turn {i + 1}: Player {deck1.player} ====\n\n")
        execute_turn(deck1, deck2)

        print(f"\n\n==== Turn {i + 1}: Player {deck2.player} ====\n\n")
        execute_turn(deck2, deck1)

    print("\n\nMultiple interface implementation successful!\n")


if __name__ == "__main__":
    main()
