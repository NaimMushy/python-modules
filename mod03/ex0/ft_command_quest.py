import sys

def main() -> None:
    """
    Displays the arguments given from the command line.
    """
    print("=== Command Quest ===")
    if len(sys.argv) == 1:
        print("no arguments provided!")
    print(f"program name: {sys.argv[0]}")
    if len(sys.argv) > 1:
        print(f"arguments received: {len(sys.argv) - 1}")
        for av in range(1, len(sys.argv)):
            print(f"argument {av}: {sys.argv[av]}")
    print(f"total arguments: {len(sys.argv)}")


if __name__ == "__main__":
    main()
