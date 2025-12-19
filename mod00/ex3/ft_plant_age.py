# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_plant_age.py                                    :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ibady <ibady@student.42lyon.fr>            +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/12/19 16:58:27 by ibady             #+#    #+#              #
#    Updated: 2025/12/19 17:01:09 by ibady            ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def ft_plant_age() ->None:
    age = int(input("Enter plant age in days: "))
    if age > 60:
        print("Plant is ready to harvest!")
    else:
        print("Plant needs more time to grow.")

ft_plant_age()
