import sys
import math


def calculate_dist(coor1: tuple, coor2: tuple) -> None:
    x_pos: int = coor2[0] - coor1[0]
    y_pos: int = coor2[1] - coor1[1]
    z_pos: int = coor2[2] - coor1[2]
    dist: float = math.sqrt(x_pos**2 + y_pos**2 + z_pos**2)
    print(f"Distance between {coor1} and {coor2}: {round(dist, 2)}\n")


def unpack_demon(coor: tuple) -> None:
    print("Unpacking demonstration:")
    x: int
    y: int
    z: int
    x, y, z = coor
    print(f"Player at x={x}, y={y}, z={z}")
    print(f"Coordinates: X={x}, Y={y}, Z={z}")


def parse_coordinates(coor: tuple | str) -> tuple:
    if isinstance(coor, tuple):
        if len(coor) > 3:
            raise ValueError(
                "Too many coordinates in tuple [REJECTED] - 3 required"
            )
        print(f"Position created: {coor}")
        coor_tup: tuple = coor

    elif isinstance(coor, str):
        print(f"Parsing coordinates: '{coor}'")
        coor_str: list[str] = coor.split(",")
        nb_coor: list[int] = []
        for c in coor_str:
            nb_coor.append(int(c))
        if len(nb_coor) != 3:
            raise ValueError(
                "Inadequate number of coordinates "
                "given as argument [REJECTED] - 3 required"
            )
        coor_tup = tuple(nb_coor)
        print(f"Parsed position: {coor_tup}")

    calculate_dist((0, 0, 0), coor_tup)
    return coor_tup


def main() -> None:
    print("=== Game Coordinate System ===\n")

    pos_tab: list[tuple] = []
    args: list[tuple | str] = [(16, 4, 6)] + sys.argv[1:]
    for coor in args:
        try:
            pos_tab.append(parse_coordinates(coor))
        except ValueError as ve:
            print(f"Caught ValueError while parsing coordinates: {ve}\n")

    if len(args) == 1:
        print(
            "No coordinates given to parse - Usage: "
            "ft_coordinate_system.py '<x1,y1,z1>' '<x2,y2,z2>' ...\n"
        )

    unpack_demon(pos_tab[-1])


if __name__ == "__main__":
    main()
