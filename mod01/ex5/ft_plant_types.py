# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_plant_types.py                                  :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ibady <ibady@student.42lyon.fr>            +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/01/06 11:51:11 by ibady             #+#    #+#              #
#    Updated: 2026/01/06 12:37:11 by ibady            ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

class Plant:
    def __init__(self, name, height, age, spec = "Plant"):
        self.name = name.capitalize()
        self.height = height
        self.age = age
        if spec != "Plant":
            print(f"{self.name} ({spec}): {self.height}cm, {self.age} days, ", end='')
        else:
            print(f"{self.name} ({spec}): {self.height}cm, {self.age} days")


class Flower(Plant):
    def __init__(self, name, height, age, color, spec = "Flower"):
        super().__init__(name, height, age, spec)
        self.color = color
        print(f"{self.color} color")

    def bloom(self)->None:
        self.height += 1
        self.age += 1
        print(f"{self.name} is blooming beautifully!")

class Tree(Plant):
    def __init__(self, name, height, age, trunk_diameter, spec = "Tree"):
        super().__init__(name, height, age, spec)
        self.trunk_diameter = trunk_diameter
        print(f"{self.trunk_diameter}cm diameter")
    
    def produce_shade(self, shade)->None:
        print(f"{self.name} provides {shade} square meters of shade")

class Vegetable(Plant):
    def __init__(self, name, height, age, harvest_season, nutri_val, spec = "Vegetable"):
        super().__init__(name, height, age, spec)
        self.harvest_season = harvest_season
        self.nutri_val = nutri_val
        print(f"{self.harvest_season} harvest")

    def display_nutri_val(self)->None:
        print(f"{self.name} is rich in {self.nutri_val}")

print("=== Garden Plant Types ===\n")
flower1 = Flower("rose", 25, 30, "white")
flower1.bloom()
flower2 = Flower("lilac", 16, 4, "mauve")
flower2.bloom()
tree1 = Tree("oak", 500, 1825, 50)
tree1.produce_shade(78)
tree2 = Tree("maple", 482, 796, 44)
tree2.produce_shade(56)
veg1 = Vegetable("tomato", 80, 90, "summer", "vitamin C, vitamin A, potassium, calcium")
veg1.display_nutri_val()
veg2 = Vegetable("eggplant", 150, 60, "fall", "fiber, potassium, magnesium, iron")
veg2.display_nutri_val()
