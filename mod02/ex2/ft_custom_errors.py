class Plant:
    def __init__(self, name: str, state: str = "blooming") -> None:
        self.name: str = name
        self.state: str = state


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

    def check_tank_amount(self, error_type: str = "WaterError") -> None:
        try:
            if self.__tank_amount < 30:
                raise WaterError("Not enough water in the tank!")
        except GardenError as ge:
            print(f"Caught {error_type}: {ge}")
        else:
            print("There's enough water in the tank!")

    def check_plants(self, error_type: str = "PlantError") -> None:
        err: bool = False
        for plant in self.plants:
            try:
                if plant.state == "withering":
                    err = True
                    raise PlantError(f"The {plant.name} is withering!")
            except GardenError as ge:
                print(f"Caught {error_type}: {ge}")
        if not err:
            print("All the plants are blooming! :)")


class GardenError(Exception):
    pass


class PlantError(GardenError):
    pass


class WaterError(GardenError):
    pass


def main() -> None:
    garden: Garden = Garden()
    garden.add_plant(Plant("lilac"))
    garden.add_plant(Plant("begonia", "withering"))
    garden.add_plant(Plant("eggplant", "withering"))
    print("=== Custom Garden Errors Demo ===")
    print("\nTesting PlantError...")
    garden.check_plants()
    print("\nTesting WaterError...")
    garden.set_tank_amount(25)
    garden.check_tank_amount()
    print("\nTesting catching all garden errors...")
    garden.check_plants("GardenError")
    garden.check_tank_amount("GardenError")
    print("\nAll custom error types work correctly!")


if __name__ == "__main__":
    main()
