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
    """
    A class that represents a plant.
    """
    def __init__(
        self,
        name: str,
        water_level: int,
        sunlight_hours: int
    ) -> None:
        """
        Initializes the plant's data.

        Parameters
        ----------
        name
            The plant's name.
        water_level
            The plant's water level.
        sunlight_hours
            The plant's sunlight hours.
        """
        self.name = name
        self.set_water_lvl(water_level)
        self.set_sun_h(sunlight_hours)

    def set_water_lvl(self, water_level: int) -> None:
        """
        Verifies and updates the plant's water level.

        Parameters
        ----------
        water_level
            The plant's water level.
        """
        if water_level >= 0:
            self._water_lvl = water_level
        else:
            self._water_lvl = 0
            print(
                f"error: water level {water_level} "
                f"for {self.name} - invalid [REJECTED]"
            )

    def set_sun_h(self, sunlight_hours: int) -> None:
        """
        Verifies and updates the plant's sunlight hours.

        Parameters
        ----------
        sunlight_hours
            The plant's sunlight hours.
        """
        if sunlight_hours >= 0:
            self._sun_h = sunlight_hours
        else:
            self._sun_h = 0
            print(
                f"error: sunlight hours {sunlight_hours} "
                f"for {self.name} - invalid [REJECTED]"
            )

    def get_water_lvl(self) -> None:
        """
        Returns
        -------
        int
            The plant's water level.
        """
        return (self._water_lvl)

    def get_sun_h(self) -> None:
        """
        Returns
        -------
        int
            The plant's sunlight hours.
        """
        return (self._sun_h)

    def water(self) -> None:
        """
        Simulates the watering of the plant.
        """
        self._water_lvl += 1
        print(f"watering {self.name} - success")

    def check_health(self, error_type: str = "HealthError") -> None:
        """
        Checks a plant's health.

        Parameters
        ----------
        error_type
            The type of the error
            (GardenError or HealthError).

        Raises
        ------
        HealthError:
            Raised if water level is inadequate (too low or too high).
        HealthError:
            Raised if sunlight hours are inadequate (too low or too high).
        """
        try:
            if self._water_lvl < MIN_WATER_LVL:
                raise HealthError(
                    f"{error_type}: water level {self._water_lvl} "
                    f"is too low (min {MIN_WATER_LVL})"
                )
            if self._water_lvl > MAX_WATER_LVL:
                raise HealthError(
                    f"{error_type}: water level {self._water_lvl} "
                    f"is too high (max {MAX_WATER_LVL})"
                )
            if self._sun_h < MIN_SUN_H:
                raise HealthError(
                    f"{error_type}: sunlight hours {self._sun_h}"
                    f"is too low (min {MIN_SUN_H})"
                )
            if self._sun_h > MAX_SUN_H:
                raise HealthError(
                    f"{error_type}: sunlight hours {self._sun_h}"
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
                    f"{self._water_lvl}, sun: {self._sun_h})"
                )


class GardenManager:
    """
    A class that represents a garden manager.
    """
    def __init__(self, owner: str) -> None:
        """
        Initializes the garden's data.

        Parameters
        ----------
        owner
            The garden's owner.
        """
        self.owner = owner
        self.plants: list[Plant] = []
        self.water_tank: int = 100

    def add_plant(self, new_plant: Plant) -> None:
        """
        Adds a plant to the garden.

        Parameters
        ----------
        new_plant
            The new plant to add.

        Raises
        ------
        ValueError:
            Raised if the plant's name is empty.
        """
        try:
            if new_plant.name == "":
                raise ValueError(
                    "error adding plant: plant name cannot be empty!"
                )
        except ValueError as ve:
            print(ve)
        else:
            self.plants.append(new_plant)
            print(f"added {new_plant.name} successfully")

    def water_plants(self, error_type: str = "WaterError") -> None:
        """
        Simulates the watering of the garden's plants.

        Parameters
        ----------
        error_type
            The type of the error
            (GardenError or WaterError).

        Raises
        ------
        WaterError:
            Raised if not enough water in the tank to water plant.
        ValueError:
            Raised if the plant's name is invalid.
        """
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

    def check_plant_health(self, error_type: str = "HealthError") -> None:
        """
        Checks the health of the garden's plants.

        Parameters
        ----------
        error_type
            The type of error
            (GardenError or PlantError).
        """
        for plant in self.plants:
            plant.check_health(error_type)

    def check_water_tank(self, error_type: str = "WaterError") -> None:
        """
        Checks the water tank amount.

        Parameters
        ----------
        error_type
            The type of error
            (GardenError or WaterError).

        Raises
        ------
        WaterError:
            Raised if the amount in the water tank is too low.
        """
        try:
            if self.water_tank < 30:
                raise WaterError(f"{error_type}: not enough water in tank!")
        except WaterError as we:
            print(we)
            if error_type == "GardenError":
                print("system recovered and continuing...")

    def check_garden_errors(self) -> None:
        """
        Checks for garden errors.
        """
        self.check_water_tank("GardenError")
        self.check_plant_health("GardenError")


p1 = Plant("lilac", 12, 9)
p2 = Plant("", 5, 6)
p3 = Plant("eggplant", 4, 3)
p4 = Plant("hibiscus", 8, 1)
p5 = Plant("zucchini", 0, 11)
p6 = Plant("pumpkin", 9, 5)


def test_all() -> None:
    """
    Tests the correct behavior of the garden manager.
    """
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


def main() -> None:
    test_all()


if __name__ == "__main__":
    main()
