from ex0.Card import Card
from ex0.CreatureCard import CreatureCard
from .ArtifactCard import ArtifactCard
from .SpellCard import SpellCard
from .Deck import Deck
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
    "Permanent: +1 attack"
)
attack_diminisher_artifact: ArtifactCard = ArtifactCard(
    "Weakness Belt",
    3,
    "Common",
    2,
    "Permanent: -1 attack"
)


def execute_turn(
    deck: Deck,
    enemy_deck: Deck
) -> None:
    card_drawn: Card = deck.draw_card()
    if card_drawn not in deck.hand:
        deck.hand.append(card_drawn)
        if isinstance(card_drawn, CreatureCard):
            deck.living_beings.append(card_drawn)
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
    play_result: dict = (random.choice(game_state["hand"])).play(game_state)
    if not play_result:
        return None
    deck.available_mana -= play_result["mana_used"]
    for card in game_state["cards_to_remove"]:
        deck.remove_from_all(card)
    enemy_deck.check_card_health()


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
    deck1.add_card(mana_buff)
    deck1.add_card(attack_booster_artifact)
    deck2.add_card(goblin_warrior)
    deck2.add_card(acromentula)
    deck2.add_card(fire_spell)
    deck2.add_card(attack_debuff_spell)
    deck2.add_card(attack_diminisher_artifact)
    deck2.add_card(mana_debuff)
    print(f"Deck One stats: {deck1.get_deck_stats()}")
    print(f"Deck Two stats: {deck2.get_deck_stats()}\n")


def main() -> None:
    deck1: Deck = Deck("Gabach")
    deck2: Deck = Deck("Ibady")
    build_decks(deck1, deck2)
    deck1.shuffle()
    deck2.shuffle()
    print("Drawing and playing cards:\n")
    for i in range(1, 6):
        print(f"=== Turn {i}: Player {deck1.player} ===\n")
        execute_turn(deck1, deck2)
        print(f"=== Turn {i}: Player {deck2.player} ===\n")
        execute_turn(deck2, deck1)
    print("Polymorphism in action: Same interface, different card behaviors!")


if __name__ == "__main__":
    main()
