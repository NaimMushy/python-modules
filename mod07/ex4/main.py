from .TournamentPlatform import TournamentPlatform
from .TournamentCard import TournamentCard
import random
import sys


DEFAULT_CARD_NB: int = 6
DEFAULT_MATCH_NB: int = 3


def card_factory() -> TournamentCard:
    prefixes: list[str] = [
        "Fire",
        "Ice",
        "Shadow",
        "Lightning",
        "Poison",
        "Water",
        "Earth",
        "Light"
    ]
    suffixes: list[str] = [
        "Dragon",
        "Phoenix",
        "Wizard",
        "Unicorn",
        "Sorcerer",
        "Elf",
        "Tiefling",
        "Ork",
        "Kraken",
        "Spirit",
        "AnimalSovereign"
    ]
    combat_types: list[str] = [
        "melee",
        "ranged",
        "adaptive"
    ]
    attack_power: tuple[int, int] = (5, 21)
    health_points: tuple[int, int] = (10, 31)
    defense_capability: tuple[int, int] = (2, 11)
    base_rating: tuple[int, int] = (500, 1001)
    return TournamentCard(
        random.choice(prefixes) + " " + random.choice(suffixes),
        random.randint(*attack_power),
        random.randint(*health_points),
        random.randint(*defense_capability),
        random.choice(combat_types),
        random.randint(*base_rating)
    )


def main() -> None:
    nb_cards: int = DEFAULT_CARD_NB
    if len(sys.argv) > 1:
        try:
            nb_cards = int(sys.argv[1])
        except ValueError:
            print(
                f"Invalid value {sys.argv[1]} for number of cards"
                f" - Resorting to default number [{DEFAULT_CARD_NB}]"
            )
    cards: list[TournamentCard] = [
        card_factory()
        for new_card in range(nb_cards)
    ]
    platform: TournamentPlatform = TournamentPlatform()
    for card in cards:
        platform.register_card(card)
    match_nb: int = DEFAULT_MATCH_NB
    if len(sys.argv) > 2:
        try:
            match_nb = int(sys.argv[2])
        except ValueError:
            print(
                f"Invalid value {sys.argv[1]} for number of matches"
                f" - Resorting to default number [{DEFAULT_MATCH_NB}]"
            )
    for match in range(match_nb):
        available_cards: list[str] = [
            card_id for card_id in platform.cards.keys()
        ]
        card1_id: str = random.choice(available_cards)
        available_cards.remove(card1_id)
        card2_id: str = random.choice(available_cards)
        platform.create_match(card1_id, card2_id)
    platform.get_leaderboard()
    platform.generate_tournament_report()
    print("\n=== Tournament Platform Successfully Deployed! ===")
    print("All abstract patterns working together harmoniously!")


if __name__ == "__main__":
    main()
