import sys


def main() -> None:
    print("=== Command Quest ===")

    args: list[str] = sys.argv
    if len(args) == 1:
        print("No arguments provided!")

    print(f"Program name: {args[0]}")
    if len(args) > 1:
        print(f"Arguments received: {len(args) - 1}")
        for av in range(1, len(args)):
            print(f"Argument {av}: {args[av]}")

    print(f"Total arguments: {len(args)}")


if __name__ == "__main__":
    main()
