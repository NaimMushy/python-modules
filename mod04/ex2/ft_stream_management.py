import sys


def main() -> None:
    """
    Takes input from the user and diplays messages on the appropriate channels.
    """
    print("CYBER ARCHIVES - COMMUNICATION SYSTEM ===\n")
    arch_id: str = input("input stream active - enter archivist ID: ")
    status: str = input("input stream active - enter status report: ")
    print("\n")
    print(f"[standard] archive status from {arch_id}: {status}")
    print(
        "[alert] system diagnostic: communication channels verified",
        file=sys.stderr
    )
    print("[standard] data transmission complete")
    print("\nthree-channel communication test successful")


if __name__ == "__main__":
    main()
