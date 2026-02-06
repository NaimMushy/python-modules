import sys


def main() -> None:
    print("=== Command Quest ===")
    if len(sys.argv) == 1:
        print("No arguments provided!")
    print(f"Program name: {sys.argv[0]}")
    if len(sys.argv) > 1:
        print(f"Arguments received: {len(sys.argv) - 1}")
        for av in range(1, len(sys.argv)):
            print(f"Argument {av}: {sys.argv[av]}")
    print(f"Total arguments: {len(sys.argv)}")


if __name__ == "__main__":
    main()
