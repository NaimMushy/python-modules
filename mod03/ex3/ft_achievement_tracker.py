def get_rare_ach(players: dict) -> None:
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
    if len(rare_ach) > 0:
        print(f"Rare achievements (1 player): {rare_ach}\n")


def compare_players(players: dict, fst: str, scd: str) -> None:
    print(
        f"{fst.capitalize()} vs {scd.capitalize()} common: "
        f"{players[fst].intersection(players[scd])}"
    )
    print(
        f"{fst.capitalize()} unique: "
        f"{players[fst].difference(players[scd])}"
    )
    print(
        f"{scd.capitalize()} unique: "
        f"{players[scd].difference(players[fst])}"
    )


def tracker_system(players: dict) -> None:
    print("=== Achievement Tracker System ===\n")
    for pk, pv in players.items():
        print(f"Player {pk} achievements: {pv}")


def get_unique_ach(players: dict) -> None:
    u: set = set()
    for ach in players.values():
        u = u.union(ach)
    print(f"All unique achievements: {u}")
    print(f"Total unique achievements: {len(u)}\n")


def get_common_ach(players: dict) -> None:
    com: set = list(players.values())[0]
    for ach in players.values():
        com = com.intersection(ach)
    print(f"Common to all players: {com}")


def main() -> None:
    a: set = {'first_kill', 'level_10', 'treasure_hunter', 'speed_demon'}
    b: set = {'first_kill', 'level_10', 'boss_slayer', 'collector'}
    c: set = {
        'level_10',
        'treasure_hunter',
        'boss_slayer',
        'speed_demon',
        'perfectionist'
    }
    players: dict = {
        "alice": a,
        "bob": b,
        "charlie": c
    }
    tracker_system(players)
    print("\n=== Achievement Analytics ===")
    get_unique_ach(players)
    get_common_ach(players)
    get_rare_ach(players)
    compare_players(players, "alice", "bob")


if __name__ == "__main__":
    main()
