class Plant:
    """
    A class that represents a plant.
    """
    def __init__(self, name: str, height: int, age: int) -> None:
        """
        Initializes the plant's data.

        Parameters
        ----------
        name
            The plant's name.
        height
            The plant's height.
        age
            The plant's age.
        """
        self.name: str = name.capitalize()
        self.height: int = height
        self.age: int = age
        print(
            f"Created: {self.name} "
            f"({self.height}cm, {self.age} days)"
        )


def ft_plant_factory(plants: dict[str, [int, int]]) -> list[Plant]:
    """
    Creates a list of plants based on user input.
    """
    plant_list: list[Plant] = []
    print("=== Plant Factory Output ===")
    for plant, values in plants.items():
        plant_list.append(Plant(plant, values[0], values[1]))
    print(f"\nTotal plants created: {len(plant_list)}")
    return plant_list


def main() -> None:
    plants: dict[str, [int, int]] = {
        "Rose": (25, 30),
        "Oak": (200, 365),
        "Cactus": (5, 90),
        "Sunflower": (80, 45),
        "Fern": (15, 120)
    }
    ft_plant_factory(plants)


if __name__ == "__main__":
    main()
