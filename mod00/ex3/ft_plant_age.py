def ft_plant_age() -> None:
    age: int = int(input("enter plant age in days: "))
    if age > 60:
        print("plant is ready to harvest!")
    else:
        print("plant needs more time to grow.")
