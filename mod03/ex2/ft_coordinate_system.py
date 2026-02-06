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
    x: int = coor[0]
    y: int = coor[1]
    z: int = coor[2]
    print(f"Player at x={x}, y={y}, z={z}")
    print(f"Coordinates: X={x}, Y={y}, Z={z}")


def main() -> None:
    print("=== Game Coordinate System ===\n")
    pos_tab: list[tuple] = []
    pos_tab.append((16, 4, 6))
    print(f"Position created: {pos_tab[0]}")
    calculate_dist((0, 0, 0), pos_tab[0])
    if len(sys.argv) > 1:
        for coor in range(1, len(sys.argv)):
            print(f"Parsing coordinates: \"{sys.argv[coor]}\"")
            coor_str: list[str] = sys.argv[coor].split(",")
            nb_coor: list[int] = []
            try:
                for c in coor_str:
                    nb_coor.append(int(c))
            except ValueError:
                print(
                    "Caught ValueError while parsing coordinates: "
                    f"Invalid literal for int() with base 10: '{c}'\n"
                )
            else:
                coor_tup = tuple(nb_coor)
                print(f"Parsed position: {coor_tup}")
                calculate_dist((0, 0, 0), coor_tup)
                pos_tab.append(coor_tup)
    else:
        print(
            "No coordinates given to parse - Usage: "
            "ft_coordinate_system.py '<x1,y1,z1>' '<x2,y2,z2>' ...\n"
        )
    unpack_demon(pos_tab[-1])


if __name__ == "__main__":
    main()
