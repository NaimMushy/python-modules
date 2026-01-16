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
            The plant's name.
        state
            The plant's state.
        """
        self.name = name
        self.state = state

    def set_state(self, new_state: str) -> None:
        """
        Updates the plant's state.

        Parameters
        ----------
        new_state
            The plant's new state.
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
        self.set_tank_amount(100)

    def add_plant(self, new_plant: Plant) -> None:
        """
        Adds a plant to the garden.

        Parameters
        ----------
        new_plant
            The plant to add.
        """
        self.plants.append(new_plant)

    def set_tank_amount(self, new_amount: int) -> None:
        """
        Verifies and updates the garden's tank amount.

        Parameters
        ----------
        new_amount
            The new amount of the garden's tank.
        """
        if new_amount >= 0:
            self._tank_amount = new_amount
        else:
            self._tank_amount = 0
            print(
                f"error: amount {new_amount} "
                f"for the garden's tank - invalid [REJECTED]"
            )

    def get_tank_amount(self) -> None:
        """
        Returns
        -------
        int
            The garden's tank amount.
        """
        return (self._tank_amount)


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
        A list of plants.
    error_type
        The type of the error
        (GardenError or PlantError).

    Raises
    ------
    PlantError:
        Raised if a plant is withering.
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
        The garden's tank amount.
    error_type
        The type of error
        (GardenError or WaterError).

    Raises
    ------
    WaterError:
        Raised if the tank amount is too low.
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
        The garden to check.
    """
    testing_plant_error(garden.plants, "GardenError")
    testing_water_error(garden.get_tank_amount(), "GardenError")


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
    testing_water_error(garden.get_tank_amount())
    garden.set_tank_amount(25)
    print("testing WaterError...")
    testing_water_error(garden.get_tank_amount())
    print("testing catching all garden errors...")
    testing_garden_errors(garden)
    print("all custom error types work correctly!\n")


if __name__ == "__main__":
    main()
