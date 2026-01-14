class Plant:
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name
        self.height = height
        self.age = age
        print(
            f"created: {self.name.capitalize()} "
            f"({self.height}cm, {self.age} days)"
        )


def ft_plant_factory() -> None:
    plants: list[Plant] = []
    print("=== Plant Factory Output ===")
    for i in range(0, 5):
        name: str = input("name of plant: ")
        height: int = int(input("height of plant: "))
        age: int = int(input("age of plant: "))
        plant = Plant(name, height, age)
        plants.append(plant)
    print(f"total plants created: {len(plants)}")


if __name__ == "__main__":
    ft_plant_factory()
