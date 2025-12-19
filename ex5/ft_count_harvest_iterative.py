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

def ft_count_harvest_iterative() ->None:
    day = int(input("Days until harvest: "))
    count = 1
    while count <= day:
        print(f"Day {count}")
        count += 1
    print("Harvest time!")

ft_count_harvest_iterative()
