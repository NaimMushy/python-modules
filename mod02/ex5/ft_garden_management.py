MIN_WATER_LVL = 1
MAX_WATER_LVL = 10
MIN_SUN_H = 2
MAX_SUN_H = 12


class GardenError(Exception):
    pass


class WaterError(GardenError):
    pass


class HealthError(GardenError):
    pass


class Plant:
    def __init__(self, name: str, water_level: int, sunlight_hours: int)->None:
        self.name = name
        self.water_lvl = water_level
        self.sun_h = sunlight_hours

    def water(self)->None:
        self.water_lvl += 1
        print(f"watering {self.name} - success")

    def check_health(self, error_type: str = "HealthError")->None:
        try:
            if self.water_lvl < MIN_WATER_LVL:
                raise HealthError(
                    f"{error_type}: water level {self.water_lvl} "
                    f"is too low (min {MIN_WATER_LVL})"
                )
            if self.water_lvl > MAX_WATER_LVL:
                raise HealthError(
                    f"{error_type}: water level {self.water_lvl} "
                    f"is too high (max {MAX_WATER_LVL})"
                )
            if self.sun_h < MIN_SUN_H:
                raise HealthError(
                    f"{error_type}: sunlight hours {self.sun_h}"
                    f"is too low (min {MIN_SUN_H})"
                )
            if self.sun_h > MAX_SUN_H:
                raise HealthError(
                    f"{error_type}: sunlight hours {self.sun_h}"
                    f"is too high (min {MAX_SUN_H})"
                )
        except HealthError as he:
            print(he)
            if error_type == "GardenError":
                print("system recovered and continuing...")
        else:
            if error_type != "GardenError":
                print(
                    f"{self.name}: healthy (water: "
                    f"{self.water_lvl}, sun: {self.sun_h})"
                )


class GardenManager:
    def __init__(self, owner: str)->None:
        self.owner = owner
        self.plants: list[Plant] = []
        self.water_tank: int = 100

    def add_plant(self, new_plant: Plant)->None:
        try:
            if new_plant.name == "":
                raise ValueError("error adding plant: plant name cannot be empty!")
        except ValueError as ve:
            print(ve)
        else:
            self.plants.append(new_plant)
            print(f"added {new_plant.name} successfully")

    def water_plants(self, error_type: str = "WaterError")->None:
        try:
            print("opening watering system")
            for plant in self.plants:
                if self.water_tank < 1:
                    raise WaterError(
                        f"{error_type}: not enough water in the tank!"
                    )
                elif type(plant.name) is str:
                    plant.water()
                    self.water_tank -= 1
                else:
                    raise ValueError(
                        f"ValueError: cannot water "
                        f"{plant.name} - invalid plant!"
                    )
        except (WaterError, ValueError) as err:
            print(err)
        finally:
            print("closing watering system (cleanup)\n")

    def check_plant_health(self, error_type: str = "HealthError")->None:
        for plant in self.plants:
            plant.check_health(error_type)

    def check_water_tank(self, error_type: str = "WaterError")->None:
        try:
            if self.water_tank < 30:
                raise WaterError(f"{error_type}: not enough water in tank!")
        except WaterError as we:
            print(we)
            if error_type == "GardenError":
                print("system recovered and continuing...")

    def check_garden_errors(self)->None:
        self.check_water_tank("GardenError")
        self.check_plant_health("GardenError")


def test_all()->None:
    print("=== Garden Management System ===\n")
    garden = GardenManager("Naïm")
    print("adding plants to garden...")
    garden.add_plant(p1)
    garden.add_plant(p2)
    garden.add_plant(p3)
    garden.add_plant(p4)
    garden.add_plant(p5)
    garden.add_plant(p6)
    print("watering plants...")
    garden.water_plants()
    p4.name = 123
    garden.water_plants()
    print("checking plant health...")
    garden.check_plant_health()
    garden.check_water_tank()
    garden.water_tank = 25
    garden.check_water_tank()
    print("testing garden errors...")
    garden.check_garden_errors()
    print("garden management system test complete!\n")


if __name__ == "__main__":
    p1 = Plant("lilac", 12, 9)
    p2 = Plant("", 5, 6)
    p3 = Plant("eggplant", 4, 3)
    p4 = Plant("hibiscus", 8, 1)
    p5 = Plant("zucchini", 0, 11)
    p6 = Plant("pumpkin", 9, 5)
    test_all()
