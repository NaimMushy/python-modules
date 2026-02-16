def healing_potion() -> str:
    from .elements import create_fire, create_water
    return (
        "Healing potion brewed with "
        f"{create_fire()} and {create_water()}"
    )


def strength_potion() -> str:
    from .elements import create_earth, create_fire
    return (
        "Strength potion brewed with "
        f"{create_earth()} and {create_fire()}"
    )


def invisibility_potion() -> str:
    from .elements import create_air, create_water
    return (
        "Invisibility potion brewed with "
        f"{create_air()} and {create_water()}"
    )


def wisdom_potion() -> str:
    from .elements import create_fire, create_water, create_earth, create_air
    return (
        "Wisdom potion brewed with all elements: "
        f"{create_fire()} - {create_water()} "
        f"- {create_earth()} - {create_air()}"
    )
