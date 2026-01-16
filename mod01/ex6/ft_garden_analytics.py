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
            the plant's name
        height
            the plant's height
        age
            the plant's age
        spec
            the plant's type
        """
        self.name = name.capitalize()
        self.height = height
        self.age = age
        self.spec = spec

    def grow(self, growth: int) -> None:
        """
        Simulates growth for a plant.

        Parameters
        ----------
        growth
            how much the plant should grow
        """
        print(f"{self.name} grew {growth}cm")
        self.height += growth

    def display_info(self) -> None:
        """
        Displays the plant's data.
        """
        if self.spec != "regular":
            print(f"- {self.name}: {self.height}cm, ", end='')
        else:
            print(f"- {self.name}: {self.height}cm")


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
            the flower's name
        height
            the flower's height
        age
            the flower's age
        color
            the flower's color
        spec
            the plant's type
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
            the prize flower's name
        height
            the prize flower's height
        age
            the prize flower's age
        color
            the prize flower's color
        prize_points
            the flower's number of prize points
        spec
            the plant's type
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
            the garden's owner
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
            the new plant to add
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
            the plant's type
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
        the garden network
    garden_helper
        a GardenStats helper
    """

    gardens: list[Garden] = []

    class GardenStats:
        """
        [TODO:description]
        """
        @staticmethod
        def display_stats(garden: Garden) -> None:
            """
            Display the garden's stats.

            Parameters
            ----------
            garden
                a Garden
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
        def all_gardens_info(gardens: list[Garden]):
            """
            Displays the data of every garden in the garden network.

            Parameters
            ----------
            gardens
                the garden network
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
    def create_garden_network(cls: GardenManager) -> None:
        """
        Creates the garden network.

        Parameters
        ----------
        cls
            the GardenManager class
        """
        cls.gardens = []

    @classmethod
    def add_garden(cls: GardenManager, new_garden: Garden) -> None:
        """
        Adds a garden to the garden network managed.

        Parameters
        ----------
        cls
            the GardenManager class
        new_garden
            the new garden to add
        """
        cls.gardens.append(new_garden)
