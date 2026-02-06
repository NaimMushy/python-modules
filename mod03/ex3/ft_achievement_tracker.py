def achievement_rarity(players: dict[str, set]) -> dict[str, set]:
    first: bool = True
    for ach in players.values():

        if first:
            all_ach: set = ach
            rare_ach: set = ach
            common_ach: set = ach
            first = False

        else:
            rare_ach = (rare_ach - ach).union((ach - all_ach))
            all_ach = all_ach.union(ach)
            common_ach = common_ach.intersection(ach)

    return {
        "unique": all_ach,
        "common": common_ach,
        "rare": rare_ach
    }


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


def tracker_system(players: dict[str, set]) -> None:
    print("=== Achievement Tracker System ===\n")

    for name, ach in players.items():
        print(f"Player {name} achievements: {ach}")


def achievement_analytics(players: dict[str, set]) -> None:
    print("\n=== Achievement Analytics ===")

    rarity: dict[str, set] = achievement_rarity(players)
    print(
        f"All unique achievements: {rarity['unique']}\n"
        f"Total unique achievements: {len(rarity['unique'])}\n"
    )
    print(f"Common to all players: {rarity['common']}")
    print(f"Rare achievements (1 player): {rarity['rare']}\n")


def main() -> None:
    players: dict[str, set] = {
        "alice": {'first_kill', 'level_10', 'treasure_hunter', 'speed_demon'},
        "bob": {'first_kill', 'level_10', 'boss_slayer', 'collector'},
        "charlie": {
            'level_10',
            'treasure_hunter',
            'boss_slayer',
            'speed_demon',
            'perfectionist'
        }
    }

    tracker_system(players)
    achievement_analytics(players)
    compare_players(players, "alice", "bob")


if __name__ == "__main__":
    main()
