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
            the plant's name
        height
            the plant's height
        age
            the plant's age
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
            the plant's new height
        """
        if type(new_height) is int and new_height >= 0:
            self._height = new_height
            print(f"height updated: {new_height}cm [OK]")
        else:
            self._height = 0
            print(
                f"invalid operation attempted: height "
                f"{new_height}cm [REJECTED]\n"
                f"security: negative height rejected"
            )

    def set_age(self, new_age: int) -> None:
        """
        Verifies and updates plant's age.

        Parameters
        ----------
        new_age
            the plant's new age
        """
        if type(new_age) is int and new_age >= 0:
            self._age = new_age
            print(f"age updated: {new_age} days [OK]")
        else:
            self._age = 0
            print(
                f"invalid operation attempted: age "
                f"{new_age} days [REJECTED]\n"
                f"security: negative age rejected"
            )

    def get_height(self) -> int:
        """

        Returns
        -------
        int
            the plant's height
        """
        return self._height

    def get_age(self) -> int:
        """

        Returns
        -------
        int
            the plant's age
        """
        return self._age
