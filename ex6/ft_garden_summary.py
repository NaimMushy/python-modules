# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_garden_summary.py                               :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ibady <ibady@student.42lyon.fr>            +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/12/19 22:09:19 by ibady             #+#    #+#              #
#    Updated: 2025/12/19 22:11:55 by ibady            ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def ft_garden_summary() ->None:
    g_name = input("Enter garden name: ")
    nb_plants = input("Enter number of plants: ")
    status_msg = "They are dying."
    print(f"Garden: {g_name}\nPlants: {nb_plants}\nStatus: {status_msg}")

ft_garden_summary()
