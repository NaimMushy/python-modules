def ft_harvest_total() -> None:
    """
    Displays total harvest over 3 days based on user input.
    """
    day1: int = int(input("Day 1 harvest: "))
    day2: int = int(input("Day 2 harvest: "))
    day3: int = int(input("Day 3 harvest: "))
    print(f"Total harvest: {day1 + day2 + day3}")
