def ft_plant_age() -> None:
    """
    Displays a message indicating
    whether or not the plant is ready for harvesting
    based on its age.
    """
    age: int = int(input("enter plant age in days: "))
    if age > 60:
        print("plant is ready to harvest!")
    else:
        print("plant needs more time to grow.")
