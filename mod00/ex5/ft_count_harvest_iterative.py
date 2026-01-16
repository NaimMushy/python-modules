def ft_count_harvest_iterative() -> None:
    """
    Displays a countdown of the days until harvest iteratively.
    """
    day = int(input("days until harvest: "))
    count = 1
    while count <= day:
        print(f"day {count}")
        count += 1
    print("harvest time!")
