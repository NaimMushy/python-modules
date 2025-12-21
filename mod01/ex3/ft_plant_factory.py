# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_plant_factory.py                                :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ibady <ibady@student.42lyon.fr>            +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/12/21 23:47:11 by ibady             #+#    #+#              #
#    Updated: 2025/12/21 23:55:14 by ibady            ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

class Plant:
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age
        print(f"Created: {self.name} ({self.height}cm, {self.age} days)")

def ft_plant_factory() ->None:
    plants = []
    print("=== Plant Factory Output ===")
    for i in range(0, 5):
        name = input("Name of plant: ")
        height = int(input("Height of plant: "))
        age = int(input("Age of plant: "))
        plant = Plant(name, height, age)
        plants.append(plant)
    print(f"Total plants created: {len(plants)}")

ft_plant_factory()

