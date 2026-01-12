# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_custom_errors.py                                :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ibady <ibady@student.42lyon.fr>            +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/01/08 11:32:09 by ibady             #+#    #+#              #
#    Updated: 2026/01/08 11:34:44 by ibady            ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

class Garden:
    def __init__(self):
        self.plants = []
        self.tank_amount = 100

    def add_plant(self, new_plant):
        self.plants.append(new_plant)

    def set_tank_amount(self, new_amount):
        self.tank_amount = new_amount

class Plant:
    def __init__(self, name, state):
        self.name = name
        self.state = state

    def set_state(self, new_state):
        self.state = new_state

class GardenError(Exception):
    def __init__(self, msg, error_type = "GardenError"):
        self.msg = "caught a " + error_type + ": " + msg

class PlantError(GardenError):
    def __init__(self, msg):
        super().__init__(msg, "PlantError")

class WaterError(GardenError):
    def __init__(self, msg):
        super().__init__(msg, "WaterError")

def testing_plant_error(plants, exception):
    err_count = 0
    for plant in plants:
        try:
            if plant.state == "withering":
                msg = "the " + plant.name + " is withering!\n"
                err_count += 1
                raise exception(msg)
        except exception as err:
            print(err.msg)
    if err_count == 0:
        print("all plants are blooming! :)\n")

def testing_water_error(tank_amount, exception):
    try:
        if tank_amount < 30:
            raise exception("not enough water in the tank!\n")
         else:
            print("there's enough water in the tank!\n")
   except exception as err:
        print(err.msg)
    
def testing_garden_errors(garden):
    testing_plant_error(garden.plants, GardenError)
    testing_water_error(garden.tank_amount, GardenError)

garden = Garden()
plant1 = Plant("lilac", "blooming")
plant2 = Plant("begonia", "withering")
plant3 = Plant("eggplant", "withering")
garden.add_plant(plant1)
garden.add_plant(plant2)
garden.add_plant(plant3)
print("=== Custom Garden Errors Demo ===\n")
print("Testing PlantError...")
testing_plant_error(garden.plants, PlantError)
print("Testing WaterError...")
testing_water_error(garden.tank_amount, WaterError)
garden.set_tank_amount(25)
print("Testing WaterError...")
testing_water_error(garden.tank_amount, WaterError)
print("Testing catching all garden errors...")
testing_garden_errors(garden)
print("All custom error types work correctly!\n")
