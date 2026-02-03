def check_temperature(temp_str: str) -> int:
    try:
        temp: int = int(temp_str)
    except ValueError:
        print(f"Error: '{temp_str}' is not a valid number\n")
        return -1
    else:
        if temp < 0:
            print(f"Temperature {temp} is too cold for plants (min 0°C)\n")
            return -1
        elif temp > 40:
            print(f"Temperature {temp} is too hot for plants (max 40°C)\n")
            return -1
        else:
            print(f"Temperature {temp}°C is perfect for plants!\n")
            return temp


def test_temperature_input() -> None:
    print("=== Garden Temperature Checker ===\n")
    temp_str: str = input("Enter a test temperature: ")
    while temp_str != "stop":
        print(f"Testing temperature: {temp_str}\n")
        check_temperature(temp_str)
        temp_str = input("Enter a test temperature: ")
    print("All tests completed: Program didn't crash!\n")


def main() -> None:
    test_temperature_input()


if __name__ == "__main__":
    main()
