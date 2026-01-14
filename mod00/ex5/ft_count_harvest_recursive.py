def ft_count_harvest_recursive(
    day: int = 0,
    count: int = 1
) -> None:
    if day == 0:
        day = int(input("days until harvest: "))
    if count <= day:
        print(f"day {count}")
        ft_count_harvest_recursive(day, count + 1)
    else:
        print("harvest time!")
