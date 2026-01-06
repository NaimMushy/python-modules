# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_garden_analytics.py                             :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ibady <ibady@student.42lyon.fr>            +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/01/06 12:41:28 by ibady             #+#    #+#              #
#    Updated: 2026/01/06 14:07:59 by ibady            ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

class GardenManager:
    
    garden_helper = GardenStats()

    def create_garden_network(cls):
        cls.gardens = []

    def add_garden(cls, new_garden):
        cls.gardens.append(new_garden)

    class GardenStats:
        def display_stats(garden):
            print(f"=== {garden.owner}'s Garden Report ===\n")
            print("Plants in garden:")
            for plant in garden:
                plant.display_info()
            print(f"Plants added: {garden.size}, Total growth: {garden.total_growth}cm")
            print(f"Plant types: {garden.regular_plants} regular, {garden.flowering_plants} flowering, {garden.prize_plants} prize flowers")
        
        def all_gardens_info(gardens):
            for grd in gardens:
                GardenStats.display_stats(grd)
            print("Garden scores - ", end='')
            for grd in range(len(gardens)):
                if grd < len(gardens) - 1:
                    print(f"{gardens[grd].owner}: {gardens[grd].score}, ", end='')
                else:
                    print(f"{gardens[grd].owner}: {gardens[grd].score}")
            print(f"Total gardens managed: {len(gardens)}")
    
class Garden:

    def __init__(self, owner):
        self.owner = owner
        self.plants = []
        self.size = 0
        self.total_growth = 0
        regular_plants = 0
        flowering_plants = 0
        prize_plants = 0
        score = 0

    def add_plant(self, plant):
        self.plants.append(plant)
        self.size += 1
        self.change_collections(plant.spec)
        print(f"Added {plant.name} to {self.owner}'s garden")

    def grow_all(self):
        print(f"{owner} is helping all plants grow...")
        for plant in self.plants:
            plant.grow(1)
            self.total_growth += 1

    def change_collections(self, spec):
        if spec == "regular":
            self.regular_plants += 1
            self.score += 5
        elif spec == "flowering":
            self.flowering_plants += 1
            self.score += 10
        else:
            self.prize_plants += 1
            self.score += 20
            

class Plant:
    def __init__(self, name, height, age, spec = "regular"):
        self.name = name.capitalize()
        self.height = height
        self.age = age
        self.spec = spec

    def grow(self, growth):
        print(f"{self.name} grew {growth}cm")
        self.height += growth

    def display_info(self):
        if self.spec != "regular":
            print(f"- {self.name}: {self.height}cm, "end='')
        else:
            print(f"- {self.name}: {self.height}cm")

class FloweringPlant(Plant):
    def __init__(self, name, height, age, color, spec = "flowering"):
        super().__init__(name, height, age, spec)
        self.color = color
        self.bloom_state = "not in bloom"

    def bloom(self):
        self.bloom_state = "blooming"

    def display_info(self):
        super().display_info()
        if self.spec != "flowering":
            print(f"{self.color} flowers ({self.bloom_state}), ", end='')
        else:
            print(f"{self.color} flowers ({self.bloom_state})")

class PrizeFlower(FloweringPlant):
    def __init__(self, name, height, age, color, prize_points, spec = "prize"):
        super().__init__(name, height, age, color, spec)
        self.prize_points = prize_points

    def display_info(self):
        super().display_info()
        print(f"prize points: {self.prize_points}")
