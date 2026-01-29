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
healing_artifact: ArtifactCard = ArtifactCard(
    "Heal Potion",
    4,
    "Rare",
    3,
    "Permanent: +2 health per turn"
)
damage_artifact: ArtifactCard = ArtifactCard(
    "Atomic Laser",
    7,
    "Legendary",
    5,
    "Permanent: -2 health per turn"
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
        card_drawn.play(game_state)
    for card in deck.active_cards:
        if isinstance(card, SpellCard):
            if (
                "damage" in card.effect_type or
                "Removes" in card.effect_type
            ):
                if len(deck.enemy_deck.active_cards):
                    card.resolve_effect([
                        card for card in deck.enemy_deck.active_cards
                        if isinstance(card, CreatureCard)
                    ])
                    deck.active_cards.remove(card)
            else:
                card.resolve_effect([
                    card for card in deck.active_cards
                    if isinstance(card, CreatureCard)
                ])
                deck.active_cards.remove(card)
        elif isinstance(card, CreatureCard):
            if card.get_health() == 0:
                print(f"Creature {card.name} has been defeated\n")
                deck.active_cards.remove(card)
            else:
                possible_targets: list[Card] = [
                    target for target in deck.enemy_deck.active_cards
                    if target.__repr__() == "CreatureCard"
                ]
                if len(possible_targets):
                    card.attack_target(random.choice(possible_targets))
        elif isinstance(card, ArtifactCard):
            game_state["last_played"] = card.activate_ability()
            if (
                game_state["last_played"]["target"] == "ally" and
                (len(deck.stack_cards) or len(deck.active_cards))
            ):
                apply_effect(
                    game_state["last_played"]["effect"],
                    deck.stack_cards + deck.active_cards
                )
                card.durability -= 1
            elif (
                game_state["last_played"]["target"] == "enemy" and
                (
                    len(deck.enemy_deck.stack_cards) or
                    len(deck.enemy_deck.active_cards)
                )
            ):
                apply_effect(
                    game_state["last_played"]["effect"],
                    (
                        deck.enemy_deck.stack_cards +
                        deck.enemy_deck.active_cards
                    )
                )
                card.durability -= 1
            if card.durability <= 0:
                print(
                    f"Artifact {card.name} "
                    "destroyed - durability depleted\n"
                )
                deck.active_cards.remove(card)
            elif not game_state["last_played"]["repeat"]:
                deck.active_cards.remove(card)
                deck.add_card(card)


def apply_effect(effect: list | str, targets: list[Card]) -> None:
    if isinstance(effect, str):
        if effect == "unknown":
            print("No card effect for this turn\n")
    else:
        if effect[0] == "health":
            for target in targets:
                if isinstance(target, CreatureCard):
                    target.set_health(target.get_health() + effect[1])
                    if effect[1] > 0:
                        print(
                            f"Effect <+{effect[1]} health points> "
                            f"applied to {target.name}"
                        )
                    else:
                        print(
                            f"Effect <{effect[1]} health points> "
                            f"applied to {target.name}"
                        )
        elif effect[0] == "mana":
            for target in targets:
                target.cost += effect[1]
                if effect[1] > 0:
                    print(
                        f"Effect <+{effect[1]} mana cost> "
                        f"applied to {target.name}"
                    )
                else:
                    print(
                        f"Effect <{effect[1]} mana cost> "
                        f"applied to {target.name}"
                    )
        elif effect[0] == "attack":
            for target in targets:
                if isinstance(target, CreatureCard):
                    target.set_attack(
                        target.get_attack() + effect[1]
                    )
                    if effect[1] > 0:
                        print(
                            f"Effect <+{effect[1]} attack> "
                            f"applied to {target.name}"
                        )
                    else:
                        print(
                            f"Effect <{effect[1]} attack> "
                            f"applied to {target.name}"
                        )


def build_decks(deck1: Deck, deck2: Deck) -> None:
    print("\n=== DataDeck Deck Builder ===\n")
    print("Building deck with different card types...")
    deck1.add_card(fire_dragon)
    deck1.add_card(sacred_unicorn)
    deck1.add_card(lightning_spell)
    deck1.add_card(healing_spell)
    deck1.add_card(attack_buff_spell)
    deck1.add_card(mana_artifact)
    deck1.add_card(healing_artifact)
    deck1.add_card(damage_artifact)
    deck1.add_card(attack_booster_artifact)
    deck2.add_card(goblin_warrior)
    deck2.add_card(acromentula)
    deck2.add_card(fire_spell)
    deck2.add_card(attack_debuff_spell)
    deck2.add_card(attack_diminisher_artifact)
    print(f"Deck One stats: {deck1.get_deck_stats()}")
    print(f"Deck Two stats: {deck2.get_deck_stats()}\n")


def main() -> None:
    game_state: dict = {}
    game_state["available_mana"] = 30
    deck1: Deck = Deck()
    deck2: Deck = Deck()
    build_decks(deck1, deck2)
    deck1.add_enemy_deck(deck2)
    deck2.add_enemy_deck(deck1)
    deck1.shuffle()
    deck2.shuffle()
    print("Drawing and playing cards:\n")
    for i in range(1, 6):
        print(f"=== Turn {i}: Deck One ===\n")
        print("Deck One Cards:")
        deck1.display_cards()
        play_card(game_state, deck1)
        print("Deck One Cards:")
        deck1.display_cards()
        print(f"=== Turn {i}: Deck Two ===\n")
        print("Deck Two Cards:")
        deck2.display_cards()
        play_card(game_state, deck2)
        print("Deck Two Cards:")
        deck2.display_cards()
    print("Polymorphism in action: Same interface, different card behaviors!")


if __name__ == "__main__":
    main()
