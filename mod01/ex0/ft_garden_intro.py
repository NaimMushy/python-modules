def main() -> None:
    """
    Displays a garden introduction.
    """
    plant_name = "lilac"
    plant_height = "42"
    plant_age = "666"
    print("=== Welcome to My Garden ===")
    print(
        f"plant: {plant_name}\n"
        f"height: {plant_height}cm\n"
        f"age: {plant_age}days"
    )
    print("\n=== THE END === ")


if __name__ == "__main__":
    main()
