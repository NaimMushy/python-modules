def ft_garden_summary() -> None:
    """
    Displays a garden's data based on user input and a fixed status message.
    """
    g_name: str = input("enter garden name: ")
    nb_plants: int = int(input("enter number of plants: "))
    status_msg = "they are dying."
    print(f"garden: {g_name}\nplants: {nb_plants}\nstatus: {status_msg}")
