class Plant:
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name
        self.height = height
        self.age = age

    def grow(self) -> None:
        self.height += 1

    def aging(self) -> None:
        self.age += 1

    def get_info(self) -> None:
        print(
            f"{self.name.capitalize()}: "
            f"{self.height}cm, {self.age} days old"
        )


def ft_plant_growth() -> None:
    p1 = Plant("rose", 25, 30)
    p2 = Plant("petunia", 10, 6)
    p3 = Plant("rhododendron", 40, 9)
    plants: list[Plant] = []
    plants.append(p1)
    plants.append(p2)
    plants.append(p3)
    for p in plants:
        initial_growth = p.height
        for i in range(1, 8):
            print(f"=== Day {i} ===")
            p.get_info()
            if i < 7:
                p.grow()
                p.aging()
        end_growth = p.height
        print(f"growth this week: +{end_growth - initial_growth}cm")


if __name__ == "__main__":
    ft_plant_growth()
