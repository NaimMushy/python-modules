class NameError(Exception):
    pass


def water_plants(plant_list: list[str]) -> None:
    print("opening watering system\n")
    try:
        for plant in plant_list:
            if type(plant) is str:
                print(f"watering {plant}")
            else:
                raise NameError(
                    f"NameError: cannot water {plant} - invalid plant!\n"
                )
    except NameError as ne:
        print(ne)
    finally:
        print("closing watering system (cleanup)\n")
        if type(plant) is str:
            print("watering completed without issues!\n")


def test_watering_system() -> None:
    print("=== Garden Watering System ===\n")
    print("Testing normal watering...")
    water_plants(["tomato", "lettuce", "carrots"])
    print("Testing watering with invalid plants...")
    water_plants(["eggplant", 123, "cucumber"])
    water_plants(["lilac", "gardenia", None])


if __name__ == "__main__":
    test_watering_system()
