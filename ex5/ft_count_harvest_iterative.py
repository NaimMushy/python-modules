# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_count_harvest_iterative.py                      :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ibady <ibady@student.42lyon.fr>            +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/12/19 18:01:17 by ibady             #+#    #+#              #
#    Updated: 2025/12/19 18:09:49 by ibady            ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def ft_count_harvest_iterative(day = 0, count = 1):
    if day == 0:
        day = int(input("Days until harvest: "))
    while count <= day:
        print(f"Day {count}")
        count += 1
