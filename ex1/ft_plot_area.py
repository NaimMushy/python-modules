# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_plot_area.py                                    :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ibady <ibady@student.42lyon.fr>            +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/12/19 16:22:42 by ibady             #+#    #+#              #
#    Updated: 2025/12/19 16:28:24 by ibady            ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def ft_plot_area() ->None:
    length = int(input("Enter length: "))
    width = int(input("Enter width: "))
    print(f"Plot area: {length * width}")

ft_plot_area()
