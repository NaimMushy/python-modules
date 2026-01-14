class Plant:
    def __init__(self, name: str, state: str = "blooming") -> None:
        self.name = name
        self.state = state

    def set_state(self, new_state: str) -> None:
        self.state = new_state


class Garden:
    def __init__(self) -> None:
        self.plants: list[Plant] = []
        self.tank_amount: int = 100

    def add_plant(self, new_plant: Plant) -> None:
        self.plants.append(new_plant)

    def set_tank_amount(self, new_amount: int) -> None:
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
    testing_plant_error(garden.plants, "GardenError")
    testing_water_error(garden.tank_amount, "GardenError")


if __name__ == "__main__":
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
