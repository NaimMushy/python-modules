def ft_garden_summary() -> None:
    """
    Displays a garden's data based on user input and a fixed status message.
    """
    g_name: str = input("Enter garden name: ")
    nb_plants: int = int(input("Enter number of plants: "))
    status_msg = "Growing well!"
    print(f"Garden: {g_name}\nPlants: {nb_plants}\nStatus: {status_msg}")
