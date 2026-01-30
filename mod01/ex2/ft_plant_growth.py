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
        self.days_old: int = age

    def grow(self) -> None:
        """
        Simulates the plant's growing.
        """
        self.height += 1

    def age(self) -> None:
        """
        Simulates the plant's aging.
        """
        self.days_old += 1

    def get_info(self) -> None:
        """
        Displays the plant's data.
        """
        print(
            f"{self.name}: {self.height}cm, {self.days_old} days old"
        )


def ft_plant_growth(plant: Plant) -> None:
    """
    Simulates growth for the given plant over the course of a week.

    Parameters
    ----------
    plant
        The plant to grow for a week.
    """
    initial_growth: int = plant.height
    for i in range(1, 8):
        if i == 1 or i == 7:
            print(f"=== Day {i} ===")
            plant.get_info()
        if i < 7:
            plant.grow()
            plant.age()
    end_growth: int = plant.height
    print(f"Growth this week: +{end_growth - initial_growth}cm\n")


def main() -> None:
    ft_plant_growth(Plant("rose", 25, 30))
    ft_plant_growth(Plant("petunia", 10, 6))
    ft_plant_growth(Plant("rhododendron", 40, 9))


if __name__ == "__main__":
    main()
