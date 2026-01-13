# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_raise_errors.py                                 :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ibady <ibady@student.42lyon.fr>            +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/01/13 13:03:59 by ibady             #+#    #+#              #
#    Updated: 2026/01/13 13:18:12 by ibady            ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def check_plant_health(plant_name, water_level, sunlight_hours)->None:
    try:
        name_msg = "error: plant name cannot be empty!\n"
        low_water_msg = "error: water level " + str(water_level) + " is too low (min 1)!\n"
        high_water_msg = "error: water level " + str(water_level) + " is too high (max 10)!\n"
        low_sunlight_msg = "error: sunlight hours " + str(sunlight_hours) + " is too low (min 2)!\n" 
        high_sunlight_msg = "error: sunlight hours " + str(sunlight_hours) + " is too high (max 12)!\n" 
        if plant_name == "":
            raise ValueError(name_msg)
        if water_level < 1:
            raise ValueError(low_water_msg)
        if water_level > 10:
            raise ValueError(high_water_msg)
        if sunlight_hours < 2:
            raise ValueError(low_sunlight_msg)
        if sunlight_hours > 12:
            raise ValueError(high_sunlight_msg)
    except ValueError as ve:
        print(ve)
    else:
        print(f"plant {plant_name} is healthy!\n")

def test_plant_checks()->None:
    print("=== Garden Plant Health Checker ===\n")
    print("testing good values...")
    check_plant_health("eggplant", 4, 9)
    print("testing empty plant name...")
    check_plant_health("", 4, 9)
    print("testing bad water level...")
    check_plant_health("eggplant", 16, 9)
    print("testing bad water level...")
    check_plant_health("eggplant", 0, 9)
    print("testing bad sunlight hours...")
    check_plant_health("eggplant", 4, 17)
    print("testing bad sunlight hours...")
    check_plant_health("eggplant", 4, 1)
    print("all error raising tests completed!\n")

test_plant_checks()
