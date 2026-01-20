ENTRY_001: str = (
    "---- [entry 001] new quantum algorithm discovered, "
    "isn't that great? ----\n"
)
ENTRY_002: str = (
    "---- [entry 002] efficiency increased by 347% "
    "(we replaced the IA by humans) ----\n"
)
ENTRY_003: str = (
    "---- [entry 003] archived by data archivist trainee "
    "(i really hope i get a permanent job, times are hard "
    "dans la france de macron) ----\n"
)


def main() -> None:
    """
    Writes a few entries to a new file.
    """
    print("=== CYBER ARCHIVES - PRESERVATION SYSTEM ===\n")
    print("initializing new storage unit: new_discovery.txt")
    with open("new_discovery.txt", "w") as new:
        print("storage unit created successfully...\n")
        print("inscribing preservation data...")
        new.write(ENTRY_001)
        print(f"{ENTRY_001}")
        new.write(ENTRY_002)
        print(f"{ENTRY_002}")
        new.write(ENTRY_003)
        print(f"{ENTRY_003}")
    print("\ndata inscription complete - storage unit sealed")
    print("archive 'new_discovery.txt' ready for long-term preservation")


if __name__ == "__main__":
    main()
