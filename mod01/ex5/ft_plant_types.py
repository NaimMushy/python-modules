class Plant:
    def __init__(
        self,
        name: str,
        height: int,
        age: int,
        spec: str = "Plant"
    ) -> None:
        self.name = name.capitalize()
        self.set_height(height)
        self.set_age(age)
        self.spec = spec
        self.display_info()

    def set_height(self, new_height: int) -> None:
        if type(new_height) is int and new_height >= 0:
            self._height = new_height
        else:
            self._height = 0
            print(f"invalid value: height {new_height} [REJECTED]")

    def set_age(self, new_age: int) -> None:
        if type(new_age) is int and new_age >= 0 :
            self._age = new_age
        else:
            self._age = 0
            print(f"invalid value: age {new_age} [REJECTED]")

    def get_height(self) -> int:
        return self._height

    def get_age(self) -> int:
        return self._age

    def display_info(self) -> None:
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
    def __init__(
        self,
        name: str,
        height: int = 0,
        age: int = 0,
        color: str
    ) -> None:
        self.color = color
        super().__init__(name, height, age, "Flower")

    def bloom(self) -> None:
        self.set_height(self._height + 1)
        self.set_age(self._age + 1)
        print(f"{self.name} is blooming beautifully!")

    def display_info(self) -> None:
        super().display_info()
        print(f"{self.color} color")


class Tree(Plant):
    def __init__(
        self,
        name: str,
        height: int = 0,
        age: int = 0,
        trunk_diameter: int = 0
    ) -> None:
        self.set_trunk_dia(trunk_diameter)
        super().__init__(name, height, age, "Tree")

    def set_trunk_dia(self, new_trunk_dia: int) -> None:
        if type(new_trunk_dia) is int and new_trunk_dia >= 0:
            self._trunk_diameter = new_trunk_dia
        else:
            self._trunk_diameter = 0
            print(f"invalid value: {new_trunk_dia} trunk diameter [REJECTED]")

    def get_trunk_dia(self) -> int:
        return self._trunk_diameter

    def display_info(self) -> None:
        super().display_info()
        print(f"{self._trunk_diameter}cm diameter")

    def produce_shade(self, shade: int) -> None:
        print(f"{self.name} provides {shade} square meters of shade")


class Vegetable(Plant):
    def __init__(
        self,
        name: str,
        height: int = 0,
        age: int = 0,
        harvest_season: str,
        nutri_val: str = ""
    ) -> None:
        self.harvest_season = harvest_season
        super().__init__(name, height, age, "Vegetable")
        if nutri_val != "":
            self.set_nutri_val(nutri_val)

    def display_info(self) -> None:
        super().display_info()
        print(f"{self.harvest_season} harvest")

    def set_nutri_val(self, nutri_val) -> None:
        self.nutri_val = nutri_val
        print(f"{self.name} is rich in {self.nutri_val}")


if __name__ == "__main__":
    print("=== Garden Plant Types ===\n")
    flower1 = Flower("rose", 25, 30, "white")
    flower1.bloom()
    flower2 = Flower("lilac", 16, 4, "mauve")
    flower2.bloom()
    tree1 = Tree("oak", 500, 1825, 50)
    tree1.produce_shade(78)
    tree2 = Tree("maple", 482, 796, 44)
    tree2.produce_shade(56)
    veg1 = Vegetable("tomato", 80, 90, "summer", "vitamin C, vitamin A, potassium, calcium")
    veg2 = Vegetable("eggplant", 150, 60, "fall", "fiber, potassium, magnesium, iron")
