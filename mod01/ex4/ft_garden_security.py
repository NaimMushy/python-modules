# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_garden_security.py                              :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ibady <ibady@student.42lyon.fr>            +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/12/22 15:05:57 by ibady             #+#    #+#              #
#    Updated: 2025/12/22 15:22:48 by ibady            ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

class Plant:
    def __init__(self, name, height = 0, age = 0):
        self.__name = name
        print(f"Plant created: {self.__name}")
        self.set_height(height)
        self.set_age(age)

    def set_height(self, new_height) ->None:
        if new_height >= 0:
            self.__height = new_height
            print(f"Height updated: {new_height}cm [OK]")
        else:
            print(f"Invalid operation attempted: height {new_height}cm [REJECTED]\nSecurity: Negative height rejected")

    def set_age(self, new_age) ->None:
        if new_age >= 0:
            self.__age = new_age
            print(f"Age updated: {new_age} days [OK]")
        else:
            print(f"Invalid operation attempted: age {new_age} days [REJECTED]\nSecurity: Negative age rejected")
    
    def get_height(self) ->int:
        return self.__height
    
    def get_age(self) ->int:
        return self.__age
