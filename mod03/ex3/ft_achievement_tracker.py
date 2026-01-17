def get_rare(players: dict) -> set:
    """
    Returns a set containing all the rare achievements.

    Parameters
    ----------
    players
        A dictionary containing the players' names and achievements.

    Returns
    -------
    set
        A set of rare achievements.
    """
    rare_ach: set = set({})
    all_ach: list[set] = list(players.values())
    for loop in range(len(all_ach)):
        temp_set: set = all_ach[0]
        for i in range(1, len(all_ach)):
            temp_set = temp_set.difference(all_ach[i])
        if len(temp_set) > 0:
            rare_ach = rare_ach.union(temp_set)
        fst: set = all_ach[0]
        all_ach = all_ach[1:]
        all_ach.append(fst)
    return (rare_ach)


def compare_players(players: dict, fst: str, scd: str) -> None:
    """
    Compares the achievements of the two players given as parameters.

    Parameters
    ----------
    players
        A dictionary containing the players' names and achievements.
    fst
        The name of the first player to compare.
    scd
        The name of the second player to compare.
    """
    print(f"{fst} vs {scd} common: {players[fst].intersection(players[scd])}")
    print(f"{fst} unique: {players[fst].difference(players[scd])}")
    print(f"{scd} unique: {players[scd].difference(players[fst])}")


def main() -> None:
    """
    Tracks and analyzes the achievements of multiple players.
    """
    a: set = {'first_kill', 'level_10', 'treasure_hunter', 'speed_demon'}
    b: set = {'first_kill', 'level_10', 'boss_slayer', 'collector'}
    c: set = {'level_10', 'treasure_hunter', 'boss_slayer', 'speed_demon', 'perfectionist'}
    players: dict = {
        "alice": a,
        "bob": b,
        "charlie": c
        }
    print("=== Achievement Tracker System ===\n")
    for pk, pv in players.items():
        print(f"player {pk} achievements: {pv}")
    print("\n=== Achievement Analytics ===")
    u: set = (a.union(b)).union(c)
    print(f"all unique achievements: {u}")
    print(f"total unique achievements: {len(u)}\n")
    com: set = (a.intersection(b)).intersection(c)
    print(f"common to all players: {com}")
    rare: set = get_rare(players)
    if len(rare) > 0:
        print(f"rare achievements (1 player): {rare}")
    compare_players(players, "alice", "bob")


if __name__ == "__main__":
    main()
