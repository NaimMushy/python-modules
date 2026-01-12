# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_different_errors.py                             :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ibady <ibady@student.42lyon.fr>            +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/01/08 11:26:48 by ibady             #+#    #+#              #
#    Updated: 2026/01/08 11:31:02 by ibady            ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def garden_operations(error_type)->None:
    if error_type == "ve":
        nb = int("abc")
    if error_type == "zde":
        nb = 16 / 0
    if error_type == "fnfe":
        file = open("inexistant.txt")
    if error_type == "ke":
        fav_tigercub_songs = {1: "The Dark Below", 2: "Beating on my Heart", 3: "It's only Love"}
        fourth = fav_tigercub_songs[4]

def test_error_types()->None:
    print("=== Garden Error Types Demo ===\n")
    print("Testing ValueError...")
    try:
        garden_operations("ve")
    except ValueError:
        print("Caught ValueError: invalid literal for int()\n")
    print("Testing ZeroDivisionError...")
    try:
        garden_operations("zde")
    except ZeroDivisionError:
        print("Caught ZeroDivisionError: division by zero\n")
    print("Testing FileNotFoundError...")
    try:
        garden_operations("fnfe")
    except FileNotFoundError:
        print("Caught FileNotFoundError: No such file 'inexistant.txt'\n")
    print("Testing KeyError...")
    try:
        garden_operations("ke")
    except KeyError:
        print("Caught KeyError: missing favorite song\n")
    print("Testing multiple errors together...")
    try:
        garden_operations("ve")
        garden_operations("zde")
        garden_operations("fnfe")
        garden_operations("ke")
    except ValueError or ZeroDivisionError or FileNotFoundError or KeyError:
        print("Caught an error, but program continues!\n")
    print("All error types tested successfully!\n")

test_error_types() 
