def ft_count_harvest_recursive(
    day: int = 0,
    count: int = 1
) -> None:
    """
    Displays a countdown of the days until harvest recursively.

    Parameters
    ----------
    day
        Number of days remaining before harvest.
    count
        Current day for the countdown.
    """
    if day == 0:
        day = int(input("Days until harvest: "))
    if count <= day:
        print(f"Day {count}")
        ft_count_harvest_recursive(day, count + 1)
    else:
        print("Harvest time!")
