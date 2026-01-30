def main() -> None:
    """
    Displays a garden introduction.
    """
    plant_name: str = "Hellebore"
    plant_height: int = 42
    plant_age: int = 666
    print("=== Welcome to My Garden ===")
    print(
        f"Plant: {plant_name}\n"
        f"Height: {plant_height}cm\n"
        f"Age: {plant_age} days"
    )
    print("\n=== End of Program === ")


if __name__ == "__main__":
    main()
