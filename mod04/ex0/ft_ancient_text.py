def main() -> None:
    """
    Extracts and displays the recovered fragments from the ancient file.
    """
    print("=== CYBER ARCHIVES - DATA RECOVERY SYSTEM ===\n")
    try:
        print("accessing storage vault: ancient_fragment.txt")
        file = open("ancient_fragment.txt")
    except FileNotFoundError:
        print("error: storage vault not found")
    else:
        print("connection established...\n")
        print("<recovered data>")
        for fragment in file:
            print(f"{fragment}")

        print("\ndata recovery complete - storage unit disconnected")


if __name__ == "__main__":
    main()
