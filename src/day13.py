from typing import DefaultDict, Tuple
from collections import defaultdict


def solve(
    coords: DefaultDict[Tuple[int, int], int],
    folds: list[Tuple[str, int]],
) -> DefaultDict[Tuple[int, int], int]:
    new_coords = []
    for fold_ori, fold_pos in folds:
        for (cx, cy), v in coords.items():
            if fold_ori == "x":
                if cx > fold_pos and v > 0:
                    coords[(cx, cy)] = 0
                    new_x = fold_pos - (cx - fold_pos)
                    new_coords.append((new_x, cy))
            else:
                if cy > fold_pos and v > 0:
                    coords[(cx, cy)] = 0
                    new_y = fold_pos - (cy - fold_pos)
                    new_coords.append((cx, new_y))

        for coord in new_coords:
            coords[coord] += 1

        new_coords.clear()

    return coords


def star1(
    coords: DefaultDict[Tuple[int, int], int],
    folds: list[Tuple[str, int]],
) -> int:
    coords = solve(coords, folds[:1])
    return sum([1 for v in coords.values() if v > 0])


def star2(
    coords: DefaultDict[Tuple[int, int], int],
    folds: list[Tuple[str, int]],
):
    coords = solve(coords, folds)

    for y in range(10):
        for x in range(40):
            if coords[(x, y)] > 0:
                print("#", end="")
            else:
                print(".", end="")
        print("")


def _fmt_data(str: str) -> str:
    return str


if __name__ == "__main__":
    coords: DefaultDict[Tuple[int, int], int] = defaultdict(int)
    folds: list[Tuple[str, int]] = []

    with open("../inputs/day13.txt") as f:
        line = f.readline().strip()

        while line != "":
            a, b = line.split(",")
            coords[(int(a), int(b))] += 1

            line = f.readline().strip()

        for line in f.readlines():
            if line.strip() == "":
                break

            parts = line.split("=")
            pos = int(parts[1])
            if "x" in parts[0]:
                folds.append(("x", pos))
            else:
                folds.append(("y", pos))

    res1 = star1(coords.copy(), folds)
    print(f"Star 1: {res1}")

    res2 = star2(coords.copy(), folds)
    print(f"Star 2: {res2}")
