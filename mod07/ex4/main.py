from .TournamentPlatform import TournamentPlatform
from .TournamentCard import TournamentCard
import random


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

    platform: TournamentPlatform = TournamentPlatform()

    default_card_nb: int = 6

    try:

        nb_cards: int = int(input(
            "Enter number of cards to generate: "
        ))

    except ValueError:

        print(
            f"\n\nInvalid value given for number of cards"
            f" - Resorting to default number [{default_card_nb}]\n"
        )
        nb_cards = default_card_nb

    cards: list[TournamentCard] = [
        card_factory()
        for _ in range(nb_cards)
    ]

    for card in cards:
        platform.register_card(card)

    default_match_nb: int = 3

    try:

        match_nb: int = int(input(
            "\n\nEnter number of matches to play: "
        ))

    except ValueError:

        print(
            f"\n\nInvalid value given for number of matches"
            f" - Resorting to default number [{default_match_nb}]\n"
        )
        match_nb = default_match_nb

    for _ in range(match_nb):

        available_cards: list[str] = [
            card_id for card_id in platform.cards.keys()
        ]

        card1_id: str = random.choice(available_cards)
        available_cards.remove(card1_id)

        card2_id: str = random.choice(available_cards)
        platform.create_match(card1_id, card2_id)

    platform.get_leaderboard()

    platform.generate_tournament_report()

    print("\n\n=== Tournament Platform Successfully Deployed! ===\n")

    print("All abstract patterns working together harmoniously!\n")


if __name__ == "__main__":
    main()
