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
        the type of the seed
    quantity
        the quantity available of a seed
    unit
        the unit type of a seed (packets, grams or square meters)
    """
    if unit == "packets":
        print(f"{seed_type.capitalize()} seeds: {quantity} packets available")
    elif unit == "grams":
        print(f"{seed_type.capitalize()} seeds: {quantity} grams total")
    else:
        print(
            f"{seed_type.capitalize()} seeds: "
            f"covers {quantity} square meters"
        )
