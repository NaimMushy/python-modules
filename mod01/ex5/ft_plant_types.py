class Plant:
    """
    A class that represents a plant.
    """
    def __init__(
        self,
        name: str,
        height: int,
        age: int,
    ) -> None:
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
        self.set_height(height)
        self.set_age(age)

    def set_height(self, new_height: int) -> None:
        """
        Verifies and updates the plant's height.

        Parameters
        ----------
        new_height
            The plant's new height.
        """
        if isinstance(new_height, int) and new_height >= 0:
            self._height: int = new_height
        else:
            print(f"Invalid value: height {new_height} [REJECTED]")

    def set_age(self, new_age: int) -> None:
        """
        Verifies and updates the plant's age.

        Parameters
        ----------
        new_age
            The plant's new age.
        """
        if isinstance(new_age, int) and new_age >= 0:
            self._age: int = new_age
        else:
            print(f"Invalid value: age {new_age} [REJECTED]")

    def get_height(self) -> int:
        """
        Returns
        -------
        int
            The plant's height.
        """
        return self._height

    def get_age(self) -> int:
        """
        Returns
        -------
        int
            The plant's age.
        """
        return self._age

    def display_info(self) -> None:
        """
        Displays the plant's data.
        """
        if isinstance(self, (Flower, Tree, Vegetable)):
            print(
                f"{self.name} ({self.__class__.__name__}): "
                f"{self._height}cm, {self._age} days, ", end=''
            )
        else:
            print(
                f"{self.name} ({self.__class__.__name__}): "
                f"{self._height}cm, {self._age} days"
            )


class Flower(Plant):
    """
    A class that represents a flower.
    """
    def __init__(
        self,
        name: str,
        height: int,
        age: int,
        color: str
    ) -> None:
        """
        Initializes the flower's data.

        Parameters
        ----------
        name
            The flower's name.
        height
            The flower's height.
        age
            The flower's age.
        color
            The flower's color.
        """
        super().__init__(name, height, age)
        self.color: str = color

    def bloom(self) -> None:
        """
        Simulates the flower's blooming.
        """
        self.set_height(self._height + 1)
        self.set_age(self._age + 1)
        print(f"{self.name} is blooming beautifully!\n")

    def display_info(self) -> None:
        """
        Displays the flower's data.
        """
        super().display_info()
        print(f"{self.color} color")


class Tree(Plant):
    """
    A class that represents a tree.
    """
    def __init__(
        self,
        name: str,
        height: int,
        age: int,
        trunk_diameter: int
    ) -> None:
        """
        Initializes the tree's data.

        Parameters
        ----------
        name
            The tree's name.
        height
            The tree's height.
        age
            The tree's age.
        trunk_diameter
            The tree's trunk diameter.
        """
        super().__init__(name, height, age)
        self.set_trunk_dia(trunk_diameter)

    def set_trunk_dia(self, new_trunk_dia: int) -> None:
        """
        Verifies and updates the tree's trunk diameter.

        Parameters
        ----------
        new_trunk_dia
            The tree trunk's new diameter.
        """
        if isinstance(new_trunk_dia, int) and new_trunk_dia >= 0:
            self._trunk_diameter: int = new_trunk_dia
        else:
            print(f"Invalid value: {new_trunk_dia} trunk diameter [REJECTED]")

    def get_trunk_dia(self) -> int:
        """
        Returns
        -------
        int
            The trunk's diameter.
        """
        return self._trunk_diameter

    def display_info(self) -> None:
        """
        Displays the tree's data.
        """
        super().display_info()
        print(f"{self._trunk_diameter}cm diameter")

    def produce_shade(self) -> None:
        """
        Calculates the shade produced by the tree
        and displays a message.
        """
        shade: int = \
            self.get_height() // 2 * self.get_trunk_dia() * 7 // 10000
        print(f"{self.name} provides {shade} square meters of shade\n")


class Vegetable(Plant):
    """
    A class that represents a vegetable.
    """
    def __init__(
        self,
        name: str,
        height: int,
        age: int,
        harvest_season: str,
        nutri_val: str
    ) -> None:
        """
        Initializes the vegetable's data.

        Parameters
        ----------
        name
            The vegetable's name.
        height
            The vegetable's height.
        age
            The vegetable's age.
        harvest_season
            The vegetable's harvest season.
        nutri_val
            The vegetable's nutritional value.
        """
        super().__init__(name, height, age)
        self.harvest_season: str = harvest_season
        self.nutri_val: str = nutri_val

    def display_info(self) -> None:
        """
        Displays the vegetable's data.
        """
        super().display_info()
        print(f"{self.harvest_season} harvest")
        print(f"{self.name} is rich in {self.nutri_val}\n")


def main() -> None:
    print("=== Garden Plant Types ===\n")
    flower1: Flower = Flower("hellebore", 25, 30, "white")
    flower1.display_info()
    flower1.bloom()
    flower2: Flower = Flower("lilac", 16, 4, "mauve")
    flower2.display_info()
    flower2.bloom()
    tree1: Tree = Tree("oak", 500, 1825, 50)
    tree1.display_info()
    tree1.produce_shade()
    tree2: Tree = Tree("maple", 482, 796, 44)
    tree2.display_info()
    tree2.produce_shade()
    veg1: Vegetable = Vegetable(
        "tomato",
        80,
        90,
        "summer",
        "vitamin C, vitamin A, potassium, calcium"
    )
    veg1.display_info()
    veg2: Vegetable = Vegetable(
        "eggplant",
        150,
        60,
        "fall",
        "fiber, potassium, magnesium, iron"
    )
    veg2.display_info()


if __name__ == "__main__":
    main()
