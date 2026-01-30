class Plant:
    """
    A class that represents a plant.
    """
    def __init__(
        self,
        name: str,
        height: int,
        age: int
    ) -> None:
        """
        Initializes the plant's data.

        Parameters
        ----------
        name
            The plant's name.
        height
            The plant's height.
        age
            The plant's age.
        """
        self.name: str = name.capitalize()
        print(f"Plant created: {self.name}")
        self.set_height(height)
        self.set_age(age)

    def set_height(self, new_height: int) -> None:
        """
        Verifies and updates plant's height.

        Parameters
        ----------
        new_height
            The plant's new height.
        """
        if isinstance(new_height, int) and new_height >= 0:
            self._height: int = new_height
            print(f"Height updated: {new_height}cm [OK]")
        else:
            print(
                f"\nInvalid operation attempted: height "
                f"{new_height}cm [REJECTED]\n"
                f"Security: Negative height rejected\n"
            )

    def set_age(self, new_age: int) -> None:
        """
        Verifies and updates plant's age.

        Parameters
        ----------
        new_age
            The plant's new age.
        """
        if isinstance(new_age, int) and new_age >= 0:
            self._age: int = new_age
            print(f"Age updated: {new_age} days [OK]")
        else:
            print(
                f"\nInvalid operation attempted: age "
                f"{new_age} days [REJECTED]\n"
                f"Security: Negative age rejected\n"
            )

    def get_height(self) -> int:
        """
        Returns
        -------
        int
            The plant's height.
        """
        return self._height

    def get_age(self) -> int:
        """
        Returns
        -------
        int
            The plant's age.
        """
        return self._age

    def get_plant_info(self) -> None:
        """
        Displays the plant's data.
        """
        print(
            f"Current plant: {self.name} "
            f"({self.get_height()}cm, {self.get_age()} days)"
        )


def main() -> None:
    print("=== Garden Security System ===")
    p1: Plant = Plant("lilac", 16, 44)
    p1.set_height(-666)
    p1.get_plant_info()


if __name__ == "__main__":
    main()
