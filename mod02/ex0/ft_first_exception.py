def check_temperature(temp_str: str)->int:
    try:
        temp: int = int(temp_str)
    except ValueError:
        print(f"error: '{temp_str}' is not a valid number\n")
    else:
        if temp < 0:
            print(f"temperature {temp} is too cold for plants (min 0°C)\n")
        elif temp > 40:
            print(f"temperature {temp} is too hot for plants (max 40°C)\n")
        else:
            print(f"temperature {temp}°C is perfect for plants!\n")
            return (temp)


def test_temperature_input()->None:
    temp_str: str = input("enter a test temperature: ")
    while temp_str != "stop":
        print(f"testing temperature: {temp_str}\n")
        check_temperature(temp_str)
        temp_str = input("enter a test temperature: ")
    print("all tests completed: program didn't crash!\n")


if __name__ == "__main__":
    test_temperature_input()
