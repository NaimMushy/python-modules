from typing import TextIO


def main() -> None:
    print("=== CYBER ARCHIVES - DATA RECOVERY SYSTEM ===\n")

    try:
        print("Accessing storage vault: ancient_fragment.txt")
        file: TextIO = open("ancient_fragment.txt")

    except (FileNotFoundError, PermissionError):
        print("ERROR: Storage vault not found")

    else:
        print("Connection established...\n")

        print("< RECOVERED DATA >")
        print(file.read())
        file.close()

    finally:
        print("\nData recovery complete - Storage unit disconnected")


if __name__ == "__main__":
    main()
