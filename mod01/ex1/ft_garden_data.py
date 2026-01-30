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

    def display_info(self) -> None:
        """
        Displays the plant's data.
        """
        print(f"{self.name}: {self.height}cm, {self.age} days old")


def ft_garden_data() -> None:
    """
    Displays plant data for each plant in the garden.
    """
    plants: list[Plant] = []
    plants.append(Plant("Lilac", 24, 666))
    plants.append(Plant("Eggplant", 285, 44))
    plants.append(Plant("Bird of Paradise", 16, 4))
    print("=== Garden Plant Registry ===")
    for plant in plants:
        plant.display_info()


def main() -> None:
    ft_garden_data()


if __name__ == "__main__":
    main()
