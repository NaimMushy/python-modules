# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_first_exception.py                              :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ibady <ibady@student.42lyon.fr>            +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/01/08 11:07:17 by ibady             #+#    #+#              #
#    Updated: 2026/01/08 11:22:21 by ibady            ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def check_temperature(temp_str)->str:
    try:
        temp = int(temp_str)
    except ValueError:
        print(f"error: '{temp_str}' is not a valid number\n")
    else:
        if temp < 0:
            print(f"temperature {temp} is too cold for plants (min 0°C)\n")
        elif temp > 40:
            print(f"temperature {temp} is too hot for plants (max 40°C)\n")
        else:
            print(f"temperature {temp}°C is perfect for plants!\n")
            return (temp)

def test_temperature_input()->None:
    temp_str = input("enter a test temperature: ")
    while temp_str != "stop":
        print(f"testing temperature: {temp_str}\n")
        check_temperature(temp_str)
        temp_str = input("enter a test temperature: ")
    print("all tests completed: program didn't crash!\n")

test_temperature_input()
