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
    card_to_play: Card
) -> None:
    deck: Deck = game_state["player_deck"]
    if card_to_play not in deck.active_cards:
        deck.active_cards.append(card_to_play)
        if card_to_play.__repr__() == "CreatureCard":
            card_to_play.play(game_state)
    for card in deck.active_cards:
        if card.__repr__() == "SpellCard":
            card.play(game_state)
            deck.active_cards.remove(card)
        elif (
            card.__repr__() == "CreatureCard"
            and len(game_state["enemy_deck"].active_cards)
        ):
            card.attack_target(random.choice(
                game_state["enemy_deck"].active_cards)
            )
        elif card.__repr__() == "ArtifactCard":
            card.play(game_state)
            if card.durability <= 0:
                print(
                    f"Artifact {card.name} "
                    "destroyed - durability depleted\n"
                )
                deck.active_cards.remove(card)
            else:
                apply_effect(game_state)
                if not game_state["last_played"]["repeat"]:
                    deck.active_cards.remove(card)
                    deck.add_card(card)


def apply_effect(game_state: dict) -> None:
    effect: list | str = game_state["last_played"]["effect"]
    if isinstance(effect, str):
        if effect == "unknown":
            print("No card effect for this turn\n")
    else:
        if effect[0] == "health":
            if effect[1] > 0:
                for ally in game_state["player_deck"].active_cards:
                    if ally.__repr__() == "CreatureCard":
                        ally.set_health(ally.get_health() + effect[1])
            else:
                for target in game_state["enemy_deck"].active_cards:
                    if target.__repr__() == "CreatureCard":
                        target.set_health(target.get_health() + effect[1])
        elif effect[0] == "mana":
            if effect[1] > 0:
                for card in game_state["player_deck"].active_cards:
                    card.cost += effect[1]
            else:
                for card in game_state["enemy_deck"].active_cards:
                    card.cost += effect[1]
        elif effect[0] == "attack":
            if effect[1] > 0:
                for ally in game_state["player_deck"].active_cards:
                    if ally.__repr__() == "CreatureCard":
                        ally.attack += effect[1]
            else:
                for target in game_state["enemy_deck"].active_cards:
                    if target.__repr__() == "CreatureCard":
                        target.attack += effect[1]


def build_decks(player_deck: Deck, enemy_deck: Deck) -> None:
    print("\n=== DataDeck Deck Builder ===\n")
    print("Building deck with different card types...")
    player_deck.add_card(fire_dragon)
    player_deck.add_card(sacred_unicorn)
    player_deck.add_card(lightning_spell)
    player_deck.add_card(healing_spell)
    player_deck.add_card(attack_buff_spell)
    player_deck.add_card(mana_artifact)
    player_deck.add_card(healing_artifact)
    player_deck.add_card(damage_artifact)
    player_deck.add_card(attack_booster_artifact)
    enemy_deck.add_card(goblin_warrior)
    enemy_deck.add_card(acromentula)
    enemy_deck.add_card(fire_spell)
    enemy_deck.add_card(attack_debuff_spell)
    enemy_deck.add_card(attack_diminisher_artifact)
    print(f"Deck stats: {player_deck.get_deck_stats()}\n")


def main() -> None:
    game_state: dict = {}
    game_state["available_mana"] = 30
    player_deck: Deck = Deck()
    enemy_deck: Deck = Deck()
    build_decks(player_deck, enemy_deck)
    game_state["player_deck"] = player_deck
    game_state["enemy_deck"] = enemy_deck
    print("Drawing and playing cards:\n")
    for i in range(5):
        print(f"Turn {i}:")
        enemy_deck.draw_card()
        card_drawn: Card = player_deck.draw_card()
        if card_drawn.__repr__() == "CreatureCard":
            card_type: str = "Creature"
        elif card_drawn.__repr__() == "SpellCard":
            card_type = "Spell"
        elif card_drawn.__repr__() == "ArtifactCard":
            card_type = "Artifact"
        else:
            card_type = "Unknown"
        print(f"Drew: {card_drawn.name} ({card_type})")
        play_card(game_state, card_drawn)
    print("Polymorphism in action: Same interface, different card behaviors!")


if __name__ == "__main__":
    main()
