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

def ft_count_harvest_iterative(day = 0, count = 1):
    if day == 0:
        day = int(input("Days until harvest: "))
    while count <= day:
        print(f"Day {count}")
        ft_count_harvest_iterative(day, count + 1)
