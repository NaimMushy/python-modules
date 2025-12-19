# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_water_reminder.py                               :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ibady <ibady@student.42lyon.fr>            +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/12/19 17:57:16 by ibady             #+#    #+#              #
#    Updated: 2025/12/19 18:00:11 by ibady            ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def ft_water_reminder():
    lastWatering = int(input("Days since last watering: "))
    if lastWatering > 2:
        print("Water the plants!")
    else:
        print("Plants are fine")
