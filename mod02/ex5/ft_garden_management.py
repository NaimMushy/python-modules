MIN_WATER_LVL = 1
MAX_WATER_LVL = 10
MIN_SUN_H = 2
MAX_SUN_H = 12


class GardenError(Exception):
    def __init__(self, msg: str, error_type: str = "GardenError") -> None:
        self.msg: str = f"{error_type}: " + msg


class WaterError(GardenError):
    def __init__(self, msg: str) -> None:
        super().__init__(msg, "WaterError")


class HealthError(GardenError):
    def __init__(self, msg: str) -> None:
        super().__init__(msg, "HealthError")


class Plant:
    def __init__(
        self,
        name: str,
        water_level: int,
        sunlight_hours: int
    ) -> None:
        self.name = name
        try:
            self.set_water_lvl(water_level)
        except ValueError as ve:
            print(f"Caught ValueError: {ve}")
            print("Setting to default: 6")
            self.set_water_lvl(5)
        try:
            self.set_sun_h(sunlight_hours)
        except ValueError as ve:
            print(f"Caught ValueError: {ve}")
            print("Setting to default: 6")
            self.set_sun_h(6)

    def set_water_lvl(self, water_level: int) -> None:
        if isinstance(water_level, int) and water_level >= 0:
            self.__water_lvl = water_level
        else:
            raise ValueError(
                f"Water level {water_level} "
                f"for {self.name} - Invalid [REJECTED]"
            )

    def set_sun_h(self, sunlight_hours: int) -> None:
        if isinstance(sunlight_hours, int) and sunlight_hours >= 0:
            self.__sun_h = sunlight_hours
        else:
            raise ValueError(
                f"Sunlight hours {sunlight_hours} "
                f"for {self.name} - Invalid [REJECTED]"
            )

    def get_water_lvl(self) -> int:
        return self.__water_lvl

    def get_sun_h(self) -> int:
        return self.__sun_h

    def water(self) -> None:
        self.__water_lvl += 1
        print(f"Watering {self.name} - Success")


class GardenManager:
    def __init__(self, owner: str) -> None:
        self.owner: str = owner
        self.plants: list[Plant] = []
        self.water_tank: int = 100

    def add_plant(self, new_plant: Plant) -> None:
        try:
            if not new_plant.name or new_plant.name == "":
                raise ValueError(
                    "Error adding plant: Plant name cannot be empty!"
                )
        except ValueError as ve:
            print(ve)
        else:
            self.plants.append(new_plant)
            print(f"Added {new_plant.name} successfully")

    def water_plants(self) -> None:
        try:
            print("Opening watering system")
            for plant in self.plants:
                if self.water_tank < 1:
                    raise WaterError(
                        "Caught WaterError: Not enough water in the tank!"
                    )
                elif isinstance(plant.name, str):
                    plant.water()
                    self.water_tank -= 1
                else:
                    raise ValueError(
                        f"Caught ValueError: Cannot water "
                        f"{plant.name} - Invalid plant!"
                    )
        except Exception as err:
            print(err)
        finally:
            print("Closing watering system (cleanup)\n")

    def check_plant_health(self) -> None:
        for plant in self.plants:
            if plant.get_water_lvl() < MIN_WATER_LVL:
                raise HealthError(
                    f"Water level {plant.get_water_lvl()} "
                    f"is too low (min {MIN_WATER_LVL})"
                )
            elif plant.get_water_lvl() > MAX_WATER_LVL:
                raise HealthError(
                    f"Water level {plant.get_water_lvl()} "
                    f"is too high (max {MAX_WATER_LVL})"
                )
            elif plant.get_sun_h() < MIN_SUN_H:
                raise HealthError(
                    f"Sunlight hours {plant.get_sun_h()}"
                    f"is too low (min {MIN_SUN_H})"
                )
            elif plant.get_sun_h() > MAX_SUN_H:
                raise HealthError(
                    f"Sunlight hours {plant.get_sun_h()}"
                    f"is too high (min {MAX_SUN_H})"
                )
            else:
                print(
                    f"{self.name}: Healthy (water: "
                    f"{self._water_lvl}, sun: {self._sun_h})"
                )

    def check_water_tank(self) -> None:
        if self.water_tank < 30:
            raise WaterError("Not enough water in tank!")

    def check_garden_errors(self) -> None:
        try:
            self.check_water_tank()
        except GardenError as ge:
            print(f"Caught GardenError: {ge}")
            print("System recovered and continuing...")
        try:
            self.check_plant_health()
        except GardenError as ge:
            print(f"Caught GardenError: {ge}")
            print("System recovered and continuing...")


def test_garden_management() -> None:
    print("=== Garden Management System ===")
    garden = GardenManager("Naïm")
    print("\nAdding plants to garden...")
    garden.add_plant(Plant("lilac", 12, 9))
    garden.add_plant(Plant(None, 5, 6))
    garden.add_plant(Plant("eggplant", 4, 3))
    garden.add_plant(Plant("hibiscus", 8, 1))
    garden.add_plant(Plant("zucchini", 0, 11))
    garden.add_plant(Plant("pumpkin", 9, 5))
    print("\nWatering plants...")
    garden.water_plants()
    garden.plants[3].name = 123
    garden.water_plants()
    print("Checking plant health...")
    try:
        garden.check_plant_health()
    except HealthError as he:
        print(f"Caught HealthError: {he}")
    try:
        garden.check_water_tank()
        garden.water_tank = 25
        garden.check_water_tank()
    except WaterError as we:
        print(f"Caught WaterError: {we}")
    print("\nTesting garden errors...")
    garden.check_garden_errors()
    print("\nGarden management system test complete!\n")


def main() -> None:
    test_garden_management()


if __name__ == "__main__":
    main()
