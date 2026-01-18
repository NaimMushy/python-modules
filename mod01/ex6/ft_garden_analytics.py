class Plant:
    """
    A class that represents a plant.
    """
    def __init__(
        self,
        name: str,
        height: int,
        age: int,
        spec: str = "regular"
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

    def set_height(self, new_height: int) -> None:
        """
        Verifies and updates the plant's height.

        Parameters
        ----------
        new_height
            The plant's new height.
        """
        if new_height >= 0:
            self._height = new_height
        else:
            self._height = 0
            print(
                f"error: height {new_height} for {self.name} "
                f"- invalid [REJECTED]"
            )

    def set_age(self, new_age: int) -> None:
        """
        Verifies and updates the plant's age.

        Parameters
        ----------
        new_age
            The plant's new age.
        """
        if new_age >= 0:
            self._age = new_age
        else:
            self._age = 0
            print(
                f"error: age {new_age} for {self.name} "
                f"- invalid [REJECTED]"
            )

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
            The plant's age
        """
        return self._age

    def grow(self, growth: int) -> None:
        """
        Simulates growth for a plant.

        Parameters
        ----------
        growth
            The plant's growth spurt.
        """
        print(f"{self.name} grew {growth}cm")
        self._height += growth

    def display_info(self) -> None:
        """
        Displays the plant's data.
        """
        if self.spec != "regular":
            print(f"- {self.name}: {self._height}cm, ", end='')
        else:
            print(f"- {self.name}: {self._height}cm")


class FloweringPlant(Plant):
    """
    A class that represents a flower.
    """
    def __init__(
        self,
        name: str,
        height: int,
        age: int,
        color: str,
        spec: str = "flowering"
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
        spec
            The plant's type.
        """
        super().__init__(name, height, age, spec)
        self.color = color
        self.bloom_state = "not in bloom"

    def bloom(self) -> None:
        """
        Simulates blooming for a flower.
        """
        self.bloom_state = "blooming"

    def display_info(self) -> None:
        """
        Displays the flower's data.
        """
        super().display_info()
        if self.spec != "flowering":
            print(f"{self.color} flowers ({self.bloom_state}), ", end='')
        else:
            print(f"{self.color} flowers ({self.bloom_state})")


class PrizeFlower(FloweringPlant):
    """
    A class that represents a prize flower.
    """
    def __init__(
        self,
        name: str,
        height: int,
        age: int,
        color: str,
        prize_points: int,
        spec: str = "prize"
    ) -> None:
        """
        Initializes the prize flower's data.

        Parameters
        ----------
        name
            The prize flower's name.
        height
            The prize flower's height.
        age
            The prize flower's age.
        color
            The prize flower's color.
        prize_points
            The flower's number of prize points.
        spec
            The plant's type.
        """
        super().__init__(name, height, age, color, spec)
        self.prize_points = prize_points

    def display_info(self) -> None:
        """
        Display the prize flower's data.
        """
        super().display_info()
        print(f"prize points: {self.prize_points}")


class Garden:
    """
    A class that represents a garden.
    """
    def __init__(self, owner: str) -> None:
        """
        Initializes the garden's data.

        Parameters
        ----------
        owner
            The garden's owner.
        """
        self.owner = owner
        self.plants: list[Plant] = []
        self.size: int = 0
        self.total_growth: int = 0
        self.regular_plants: int = 0
        self.flowering_plants: int = 0
        self.prize_plants: int = 0
        self.score: int = 0

    def add_plant(self, plant: Plant) -> None:
        """
        Adds a plant to the garden.

        Parameters
        ----------
        plant
            The new plant to add.
        """
        self.plants.append(plant)
        self.size += 1
        self.change_collections(plant.spec)
        print(f"Added {plant.name} to {self.owner}'s garden")

    def grow_all(self) -> None:
        """
        Simulates growth for all plants in the garden.
        """
        print(f"{self.owner} is helping all plants grow...")
        for plant in self.plants:
            plant.grow(1)
            self.total_growth += 1

    def change_collections(self, spec: str) -> None:
        """
        Modifies the garden's collections of plants based on types.

        Parameters
        ----------
        spec
            The plant's type.
        """
        if spec == "regular":
            self.regular_plants += 1
            self.score += 5
        elif spec == "flowering":
            self.flowering_plants += 1
            self.score += 10
        else:
            self.prize_plants += 1
            self.score += 20


class GardenManager:
    """
    A class that represents a garden manager.

    Attributes
    ----------
    gardens
        The garden network.
    garden_helper
        A GardenStats helper.
    """

    gardens: list[Garden] = []

    class GardenStats:
        """
        A class that displays the stats of a garden or a garden network.
        """
        @staticmethod
        def display_stats(garden: Garden) -> None:
            """
            Display the garden's stats.

            Parameters
            ----------
            garden
                A Garden.
            """
            print(f"=== {garden.owner}'s Garden Report ===\n")
            print("Plants in garden:")
            for plant in garden.plants:
                plant.display_info()
            print(
                f"Plants added: {garden.size}, "
                f"Total growth: {garden.total_growth}cm"
            )
            print(
                f"Plant types: {garden.regular_plants} regular, "
                f"{garden.flowering_plants} flowering, "
                f"{garden.prize_plants} prize flowers"
            )

        @staticmethod
        def all_gardens_info(gardens: list[Garden]) -> None:
            """
            Displays the data of every garden in the garden network.

            Parameters
            ----------
            gardens
                The garden network.
            """
            for grd in gardens:
                GardenManager.GardenStats.display_stats(grd)
            print("Garden scores - ", end='')
            for i in range(len(gardens)):
                if i < len(gardens) - 1:
                    print(
                        f"{gardens[i].owner}: "
                        f"{gardens[i].score}, ", end=''
                    )
                else:
                    print(f"{gardens[i].owner}: {gardens[i].score}")
            print(f"Total gardens managed: {len(gardens)}")

    garden_helper: GardenStats = GardenStats()

    @classmethod
    def create_garden_network(cls) -> None:
        """
        Creates the garden network.

        Parameters
        ----------
        cls
            The GardenManager class.
        """
        cls.gardens = []

    @classmethod
    def add_garden(cls, new_garden: Garden) -> None:
        """
        Adds a garden to the garden network managed.

        Parameters
        ----------
        cls
            The GardenManager class.
        new_garden
            The new garden to add.
        """
        cls.gardens.append(new_garden)
