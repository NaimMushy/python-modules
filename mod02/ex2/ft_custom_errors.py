class Plant:
    def __init__(self, name: str, state: str = "blooming") -> None:
        self.name = name
        self.state = state


class Garden:
    def __init__(self) -> None:
        self.plants: list[Plant] = []
        self.set_tank_amount(100)

    def add_plant(self, new_plant: Plant) -> None:
        self.plants.append(new_plant)

    def set_tank_amount(self, new_amount: int) -> None:
        if isinstance(new_amount, int) and new_amount >= 0:
            self.__tank_amount = new_amount
            print(
                "Garden's tank amount has been successfully "
                f"updated to {new_amount}!"
            )
        else:
            print(
                f"Error: amount {new_amount} "
                f"for the garden's tank - Invalid [REJECTED]"
            )

    def get_tank_amount(self) -> None:
        return (self.__tank_amount)


class GardenError(Exception):
    pass


class PlantError(GardenError):
    pass


class WaterError(GardenError):
    pass


def testing_plant_error(
    plant: Plant
) -> None:
    if plant.state == "withering":
        raise PlantError(f"The {plant.name} is withering!")


def testing_water_error(
    tank_amount: int,
) -> None:
    if tank_amount < 30:
        raise WaterError("Not enough water in the tank!")
    else:
        print("There's enough water in the tank!")


def testing_garden_errors(garden: Garden) -> None:
    for plant in garden.plants:
        try:
            testing_plant_error(plant)
        except GardenError as ge:
            print(f"Caught a garden error: {ge}")
    try:
        testing_water_error(garden.get_tank_amount())
    except GardenError as ge:
        print(f"Caught a garden error: {ge}")


def main() -> None:
    garden = Garden()
    garden.add_plant(Plant("lilac"))
    garden.add_plant(Plant("begonia", "withering"))
    garden.add_plant(Plant("eggplant", "withering"))
    print("=== Custom Garden Errors Demo ===")
    print("\nTesting PlantError...")
    for plant in garden.plants:
        try:
            testing_plant_error(plant)
        except PlantError as pe:
            print(f"Caught PlantError: {pe}")
    print("\nTesting WaterError...")
    try:
        testing_water_error(garden.get_tank_amount())
        garden.set_tank_amount(25)
        testing_water_error(garden.get_tank_amount())
    except WaterError as we:
        print(f"Caught WaterError: {we}")
    print("\nTesting catching all garden errors...")
    testing_garden_errors(garden)
    print("All custom error types work correctly!\n")


if __name__ == "__main__":
    main()
