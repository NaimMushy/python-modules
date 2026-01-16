def ft_water_reminder() -> None:
    """
    Outputs a message indicating whether or not the plants need watering
    based on the date of the last watering.
    """
    last_watering: int = int(input("days since last watering: "))
    if last_watering > 2:
        print("water the plants!")
    else:
        print("plants are fine")
