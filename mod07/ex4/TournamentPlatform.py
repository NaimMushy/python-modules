from .TournamentCard import TournamentCard


class TournamentPlatform:

    def __init__(self) -> None:

        print("\n\n=== DataDeck Tournament Platform ===\n\n")

        self.cards: dict[str, TournamentCard] = {}
        self.match_count: int = 0

    def register_card(self, card: TournamentCard) -> str:

        print("\n\nRegistering Tournament Card...\n")

        card_id: str = card.name.split(" ")[-1].lower()

        type_count: str = str(sum(
            1 for card_type in self.cards.keys()
            if card_id in card_type
        ) + 1)

        card_id += (
            "_"
            + "0" * (3 - len(type_count))
            + type_count
        )

        if card_id in self.cards.keys():
            return f"{card.name} already registered!\n"

        self.cards[card_id] = card

        print(f"\n{card.name} (ID: {card_id}):")

        for stat, val in card.get_tournament_stats().items():
            print(f"{stat.capitalize()}: {val}")

        return f"\n\nRegistered {card.name} with ID: {card_id}!\n"

    def create_match(self, card1_id: str, card2_id: str) -> dict:

        print("\n\nCreating tournament match...\n")

        card1: TournamentCard = self.cards[card1_id]
        card2: TournamentCard = self.cards[card2_id]

        base_health: dict[str, int] = {
            card1_id: card1.get_health(),
            card2_id: card2.get_health()
        }

        match_ongoing: bool = True

        while match_ongoing:

            card1.play({"priority_target": card2})

            if card2.get_health() <= 0:
                winner: str = card1_id
                loser: str = card2_id
                match_ongoing = False

            else:
                card1, card2, card1_id, card2_id = (
                    card2, card1, card2_id, card1_id
                )

        self.cards[winner].update_wins(1)
        self.cards[loser].update_losses(1)

        self.cards[winner].set_health(base_health[winner])
        self.cards[loser].set_health(base_health[loser])

        match_result: dict = {
            "winner": winner,
            "loser": loser,
            "winner_rating": self.cards[winner].calculate_rating(),
            "loser_rating": self.cards[loser].calculate_rating()
        }

        print(f"\nMatch result: {match_result}\n")

        self.match_count += 1

        return match_result

    def get_leaderboard(self) -> list:

        print("\n\nTournament Leaderboard:\n")

        leaderboard: list[TournamentCard] = []

        ranking_cards: list[TournamentCard] = [
            val for val in self.cards.values()
        ]

        for rank in range(len(ranking_cards)):

            leader: TournamentCard = (
                max(
                    ranking_cards,
                    key=lambda card: card.calculate_rating()
                )
            )

            leaderboard.append(leader)

            ranking_cards.remove(leader)

            print(
                f"{rank + 1}. {leader.name} - Rating: "
                f"{leader.get_rank_info()['rating']} "
                f"({leader.get_rank_info()['record']})"
            )

        print("\n")

        return leaderboard

    def generate_tournament_report(self) -> dict:

        print("\n\nPlatform Report:\n")

        card_nb: int = len(self.cards.keys())

        platform_report: dict = {
            "total_cards": card_nb,
            "matches_played": self.match_count,
            "avg_rating": (sum(
                card.calculate_rating()
                for card in self.cards.values()
            ) // card_nb),
            "platform_status": (
                "active" if card_nb and self.match_count else "inactive"
            )
        }

        print(f"{platform_report}\n")

        return platform_report
