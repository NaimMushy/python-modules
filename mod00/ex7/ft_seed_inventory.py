def ft_seed_inventory(
    seed_type: str,
    quantity: int,
    unit: str
) -> None:
    """
    Displays the seed inventory.

    Parameters
    ----------
    seed_type
        The type of the seed.
    quantity
        The quantity available of a seed.
    unit
        The unit type of a seed (packets, grams or square meters).
    """
    if unit == "packets":
        print(f"{seed_type.capitalize()} seeds: {quantity} {unit} available")
    elif unit == "grams":
        print(f"{seed_type.capitalize()} seeds: {quantity} {unit} total")
    elif unit == "area":
        print(
            f"{seed_type.capitalize()} seeds: "
            f"covers {quantity} square meters"
        )
    else:
        print("Unknown unit type")
