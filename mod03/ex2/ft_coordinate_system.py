import sys
import math


def calculate_dist(coor1: tuple, coor2: tuple) -> None:
    """
    Calculates the distance between two sets of coordinates.

    Parameters
    ----------
    coor1
        The first set of coordinates.
    coor2
        The second set of coordinates.
    """
    x_pos: int = coor2[0] - coor1[0]
    y_pos: int = coor2[1] - coor1[1]
    z_pos: int = coor2[2] - coor1[2]
    dist: float = math.sqrt(x_pos**2 + y_pos**2 + z_pos**2)
    print(f"distance between {coor1} and {coor2}: {dist}\n")


def unpack_demon(coor: tuple) -> None:
    """
    Displays the unpacked coordinates from the tuple.

    Parameters
    ----------
    coor
        The coordinates to unpack.
    """
    print("unpacking demonstration:")
    x: int = coor[0]
    y: int = coor[1]
    z: int = coor[2]
    print(f"player at x={x}, y={y}, z={z}")
    print(f"coordinates: X={x}, Y={y}, Z={z}")


def main() -> None:
    """
    Parses and creates player's coordinates.
    """
    print("=== Game Coordinate System ===\n")
    pos_tab: list[tuple] = []
    pos_tab.append((16, 4, 6))
    print(f"position created: {pos_tab[0]}")
    calculate_dist((0, 0, 0), pos_tab[0])
    if len(sys.argv) > 1:
        for coor in range(1, len(sys.argv)):
            print(f"parsing coordinates: \"{sys.argv[coor]}\"")
            coor_str: str = sys.argv[coor].split(",")
            nb_coor: list[int] = []
            try:
                for c in coor_str:
                    nb_coor.append(int(c))
            except ValueError:
                print(
                    f"error parsing coordinates: invalid literal for int()"
                    f"with base 10: '{c}'\n"
                )
            else:
                coor_tup = tuple(nb_coor)
                calculate_dist((0, 0, 0), coor_tup)
                pos_tab.append(coor_tup)
    unpack_demon(pos_tab[-1])


if __name__ == "__main__":
    main()
