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
        self.name = name
        print(f"plant created: {self.name}")
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
        if type(new_height) is int and new_height >= 0:
            self._height = new_height
            print(f"height updated: {new_height}cm [OK]")
        else:
            self._height = 0
            print(
                f"invalid operation attempted: height "
                f"{new_height}cm [REJECTED]\n"
                f"security: negative height rejected\n"
            )

    def set_age(self, new_age: int) -> None:
        """
        Verifies and updates plant's age.

        Parameters
        ----------
        new_age
            The plant's new age.
        """
        if type(new_age) is int and new_age >= 0:
            self._age = new_age
            print(f"age updated: {new_age} days [OK]")
        else:
            self._age = 0
            print(
                f"invalid operation attempted: age "
                f"{new_age} days [REJECTED]\n"
                f"security: negative age rejected\n"
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
            f"current plant: {self.name} "
            f"({self.get_height}cm, {self.get_age} days)"
        )


def main() -> None:
    print("=== Garden Security System ===")
    p1 = Plant("lilac", 16, 44)
    p1.set_height(-666)
    p1.get_plant_info()


if __name__ == "__main__":
    main()
