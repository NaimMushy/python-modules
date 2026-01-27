def ft_water_reminder() -> None:
    """
    Outputs a message indicating whether or not the plants need watering
    based on the date of the last watering.
    """
    last_watering: int = int(input("Days since last watering: "))
    if last_watering > 2:
        print("Water the plants!")
    else:
        print("Plants are fine")
