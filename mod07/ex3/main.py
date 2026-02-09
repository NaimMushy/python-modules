from ex0.Card import Card
from ex0.CreatureCard import CreatureCard
from ex1.SpellCard import SpellCard
from ex1.ArtifactCard import ArtifactCard
from ex1.Deck import Deck
from ex2.EliteCard import EliteCard
from .AggressiveStrategy import AggressiveStrategy


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


def play_card(
    game_state: dict,
    deck: Deck,
) -> None:
    card_drawn: Card = deck.draw_card()
    print(
        f"Drew: {card_drawn.name} "
        f"({card_drawn.get_card_info()['type']})"
    )
    if card_drawn not in deck.active_cards:
        deck.active_cards.append(card_drawn)
        if isinstance(card_drawn, (EliteCard, CreatureCard)):
            deck.possible_targets.append(card_drawn)
        if card_drawn.is_playable(deck.available_mana):
            deck.available_mana -= card_drawn.cost
        game_state["available_mana"] = deck.available_mana
        card_drawn.play(game_state)
    game_state["strategy"].execute_turn(
        [deck.available_mana] + deck.active_cards,
        deck.enemy_deck.active_cards
    )


def build_decks(deck1: Deck, deck2: Deck) -> None:
    print("\n=== DataDeck Deck Builder ===\n")
    print("Building deck with different card types...")
    deck1.add_card(fire_dragon)
    deck1.add_card(sacred_unicorn)
    deck1.add_card(lightning_spell)
    deck1.add_card(healing_spell)
    deck1.add_card(super_healing_spell)
    deck1.add_card(attack_buff_spell)
    deck1.add_card(mana_artifact)
    deck1.add_card(healing_artifact)
    deck1.add_card(damage_artifact)
    deck1.add_card(attack_booster_artifact)
    deck1.add_card(dark_sorcerer)
    deck1.add_card(divine_healer)
    deck1.add_card(mana_buff)
    deck2.add_card(goblin_warrior)
    deck2.add_card(acromentula)
    deck2.add_card(fire_spell)
    deck2.add_card(attack_debuff_spell)
    deck2.add_card(attack_diminisher_artifact)
    deck2.add_card(acrobatic_monk)
    deck2.add_card(forest_elf)
    deck2.add_card(mana_debuff)
    print(f"Deck One stats: {deck1.get_deck_stats()}")
    print(f"Deck Two stats: {deck2.get_deck_stats()}\n")


def main() -> None:
    deck1: Deck = Deck()
    deck2: Deck = Deck()
    build_decks(deck1, deck2)
    deck1.shuffle()
    deck2.shuffle()
    print("Drawing and playing cards:\n")
    for i in range(1, 6):
        print(f"=== Turn {i}: Deck One ===\n")
        play_card(deck1, deck2)
        print(f"=== Turn {i}: Deck Two ===\n")
        play_card(deck2, deck1)
    print("Polymorphism in action: Same interface, different card behaviors!")


if __name__ == "__main__":
    main()
