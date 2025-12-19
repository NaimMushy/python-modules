# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_count_harvest_recursive.py                      :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ibady <ibady@student.42lyon.fr>            +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/12/19 18:10:09 by ibady             #+#    #+#              #
#    Updated: 2025/12/19 18:10:44 by ibady            ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def ft_count_harvest_recursive(day:int = 0, count:int = 1) ->None:
    if day == 0:
        day = int(input("Days until harvest: "))
    if count <= day:
        print(f"Day {count}")
        ft_count_harvest_recursive(day, count + 1)
    else:
        print("Harvest time!")

ft_count_harvest_recursive()
