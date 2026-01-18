class Plant:
    """
    A class that represents a plant.
    """
    def __init__(
        self,
        name: str,
        height: int,
        age: int,
        spec: str = "Plant"
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
        spec
            The plant's type.
        """
        self.name = name.capitalize()
        self.set_height(height)
        self.set_age(age)
        self.spec = spec
        self.display_info()

    def set_height(self, new_height: int) -> None:
        """
        Verifies and updates the plant's height.

        Parameters
        ----------
        new_height
            The plant's new height.
        """
        if type(new_height) is int and new_height >= 0:
            self._height = new_height
        else:
            self._height = 0
            print(f"invalid value: height {new_height} [REJECTED]")

    def set_age(self, new_age: int) -> None:
        """
        Verifies and updates the plant's age.

        Parameters
        ----------
        new_age
            The plant's new age.
        """
        if type(new_age) is int and new_age >= 0:
            self._age = new_age
        else:
            self._age = 0
            print(f"invalid value: age {new_age} [REJECTED]")

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
        if self.spec != "Plant":
            print(
                f"{self.name} ({self.spec}): "
                f"{self._height}cm, {self._age} days, ", end=''
            )
        else:
            print(
                f"{self.name} ({self.spec}): "
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
        self.color = color
        super().__init__(name, height, age, "Flower")

    def bloom(self) -> None:
        """
        Simulates the flower's blooming.
        """
        self.set_height(self._height + 1)
        self.set_age(self._age + 1)
        print(f"{self.name} is blooming beautifully!")

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
        self.set_trunk_dia(trunk_diameter)
        super().__init__(name, height, age, "Tree")

    def set_trunk_dia(self, new_trunk_dia: int) -> None:
        """
        Verifies and updates the tree's trunk diameter.

        Parameters
        ----------
        new_trunk_dia
            The tree trunk's new diameter.
        """
        if type(new_trunk_dia) is int and new_trunk_dia >= 0:
            self._trunk_diameter = new_trunk_dia
        else:
            self._trunk_diameter = 0
            print(f"invalid value: {new_trunk_dia} trunk diameter [REJECTED]")

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

    def produce_shade(self, shade: int) -> None:
        """
        Displays a message indicating the shade produced by the tree.

        Parameters
        ----------
        shade
            The shade produced by the tree.
        """
        print(f"{self.name} provides {shade} square meters of shade")


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
        nutri_val: str = ""
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
        self.harvest_season = harvest_season
        super().__init__(name, height, age, "Vegetable")
        if nutri_val != "":
            self.set_nutri_val(nutri_val)

    def display_info(self) -> None:
        """
        Displays the vegetable's data.
        """
        super().display_info()
        print(f"{self.harvest_season} harvest")

    def set_nutri_val(self, nutri_val: str) -> None:
        """
        Updates the vegetable's nutritional value.

        Parameters
        ----------
        nutri_val
            The vegetable's nutritional value.
        """
        self.nutri_val = nutri_val
        print(f"{self.name} is rich in {self.nutri_val}")


def main() -> None:
    print("=== Garden Plant Types ===\n")
    flower1 = Flower("rose", 25, 30, "white")
    flower1.bloom()
    flower2 = Flower("lilac", 16, 4, "mauve")
    flower2.bloom()
    tree1 = Tree("oak", 500, 1825, 50)
    tree1.produce_shade(78)
    tree2 = Tree("maple", 482, 796, 44)
    tree2.produce_shade(56)
    veg1 = Vegetable("tomato", 80, 90, "summer")
    veg1.set_nutri_val("vitamin C, vitamin A, potassium, calcium")
    veg2 = Vegetable("eggplant", 150, 60, "fall")
    veg2.set_nutri_val("fiber, potassium, magnesium, iron")


if __name__ == "__main__":
    main()
