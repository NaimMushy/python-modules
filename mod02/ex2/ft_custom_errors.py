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

    def get_tank_amount(self) -> int:
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
    err_count: int = 0
    for plant in plants:
        try:
            if plant.state == "withering":
                err_count += 1
                raise PlantError(
                    f"Caught {error_type}: the {plant.name} is withering!\n"
                )
        except PlantError as pe:
            print(pe)
    if err_count == 0:
        print("All plants are blooming! :)\n")


def testing_water_error(
    tank_amount: int,
) -> None:
    try:
        if tank_amount < 30:
            raise WaterError(
                f"Caught {error_type}: not enough water in the tank!\n"
            )
        else:
            print("There's enough water in the tank!\n")
    except WaterError as we:
        print(we)


def testing_garden_errors(garden: Garden) -> None:
    testing_plant_error(garden.plants, "GardenError")
    testing_water_error(garden.get_tank_amount(), "GardenError")


def main() -> None:
    garden: Garden = Garden()
    plant1: Plant = Plant("lilac")
    plant2: Plant = Plant("begonia", "withering")
    plant3: Plant = Plant("eggplant", "withering")
    garden.add_plant(plant1)
    garden.add_plant(plant2)
    garden.add_plant(plant3)
    print("=== Custom Garden Errors Demo ===\n")
    print("Testing PlantError...")
    testing_plant_error(garden.plants)
    print("Testing WaterError...")
    testing_water_error(garden.get_tank_amount())
    garden.set_tank_amount(25)
    print("Testing WaterError...")
    testing_water_error(garden.get_tank_amount())
    print("Testing catching all garden errors...")
    testing_garden_errors(garden)
    print("All custom error types work correctly!\n")


if __name__ == "__main__":
    main()
