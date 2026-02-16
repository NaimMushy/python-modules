import alchemy


def direct_access(elements: list[str]) -> None:
    print("\nTesting direct module access:")
    for element in elements:
        print(
            f"alchemy.elements.{element}(): "
            f"{getattr(alchemy.elements, element)()}"
        )


def package_lvl_access(elements: list[str]) -> None:
    print(
        "\nTesting package-level access"
        "(controlled by __init__.py):"
    )
    for element in elements:
        try:
            print(f"alchemy.{element}(): ", end="")
            print(getattr(alchemy, element)())
        except AttributeError:
            print("AttributeError - Not exposed")


def main() -> None:
    print("\n=== Sacred Scroll Mastery ===")
    elements: list[str] = [
        "create_fire",
        "create_water",
        "create_earth",
        "create_air"
    ]
    direct_access(elements)
    package_lvl_access(elements)
    print("\nPackage metadata:")
    print(f"Version: {alchemy.__version__}")
    print(f"Author: {alchemy.__author__}")


if __name__ == "__main__":
    main()
