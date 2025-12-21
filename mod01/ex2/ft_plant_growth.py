# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_plant_growth.py                                 :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ibady <ibady@student.42lyon.fr>            +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/12/21 23:32:18 by ibady             #+#    #+#              #
#    Updated: 2025/12/21 23:43:58 by ibady            ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

class Plant:
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age

    def grow(self) ->None:
        self.height += 1
        
    def age(self) ->None:
        self.age += 1

    def get_info(self) ->None:
        print(f"{self.name}: {self.height}cm, {self.age} days old")

def ft_plant_growth() ->None:
    p1 = Plant("Rose", 25, 30)
    p2 = Plant("Petunia", 10, 6)
    p3 = Plant("Rhododendron", 40, 9)
    plants = []
    plants.append(p1)
    plants.append(p2)
    plants.append(p3)
    for p in plants:
        initial_growth = p.height
        for i in range(1, 8):
            print(f"=== Day {i} ===")
            p.get_info()
            if i < 7:
                p.grow()
                p.age()
        end_growth = p.height
        print(f"Growth this week: +{end_growth - initial_growth}cm")

ft_plant_growth()        
