class NameError(Exception):
    pass


def water_plants(plant_list: list[str]) -> None:
    print("Opening watering system")
    err: bool = False
    try:
        for plant in plant_list:
            if isinstance(plant, str):
                print(f"Watering {plant}")
            else:
                err = True
                raise NameError(
                    f"NameError: Cannot water {plant} - Invalid plant!"
                )
    except NameError as ne:
        print(ne)
    finally:
        print("Closing watering system (cleanup)\n")
        if not err:
            print("Watering completed without issues!")


def test_watering_system() -> None:
    print("=== Garden Watering System ===")
    print("\nTesting normal watering...")
    water_plants(["tomato", "lettuce", "carrots"])
    print("\nTesting watering with invalid plants...")
    water_plants(["eggplant", 123, "cucumber"])
    water_plants(["lilac", "gardenia", None])


def main() -> None:
    test_watering_system()


if __name__ == "__main__":
    main()
