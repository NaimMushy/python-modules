# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_garden_data.py                                  :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ibady <ibady@student.42lyon.fr>            +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/12/19 22:50:05 by ibady             #+#    #+#              #
#    Updated: 2025/12/19 23:03:48 by ibady            ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

class Plant:
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age

    def display_info(self) ->None:
        print(f"{self.name}: {self.height}cm, {self.age} days old")

plants = []
plant1 = Plant("Anneau de cinabre", 40075017000, 666)
plant2 = Plant("Baltrou", -10000000, 53)
plant3 = Plant("Trou qui pète", 1, 0)
plants.append(plant1)
plants.append(plant2)
plants.append(plant3)
print("=== Garden Plant Registry ===")
for plant in plants:
    plant.display_info()

