def garden_operations(error_type: str) -> None:
    """
    Provokes an error based on error_type.

    Parameters
    ----------
    error_type
        the type of the error:
        (ValueError, ZeroDivisionError, FileNotFoundError, KeyError)
    """
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
    """
    Tests the different error types.
    """
    print("=== Garden Error Types Demo ===\n")
    print("testing ValueError...")
    try:
        garden_operations("ve")
    except ValueError:
        print("caught ValueError: invalid literal for int()\n")
    print("testing ZeroDivisionError...")
    try:
        garden_operations("zde")
    except ZeroDivisionError:
        print("caught ZeroDivisionError: division by zero\n")
    print("testing FileNotFoundError...")
    try:
        garden_operations("fnfe")
    except FileNotFoundError:
        print("caught FileNotFoundError: No such file 'inexistant.txt'\n")
    print("testing KeyError...")
    try:
        garden_operations("ke")
    except KeyError:
        print("caught KeyError: missing favorite song\n")
    print("testing multiple errors together...")
    try:
        garden_operations("ve")
        garden_operations("zde")
        garden_operations("fnfe")
        garden_operations("ke")
    except (ValueError, ZeroDivisionError, FileNotFoundError, KeyError):
        print("caught an error, but program continues!\n")
    print("all error types tested successfully!\n")


def main() -> None:
    test_error_types()


if __name__ == "__main__":
    main()
