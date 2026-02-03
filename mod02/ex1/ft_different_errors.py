def garden_operations(error_type: str) -> None:
    if error_type == "ve":
        int("abc")
    if error_type == "zde":
        16 / 0
    if error_type == "fnfe":
        with open("inexistant.txt"):
            pass
    if error_type == "ke":
        fav_tigercub_songs = {
            1: "The Dark Below",
            2: "Beating on my Heart",
            3: "It's Only Love"
        }
        fav_tigercub_songs[4]


def test_error_types() -> None:
    print("=== Garden Error Types Demo ===\n")
    print("Testing ValueError...")
    try:
        garden_operations("ve")
    except ValueError:
        print("Caught ValueError: Invalid literal for int()\n")
    print("Testing ZeroDivisionError...")
    try:
        garden_operations("zde")
    except ZeroDivisionError:
        print("Caught ZeroDivisionError: Division by zero\n")
    print("Testing FileNotFoundError...")
    try:
        garden_operations("fnfe")
    except FileNotFoundError:
        print("Caught FileNotFoundError: No such file 'inexistant.txt'\n")
    print("testing KeyError...")
    try:
        garden_operations("ke")
    except KeyError:
        print("Caught KeyError: Missing favorite song\n")
    print("Testing multiple errors together...")
    try:
        garden_operations("ve")
        garden_operations("zde")
        garden_operations("fnfe")
        garden_operations("ke")
    except (ValueError, ZeroDivisionError, FileNotFoundError, KeyError):
        print("Caught an error, but program continues!\n")
    print("All error types tested successfully!\n")


def main() -> None:
    test_error_types()


if __name__ == "__main__":
    main()
