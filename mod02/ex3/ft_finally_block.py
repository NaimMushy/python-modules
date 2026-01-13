# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_finally_block.py                                :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ibady <ibady@student.42lyon.fr>            +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/01/12 16:26:50 by ibady             #+#    #+#              #
#    Updated: 2026/01/12 16:44:00 by ibady            ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

class Plant:
    def __init__(self, name):
        self.name = name

class NameError(Exception):
    def __init__(self, name):
        self.msg = "error: cannot water " + str(name) + " - invalid name!\n"

def water_plants(plant_list)->None:
    print("opening watering system\n")
    try:
        for plant in plant_list:
            name = plant.name
            if type(name) == str:
                print(f"watering {name}")
            else:
                raise NameError(name)
    except NameError as ne:
        print(ne.msg)
    finally:
        print("closing watering system (cleanup)\n")
        if type(name) == str:
            print("watering completed without issues!\n")

def test_watering_system()->None:
    print("=== Garden Watering System ===\n")
    print("Testing normal watering...")
    p1 = Plant("tomato")
    p2 = Plant("lettuce")
    p3 = Plant("carrots")
    p4 = Plant("eggplant")
    p5 = Plant(123)
    p6 = Plant(None)
    water_plants([p1, p2, p3])
    water_plants([p1, p5, p6, p4])

test_watering_system()
