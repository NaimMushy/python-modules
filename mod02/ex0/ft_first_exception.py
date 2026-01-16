def check_temperature(temp_str: str) -> int:
    """
    Verifies and indicates whether or not the temperature is valid/correct.

    Parameters
    ----------
    temp_str
        The temperature to check.

    Returns
    -------
    int
        The temperature if valid, and 0 otherwise.
    """
    try:
        temp: int = int(temp_str)
    except ValueError:
        print(f"error: '{temp_str}' is not a valid number\n")
        return (0)
    else:
        if temp < 0:
            print(f"temperature {temp} is too cold for plants (min 0°C)\n")
            return (0)
        elif temp > 40:
            print(f"temperature {temp} is too hot for plants (max 40°C)\n")
            return (0)
        else:
            print(f"temperature {temp}°C is perfect for plants!\n")
            return (temp)


def test_temperature_input() -> None:
    """
    Tests the check_temperature function.
    """
    temp_str: str = input("enter a test temperature: ")
    while temp_str != "stop":
        print(f"testing temperature: {temp_str}\n")
        check_temperature(temp_str)
        temp_str = input("enter a test temperature: ")
    print("all tests completed: program didn't crash!\n")


def main() -> None:
    test_temperature_input()


if __name__ == "__main__":
    main()
