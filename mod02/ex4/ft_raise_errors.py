MIN_WATER_LVL = 1
MAX_WATER_LVL = 10
MIN_SUN_H = 2
MAX_SUN_H = 12


def check_plant_health(
    plant_name: str,
    water_level: int,
    sunlight_hours: int
) -> None:
    try:
        if not plant_name or plant_name == "":
            raise ValueError("ValueError: Plant name cannot be empty!")
        if water_level < MIN_WATER_LVL:
            raise ValueError(
                f"ValueError: Water level {water_level} "
                f"is too low (min {MIN_WATER_LVL})"
            )
        if water_level > MAX_WATER_LVL:
            raise ValueError(
                f"ValueError: Water level {water_level} "
                f"is too high (max {MAX_WATER_LVL})"
            )
        if sunlight_hours < MIN_SUN_H:
            raise ValueError(
                f"ValueError: Sunlight hours {sunlight_hours} "
                f"is too low (min {MIN_SUN_H})"
            )
        if sunlight_hours > MAX_SUN_H:
            raise ValueError(
                f"ValueError: Sunlight hours {sunlight_hours} "
                f"is too high (max {MAX_SUN_H})"
            )
    except ValueError as ve:
        print(ve)
    else:
        print(f"Plant {plant_name} is healthy!")


def test_plant_checks() -> None:
    print("=== Garden Plant Health Checker ===")
    print("\nTesting good values...")
    check_plant_health("eggplant", 4, 9)
    print("\nTesting empty plant name...")
    check_plant_health("", 4, 9)
    check_plant_health(None, 4, 9)
    print("\nTesting bad water level...")
    check_plant_health("eggplant", 16, 9)
    print("\nTesting bad water level...")
    check_plant_health("eggplant", 0, 9)
    print("\nTesting bad sunlight hours...")
    check_plant_health("eggplant", 4, 17)
    print("\nTesting bad sunlight hours...")
    check_plant_health("eggplant", 4, 1)
    print("\nAll error raising tests completed!")


def main() -> None:
    test_plant_checks()


if __name__ == "__main__":
    main()
