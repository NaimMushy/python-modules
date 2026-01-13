# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_garden_management.py                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ibady <ibady@student.42lyon.fr>            +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/01/13 13:19:19 by ibady             #+#    #+#              #
#    Updated: 2026/01/13 14:08:30 by ibady            ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

class GardenError(Exception):
    def __init__(self, msg, error_type = "GardenError"):
        self.msg = error_type + ": " + msg
        
class WaterError(GardenError):
    def __init__(self, msg, error_type):
        super().__init__(msg, error_type)

class WateringError(GardenError):
    def __init__(self, plant_name):
        msg = "cannot water " + str(plant_name) + " - invalid plant!"
        super().__init__(msg, "WateringError")

class HealthError(GardenError):
    def __init__(self, msg, error_type):
        super().__init__(msg, error_type)

class Plant:
    def __init__(self, name, water_level, sunlight_hours):
        self.name = name
        self.water_lvl = water_level
        self.sun_h = sunlight_hours

    def water(self):
        self.water_lvl += 1
        print(f"watering {self.name} - success")

    def check_health(self, error_type = "HealthError"):
        try:
            if self.water_lvl < 1:
                raise HealthError(str(self.name) + ": water level " + str(self.water_lvl) + " is too low (min 1)", error_type)
            if self.water_lvl > 10:
                raise HealthError(str(self.name) + ": water level " + str(self.water_lvl) + " is too high (max 10)", error_type)
            if self.sun_h < 2:
                raise HealthError(str(self.name) + ": sunlight hours " + str(self.sun_h) + " is too low (min 2)", error_type)
            if self.sun_h > 12:
                raise HealthError(str(self.name) + ": sunlight hours " + str(self.sun_h) + " is too high (max 12)", error_type)
        except HealthError as he:
            print(he.msg)
            if error_type == "GardenError":
                print("system recovered and continuing...")
        else:
            if error_type != "GardenError":
                print(f"{self.name}: healthy (water: {self.water_lvl}, sun: {self.sun_h})")

class GardenManager:
    def __init__(self, owner):
        self.owner = owner
        self.plants = []
        self.water_tank = 100

    def add_plant(self, new_plant):
        try:
            if new_plant.name == "":
                raise ValueError("error adding plant: plant name cannot be empty!")
        except ValueError as ve:
            print(ve)
        else:
            self.plants.append(new_plant)
            print(f"added {new_plant.name} successfully")

    def water_plants(self):
        try:
            print("opening watering system")
            for plant in self.plants:
                if type(plant.name) == str:
                    plant.water()
                    self.water_tank -= 1
                else:
                    raise WateringError(plant.name)
        except WateringError as we:
            print(we.msg)
        finally:
            print("closing watering system (cleanup)\n")

    def check_plant_health(self, error_type = "HealthError"):
        for plant in self.plants:
            plant.check_health(error_type)

    def check_water_tank(self, error_type = "WaterError"):
        try:
            if self.water_tank < 30:
                raise WaterError("not enough water in tank", error_type)
        except WaterError as we:
            print(we.msg)
            if error_type == "GardenError":
                print("system recovered and continuing...")

    def check_garden_errors(self):
        self.check_water_tank("GardenError")
        self.check_plant_health("GardenError")

p1 = Plant("lilac", 12, 9)
p2 = Plant("", 5, 6)
p3 = Plant("eggplant", 4, 3)
p4 = Plant("hibiscus", 8, 1)
p5 = Plant("zucchini", 0, 11)
p6 = Plant("pumpkin", 9, 5)

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

test_all()
