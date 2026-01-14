def ft_water_reminder() -> None:
    last_watering: int = int(input("days since last watering: "))
    if last_watering > 2:
        print("water the plants!")
    else:
        print("plants are fine")
