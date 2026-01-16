def ft_plot_area() -> None:
    """
    Displays the area of a plot based on user input.
    """
    length: int = int(input("enter length: "))
    width: int = int(input("enter width: "))
    print(f"plot area: {length * width}")
