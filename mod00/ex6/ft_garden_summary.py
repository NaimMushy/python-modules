def ft_garden_summary() -> None:
    """
    Displays a garden's data based on user input and a fixed status message.
    """
    grd_name: str = input("Enter garden name: ")
    nb_plants: int = int(input("Enter number of plants: "))
    print(f"Garden: {grd_name}\nPlants: {nb_plants}\nStatus: Growing well!")
