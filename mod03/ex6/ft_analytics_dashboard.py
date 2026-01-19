class Player:
    """
    A class that represents a player.
    """
    def __init__(
        self,
        name: str,
        score: int,
        status: str,
        achievements: set,
        regions: set
    ) -> None:
        """
        Initializes the player's data.

        Parameters
        ----------
        name
            The player's name.
        score
            The player's score.
        status
            The player's status.
        achievements
            The player's achievements.
        regions
            The player's visited regions.
        """
        self.name: str = name
        self.score: int = score
        self.status: str = status
        self.achievements: set = achievements
        self.regions: set = regions


def create_default_players() -> list[Player]:
    """
    Creates a list containing the default players.

    Returns
    -------
    list[Player]
        The list of default players.
    """
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
    """
    Displays a demonstration of list comprehension.

    Parameters
    ----------
    players
        The list of players.
    """
    print("=== List Comprehension Examples ===")
    high_scorers: list[str] = [pl.name for pl in players if pl.score > 2000]
    print(f"high_scorers (>2000): {high_scorers}")
    doubled_scores: list[int] = [pl.score * 2 for pl in players]
    print(f"scores doubled: {doubled_scores}")
    active_pl: list[str] = [pl.name for pl in players if pl.status == "active"]
    print(f"active players: {active_pl}\n")


def dict_comp(players: list[Player]) -> None:
    """
    Displays a demonstration of dictionary comprehension.

    Parameters
    ----------
    players
        The list of players.        
    """
    print("=== Dict Comprehension Examples ===")
    pl_scores: dict[str, int] = {pl.name: pl.score for pl in players}
    print(f"player scores: {pl_scores}")
    score_cat: dict[str, int] = {}
    score_cat["high"] = sum(1 for pl in players if pl.score >= 4000)
    score_cat["medium"] = sum(
        1 for pl in players if pl.score >= 2000 and pl.score < 4000
    )
    score_cat["low"] = sum(1 for pl in players if pl.score < 2000)
    print(f"score categories: {score_cat}")
    ach_count: dict[str, int] = {
        pl.name: len(pl.achievements)
        for pl in players
    }
    print(f"achievement counts: {ach_count}\n")


def set_comp(players: list[Player]) -> set:
    """
    Displays a demonstration of set comprehension.

    Parameters
    ----------
    players
        The list of players.

    Returns
    -------
    set
        The set containing all the unique achievements.
    """
    print("=== Set Comprehension Examples ===")
    unique_pl: set = {pl.name for pl in players}
    print(f"unique players: {unique_pl}")
    all_ach: set = set.union(*(pl.achievements for pl in players))
    common_ach: set = set.union(*(
        players[pl].achievements.intersection(players[index].achievements)
        for pl in range(len(players) - 2)
        for index in range(pl, len(players) - 1)
    ))
    unique_ach: set = all_ach.difference(common_ach)
    print(f"unique achievements: {unique_ach}")
    act_regions: set = set().union(*(pl.regions for pl in players))
    print(f"active regions: {act_regions}\n")
    return unique_ach


def combined_analysis(players: list[Player], unique_ach: set) -> None:
    """
    Displays a analysis combining all three types of comprehension.

    Parameters
    ----------
    players
        The list of players.
    unique_ach
        The set containing all the unique achievements.
    """
    print("=== Combined Analysis ===")
    print(f"total players: {len(players)}")
    print(f"total unique achievements: {len(unique_ach)}")
    scores: list[int] = {pl.score for pl in players}
    avg_score: int = sum(pl.score for pl in players)
    print(f"average score: {round(avg_score / len(scores), 1)}")
    top_perf: Player = [pl for pl in players if pl.score == max(scores)][0]
    print(
        f"top performer: {top_perf.name} "
        f"({top_perf.score}, {len(top_perf.achievements)} achievements)\n"
    )


def main() -> None:
    """
    Displays demonstrations of different types of comprehensions.
    """
    print("=== Game Analysis Dashboard ===\n")
    players: list[Player] = create_default_players()
    lst_comp(players)
    dict_comp(players)
    unique_ach: set = set_comp(players)
    combined_analysis(players, unique_ach)


if __name__ == "__main__":
    main()
