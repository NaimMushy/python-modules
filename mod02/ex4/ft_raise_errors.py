MIN_WATER_LVL = 1
MAX_WATER_LVL = 10
MIN_SUN_H = 2
MAX_SUN_H = 12


def check_plant_health(
    plant_name: str,
    water_level: int,
    sunlight_hours: int
) -> None:
    """
    Checks the health of a plant.

    Parameters
    ----------
    plant_name
        the plant's name
    water_level
        the plant's water level
    sunlight_hours
        the plant's sunlight hours

    Raises
    ------
    ValueError:
        raised if the plant's name is empty
    ValueError:
        raised if the water level is inadequate (too low or too high)
    ValueError:
        raised if the sunlight hours are inadequate (too low or too high)
    """
    try:
        if plant_name == "":
            raise ValueError("ValueError: plant name cannot be empty!")
        if water_level < MIN_WATER_LVL:
            raise ValueError(
                f"ValueError: water level {water_level} "
                f"is too low (min {MIN_WATER_LVL})"
            )
        if water_level > MAX_WATER_LVL:
            raise ValueError(
                f"ValueError: water level {water_level} "
                f"is too high (max {MAX_WATER_LVL})"
            )
        if sunlight_hours < MIN_SUN_H:
            raise ValueError(
                f"ValueError: sunlight hours {sunlight_hours} "
                f"is too low (min {MIN_SUN_H})"
            )
        if sunlight_hours > MAX_SUN_H:
            raise ValueError(
                f"ValueError: sunlight hours {sunlight_hours} "
                f"is too high (max {MAX_SUN_H})"
            )
    except ValueError as ve:
        print(ve)
    else:
        print(f"plant {plant_name} is healthy!\n")


def test_plant_checks() -> None:
    """
    Tests the health of multiple plants with different data.
    """
    print("=== Garden Plant Health Checker ===\n")
    print("testing good values...")
    check_plant_health("eggplant", 4, 9)
    print("testing empty plant name...")
    check_plant_health("", 4, 9)
    print("testing bad water level...")
    check_plant_health("eggplant", 16, 9)
    print("testing bad water level...")
    check_plant_health("eggplant", 0, 9)
    print("testing bad sunlight hours...")
    check_plant_health("eggplant", 4, 17)
    print("testing bad sunlight hours...")
    check_plant_health("eggplant", 4, 1)
    print("all error raising tests completed!\n")


def main() -> None:
    test_plant_checks()


if __name__ == "__main__":
    main()
