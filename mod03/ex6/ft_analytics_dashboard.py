class Player:
    def __init__(
        self,
        name: str,
        score: int,
        status: str,
        achievements: set,
        regions: set
    ) -> None:
        self.name: str = name
        self.score: int = score
        self.status: str = status
        self.achievements: set = achievements
        self.regions: set = regions


def create_default_players() -> list[Player]:
    a: Player = Player(
        "alice",
        2300,
        "active",
        {'first_kill', 'speed_demon', 'level_10'},
        {'north', 'east'}
        )
    b: Player = Player(
        "bob",
        1800,
        "active",
        {'first_kill', 'speed_demon', 'boss_slayer', 'perfectionist'},
        {'north', 'west'}
        )
    c: Player = Player(
        "charlie",
        4444,
        "active",
        {'first_kill', 'speed_demon', 'collector',
         'level_10', 'boss_slayer', 'trash_digger'},
        {'west'}
        )
    d: Player = Player(
        "diana",
        3670,
        "inactive",
        {'speed_demon', 'level_10', 'perfectionist'},
        {'east'}
        )
    return [a, b, c, d]


def lst_comp(players: list[Player]) -> None:
    print("=== List Comprehension Examples ===")
    high_scorers: list[str] = [pl.name for pl in players if pl.score > 2000]
    print(f"High_scorers (>2000): {high_scorers}")
    doubled_scores: list[int] = [pl.score * 2 for pl in players]
    print(f"Scores doubled: {doubled_scores}")
    active_pl: list[str] = [pl.name for pl in players if pl.status == "active"]
    print(f"Active players: {active_pl}\n")


def dict_comp(players: list[Player]) -> None:
    print("=== Dict Comprehension Examples ===")
    pl_scores: dict[str, int] = {pl.name: pl.score for pl in players}
    print(f"Player scores: {pl_scores}")
    score_cat: dict[str, int] = {}
    score_cat["high"] = sum(1 for pl in players if pl.score >= 4000)
    score_cat["medium"] = sum(
        1 for pl in players if pl.score >= 2000 and pl.score < 4000
    )
    score_cat["low"] = sum(1 for pl in players if pl.score < 2000)
    print(f"Score categories: {score_cat}")
    ach_count: dict[str, int] = {
        pl.name: len(pl.achievements)
        for pl in players
    }
    print(f"Achievement counts: {ach_count}\n")


def set_comp(players: list[Player]) -> set:
    print("=== Set Comprehension Examples ===")
    unique_pl: set = {pl.name for pl in players}
    print(f"Unique players: {unique_pl}")
    all_ach: set = set.union(*(pl.achievements for pl in players))
    common_ach: set = set.union(*(
        players[pl].achievements.intersection(players[index].achievements)
        for pl in range(len(players) - 2)
        for index in range(pl, len(players) - 1)
    ))
    unique_ach: set = all_ach.difference(common_ach)
    print(f"Unique achievements: {unique_ach}")
    act_regions: set = set().union(*(pl.regions for pl in players))
    print(f"Active regions: {act_regions}\n")
    return unique_ach


def combined_analysis(players: list[Player], unique_ach: set) -> None:
    print("=== Combined Analysis ===")
    print(f"Total players: {len(players)}")
    print(f"Total unique achievements: {len(unique_ach)}")
    scores: list[int] = {pl.score for pl in players}
    avg_score: int = sum(pl.score for pl in players)
    print(f"Average score: {round(avg_score / len(scores), 1)}")
    top_perf: Player = [pl for pl in players if pl.score == max(scores)][0]
    print(
        f"Top performer: {top_perf.name} "
        f"({top_perf.score}, {len(top_perf.achievements)} achievements)\n"
    )


def main() -> None:
    print("=== Game Analysis Dashboard ===\n")
    players: list[Player] = create_default_players()
    lst_comp(players)
    dict_comp(players)
    unique_ach: set = set_comp(players)
    combined_analysis(players, unique_ach)


if __name__ == "__main__":
    main()
