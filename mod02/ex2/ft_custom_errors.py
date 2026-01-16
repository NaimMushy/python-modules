class Plant:
    """
    A class that represents a plant.
    """
    def __init__(self, name: str, state: str = "blooming") -> None:
        """
        Initializes the plant's data.

        Parameters
        ----------
        name
            the plant's name
        state
            the plant's state
        """
        self.name = name
        self.state = state

    def set_state(self, new_state: str) -> None:
        """
        Updates the plant's state.

        Parameters
        ----------
        new_state
            the plant's new state
        """
        self.state = new_state


class Garden:
    """
    A class that represents a garden.
    """
    def __init__(self) -> None:
        """
        Initializes the garden's data.
        """
        self.plants: list[Plant] = []
        self.tank_amount: int = 100

    def add_plant(self, new_plant: Plant) -> None:
        """
        Adds a plant to the garden.

        Parameters
        ----------
        new_plant
            the plant to add
        """
        self.plants.append(new_plant)

    def set_tank_amount(self, new_amount: int) -> None:
        """
        Updates the garden's tank amount.

        Parameters
        ----------
        new_amount
            the new amount of the garden's tank
        """
        self.tank_amount = new_amount


class GardenError(Exception):
    pass


class PlantError(GardenError):
    pass


class WaterError(GardenError):
    pass


def testing_plant_error(
    plants: list[Plant],
    error_type: str = "PlantError"
) -> None:
    """
    Checks for plant errors.

    Parameters
    ----------
    plants
        a list of plants
    error_type
        the type of the error:
        (GardenError or PlantError)

    Raises
    ------
    PlantError:
        raised if a plant is withering
    """
    err_count: int = 0
    for plant in plants:
        try:
            if plant.state == "withering":
                err_count += 1
                raise PlantError(
                    f"caught {error_type}: the {plant.name} is withering!\n"
                )
        except PlantError as pe:
            print(pe)
    if err_count == 0:
        print("all plants are blooming! :)\n")


def testing_water_error(
    tank_amount: int,
    error_type: str = "WaterError"
) -> None:
    """
    Checks for water errors.

    Parameters
    ----------
    tank_amount
        the garden's tank amount
    error_type
        the type of error:
        (GardenError or WaterError)

    Raises
    ------
    WaterError:
        raised if the tank amount is too low
    """
    try:
        if tank_amount < 30:
            raise WaterError(
                f"caught {error_type}: not enough water in the tank!\n"
            )
        else:
            print("there's enough water in the tank!\n")
    except WaterError as we:
        print(we)


def testing_garden_errors(garden: Garden) -> None:
    """
    Checks for garden errors.

    Parameters
    ----------
    garden
        the garden to check
    """
    testing_plant_error(garden.plants, "GardenError")
    testing_water_error(garden.tank_amount, "GardenError")


def main() -> None:
    garden = Garden()
    plant1 = Plant("lilac")
    plant2 = Plant("begonia", "withering")
    plant3 = Plant("eggplant", "withering")
    garden.add_plant(plant1)
    garden.add_plant(plant2)
    garden.add_plant(plant3)
    print("=== Custom Garden Errors Demo ===\n")
    print("testing PlantError...")
    testing_plant_error(garden.plants)
    print("testing WaterError...")
    testing_water_error(garden.tank_amount)
    garden.set_tank_amount(25)
    print("testing WaterError...")
    testing_water_error(garden.tank_amount)
    print("testing catching all garden errors...")
    testing_garden_errors(garden)
    print("all custom error types work correctly!\n")


if __name__ == "__main__":
    main()
