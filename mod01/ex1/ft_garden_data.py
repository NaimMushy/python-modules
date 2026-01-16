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
        self.name = name
        self.height = height
        self.age = age

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
    plant1 = Plant("anneau de cinabre", 40075017000, 666)
    plant2 = Plant("baltrou", -10000000, 53)
    plant3 = Plant("trou qui pète", 1, 0)
    plants.append(plant1)
    plants.append(plant2)
    plants.append(plant3)
    print("=== Garden Plant Registry ===")
    for plant in plants:
        plant.display_info()


def main() -> None:
    ft_garden_data()


if __name__ == "__main__":
    main()
