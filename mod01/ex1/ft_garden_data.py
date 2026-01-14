class Plant:
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name
        self.height = height
        self.age = age

    def display_info(self) -> None:
        print(f"{self.name}: {self.height}cm, {self.age} days old")


def ft_garden_data() -> None:
    plants: list[Plant] = []
    plant1 = Plant("anneau de cinabre", 40075017000, 666)
    plant2 = Plant("baltrou", -10000000, 53)
    plant3 = Plant("trou qui pète", 1, 0)
    plants.append(plant1)
    plants.append(plant2)
    plants.append(plant3)
    print("=== Garden Plant Registry ===")
    for plant in plants:
        plant.display_info()


if __name__ == "__main__":
    ft_garden_data()
