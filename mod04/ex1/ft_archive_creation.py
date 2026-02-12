from typing import TextIO


def inscribe_entry(filename: str, entries: list[str]) -> None:
    try:
        file: TextIO = open(filename, "w")
    except (FileNotFoundError, PermissionError) as err:
        print(f"ERROR: {err}")
    else:
        for entry in range(len(entries)):
            entries[entry] = (
                f"--- [ENTRY 00{entry + 1}] "
                + entries[entry]
                + " ---"
            )
            file.write(entries[entry])
            print(entries[entry])
        file.close()


def main() -> None:
    print("=== CYBER ARCHIVES - PRESERVATION SYSTEM ===\n")

    filename: str = "new_discovery.txt"
    print(f"Initializing new storage unit: {filename}")

    entries: list[str] = [
        "New quantum algorithm discovered",
        "Efficiency increased by 347%",
        "Archived by Data Archivist Trainee"
    ]
    print("Storage unit created successfully...\n")
    print("Inscribing preservation data...")

    inscribe_entry(filename, entries)

    print("\nData inscription complete - Storage unit sealed")
    print(f"Archive '{filename}' ready for long-term preservation")


if __name__ == "__main__":
    main()
