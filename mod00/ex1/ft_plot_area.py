def ft_plot_area() -> None:
    """
    Displays the area of a plot based on user input.
    """
    length: int = int(input("Enter length: "))
    width: int = int(input("Enter width: "))
    print(f"Plot area: {length * width}")
