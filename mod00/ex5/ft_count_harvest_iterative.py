def ft_count_harvest_iterative() -> None:
    day = int(input("days until harvest: "))
    count = 1
    while count <= day:
        print(f"day {count}")
        count += 1
    print("harvest time!")
