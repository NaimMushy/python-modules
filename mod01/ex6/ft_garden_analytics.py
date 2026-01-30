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
        self.name: str = name.capitalize()
        self.set_height(height)
        self.set_age(age)
        self.spec: str = spec
        self._growth: int = 0

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
            print(
                f"Error: height {new_height} for {self.name} "
                f"- Invalid [REJECTED]"
            )

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
            print(
                f"Error: age {new_age} for {self.name} "
                f"- Invalid [REJECTED]"
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
            The plant's age.
        """
        return self._age

    def get_growth(self) -> int:
        """
        Returns
        -------
        int
            The plant's growth.
        """
        return self._growth

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
        self._growth += growth

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
        self.color: str = color
        self.bloom_state: str = "not in bloom"

    def bloom(self) -> None:
        """
        Simulates blooming for a flower.
        """
        if self.bloom_state == "blooming":
            print(f"{self.name} is already in bloom")
        else:
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
        self.prize_points: int = prize_points

    def display_info(self) -> None:
        """
        Display the prize flower's data.
        """
        super().display_info()
        print(f"Prize points: {self.prize_points}")


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
        self.owner: str = owner.capitalize()
        self.plants: list[Plant] = []
        print(f"Created {self.owner}'s Garden\n")

    def add_plant(self, plant: Plant) -> None:
        """
        Adds a plant to the garden.

        Parameters
        ----------
        plant
            The new plant to add.
        """
        self.plants.append(plant)
        print(f"Added {plant.name} to {self.owner}'s garden")

    def grow_all(self) -> None:
        """
        Simulates growth for all plants in the garden.
        """
        print(f"\n{self.owner} is helping all plants grow...")
        for plant in self.plants:
            plant.grow(1)

    def find_plant(self, plant_name: str) -> Plant | None:
        """
        Searches for a specific plant in the garden.

        Parameters
        ----------
        plant_name
            The plant to find in the garden.

        Returns
        -------
        Plant | None
            The Plant object if found, None otherwise.
        """
        for plant in self.plants:
            if plant.name == plant_name.capitalize():
                return plant
        return None


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
        A class that calculates the stats of a garden.
        """
        def grd_report(self, garden: Garden) -> dict:
            """
            Calculates the given garden's stats.

            Parameters
            ----------
            garden
                The garden for which to calculate stats.

            Returns
            -------
            dict
                The garden's stats.
            """
            stats: dict = {
                "plants_added": len(garden.plants),
                "total_growth": self.get_total_growth(garden),
                "plant_types": self.get_collection(garden),
            }
            return stats

        @staticmethod
        def get_total_growth(garden: Garden) -> int:
            """
            Calculates the total growth of the garden's plants.

            Parameters
            ----------
            garden
                The garden for which to calculate total plant growth.

            Returns
            -------
            int
                The garden's plants' total growth.
            """
            total_growth: int = 0
            for plant in garden.plants:
                total_growth += plant.get_growth()
            return total_growth

        def get_grd_score(self, garden: Garden) -> int:
            """
            Calculates the garden's total score
            based on collections and plant growth.

            Parameters
            ----------
            garden
                The garden for which to calculate score.

            Returns
            -------
            int
                The garden's score.
            """
            collection: dict[str, int] = self.get_collection(garden)
            score: int = (
                5 * collection["regular"]
            ) + (
                10 * collection["flowering"]
            ) + (
                20 * collection["prize"]
            )
            return score + self.get_total_growth(garden)

        @staticmethod
        def get_collection(garden: Garden) -> dict[str, int]:
            """
            Calculates the garden's plant collection based on types.

            Parameters
            ----------
            garden
                The garden for which to calculate plant collection.

            Returns
            -------
            dict[str, int]
                The garden's plant collection.
            """
            collection: dict[str, int] = {
                "regular": 0,
                "flowering": 0,
                "prize": 0
            }
            for plant in garden.plants:
                collection[plant.spec] += 1
            return collection

        @staticmethod
        def height_validation(gardens: list[Garden]) -> bool:
            """
            Calculates whether or not the gardens' plants in the network
            have reached a sufficient height.

            Parameters
            ----------
            gardens
                The network of gardens to test.

            Returns
            -------
            bool
                True if the plants are high enough, False otherwise.
            """
            total_size: int = 0
            for garden in gardens:
                for plant in garden.plants:
                    total_size += plant.get_height()
            if total_size < 200:
                return False
            else:
                return True

    garden_helper = GardenStats()

    @classmethod
    def create_garden_network(cls, gardens: dict[str, dict]) -> None:
        """
        Creates the garden network.

        Parameters
        ----------
        cls
            The GardenManager class.
        gardens
            The list of gardens to create and add to the network.
        """
        print("Creating Garden Network...\n")
        for grd_name, plants in gardens.items():
            cls.add_garden(grd_name, plants)

    @classmethod
    def add_garden(cls, grd_name: str, plants: dict[str, list]) -> None:
        """
        Creates and adds a garden to the garden network managed,
        then populates it with plants.

        Parameters
        ----------
        cls
            The GardenManager class.
        new_garden
            The new garden to add.
        plants
            The list of plants to populate the new garden with.
        """
        new_garden: Garden = Garden(grd_name)
        cls.gardens.append(new_garden)
        cls.populate_garden(new_garden, plants)

    @staticmethod
    def plant_factory(plants: dict[str, list]) -> list[Plant]:
        """
        Creates a list of plants based on the initializing values
        given as parameter.

        Parameters
        ----------
        plants
            The list of plants to create.

        Returns
        -------
        list[Plant]
            The list of created plants.
        """
        plant_list: list[Plant] = []
        for plant_type, plant_values in plants.items():
            if plant_type == "regular":
                plant_list.append(Plant(
                    plant_values[0],
                    plant_values[1],
                    plant_values[2]
                ))
            elif plant_type == "flowering":
                plant_list.append(FloweringPlant(
                    plant_values[0],
                    plant_values[1],
                    plant_values[2],
                    plant_values[3],
                ))
            elif plant_type == "prize":
                plant_list.append(PrizeFlower(
                    plant_values[0],
                    plant_values[1],
                    plant_values[2],
                    plant_values[3],
                    plant_values[4]
                ))
            else:
                print("Plant type unknown\n")
        return plant_list

    @classmethod
    def find_garden(cls, grd_name: str) -> Garden | None:
        """
        Searches for a specific garden in the network.

        Parameters
        ----------
        cls
            The GardenManager class.
        grd_name
            The name of the garden to find.

        Returns
        -------
        Garden | None
            The Garden object if found, and None otherwise.
        """
        for garden in cls.gardens:
            if garden.owner == grd_name.capitalize():
                return garden
        return None

    @classmethod
    def populate_garden(cls, garden: Garden, plants: dict[str, list]) -> None:
        """
        Populates the given garden with the given plants.

        Parameters
        ----------
        cls
            The GardenManager class.
        garden
            The garden to populate.
        plants
            The plants to populate the garden with.
        """
        plants_to_add: list[Plant] = cls.plant_factory(plants)
        if garden in cls.gardens:
            for plant in plants_to_add:
                cls.add_plant_to_grd(plant, garden)
        else:
            print(f"{garden.owner}'s Garden is not in the network.\n")

    @classmethod
    def add_plant_to_grd(cls, plant: Plant, garden: Garden) -> None:
        """
        Adds the given plant to the given garden.

        Parameters
        ----------
        cls
            The GardenManager class.
        plant
            The plant to add to the garden.
        garden
            The garden to add the plant to.
        """
        garden.add_plant(plant)

    @classmethod
    def grow_all_garden_plants(cls) -> None:
        """
        Grows every plant of 1cm in every garden of the network.

        Parameters
        ----------
        cls
            The GardenManager class.
        """
        for garden in cls.gardens:
            garden.grow_all()

    @classmethod
    def grow_one_plant(
        cls,
        garden_name: str,
        plant_growth: dict[str, int]
    ) -> None:
        """
        Grows the given plants with the given growth in the given garden.

        Parameters
        ----------
        cls
            The GardenManager class.
        garden_name
            The name of the garden in which the plants need to grow.
        plant_growth
            The name and growth value of the plants to grow.
        """
        garden: Garden | None = cls.find_garden(garden_name)
        if not garden:
            print(
                f"{garden_name.capitalize()}'s Garden "
                "is not in the network\n"
            )
        else:
            for plant_name, growth in plant_growth.items():
                plant: Plant | None = garden.find_plant(plant_name)
                if plant:
                    plant.grow(growth)
                else:
                    print(
                        f"Plant {plant_name.capitalize()} not found in "
                        f"{garden.owner}'s Garden\n"
                    )

    @classmethod
    def bloom_all(cls) -> None:
        """
        Makes every flower of every garden in the network bloom.

        Parameters
        ----------
        cls
            The GardenManager class.
        """
        for garden in cls.gardens:
            for plant in garden.plants:
                if isinstance(plant, (FloweringPlant, PrizeFlower)):
                    plant.bloom()

    @classmethod
    def bloom_flowers(cls, garden_name: str, flowers: list[str]) -> None:
        """
        Makes the given flowers of the given garden bloom.

        Parameters
        ----------
        cls
            The GardenManager class.
        garden_name
            The name of the garden in which the flowers need to bloom.
        flowers
            The name of the flowers to bloom.
        """
        garden: Garden | None = cls.find_garden(garden_name)
        if not garden:
            print(
                f"{garden_name.capitalize()}'s Garden "
                "is not in the network\n"
            )
        else:
            for flower_name in flowers:
                flower: Plant | None = garden.find_plant(flower_name)
                if not flower:
                    print(
                        f"Plant {flower_name.capitalize()} not found in "
                        f"{garden.owner}'s Garden\n"
                    )
                elif not isinstance(flower, (FloweringPlant, PrizeFlower)):
                    print(
                        f"{flower.name} "
                        "does not have the ability to bloom\n"
                    )
                else:
                    flower.bloom()

    @classmethod
    def display_grd_stats(cls) -> None:
        """
        Displays the statistics of every garden in the network.

        Parameters
        ----------
        cls
            The GardenManager class.
        """
        for garden in cls.gardens:
            stats: dict = cls.garden_helper.grd_report(garden)
            print(f"\n=== {garden.owner}'s Garden Report ===\n")
            print("Plants in garden:")
            for plant in garden.plants:
                plant.display_info()
            print(
                f"\nPlants added: {stats['plants_added']}, "
                f"Total growth: {stats['total_growth']}cm"
            )
            print(
                f"Plant types: {stats['plant_types']['regular']} regular, "
                f"{stats['plant_types']['flowering']} flowering, "
                f"{stats['plant_types']['prize']} prize flowers"
            )
        print(
            "\nHeight validation test: "
            f"{cls.garden_helper.height_validation(cls.gardens)}"
        )
        print("Garden scores - ", end="")
        for garden in cls.gardens:
            if garden != cls.gardens[-1]:
                print(
                    f"{garden.owner}: "
                    f"{cls.garden_helper.get_grd_score(garden)}, ", end=""
                )
            else:
                print(
                    f"{garden.owner}: "
                    f"{cls.garden_helper.get_grd_score(garden)}"
                )
        print(f"Total gardens managed: {len(cls.gardens)}")


def main() -> None:
    """
    Demonstrates how the Garden Manager works and its abilities.
    """
    print("=== Garden Management System Demo ===\n")
    grd_mngr: GardenManager = GardenManager()
    plant_list1: dict[str, list] = {
        "regular": ["oak tree", 100, 666],
        "flowering": ["lilac", 16, 44, "mauve"],
        "prize": ["hellebore", 24, 58, "white", 16]
    }
    plant_list2: dict[str, list] = {
        "regular": ["mushroom", 12, 57],
        "flowering": ["begonia", 56, 202, "red"],
        "prize": ["lily", 25, 88, "vanilla", 12]
    }
    grd_mngr.create_garden_network({"alice": plant_list1, "bob": plant_list2})
    grd_mngr.grow_all_garden_plants()
    grd_mngr.grow_one_plant("alice", {
        "lilac": 2,
        "hellebore": 4
    })
    grd_mngr.grow_one_plant("bob", {
        "mushroom": 3,
        "lily": 1,
        "cactus": 5
    })
    grd_mngr.grow_one_plant("charlie", {
        "lilac": 2,
        "hellebore": 4
    })
    grd_mngr.bloom_flowers("alice", ["lilac", "hellebore"])
    grd_mngr.bloom_all()
    grd_mngr.display_grd_stats()


if __name__ == "__main__":
    main()
