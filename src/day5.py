from typing import Iterator
from common import read_file
from collections import namedtuple


Line = namedtuple("Line", field_names=["x1", "y1", "x2", "y2"])


def star1(data: Iterator[Line]) -> int:
    map = [[0] * 1000 for i in range(1000)]

    for line in data:
        if line.x1 == line.x2:
            x_range = [line.x1] * (abs(line.y2 - line.y1) + 1)
            y_sign = 1 if line.y2 >= line.y1 else -1
            y_range = list(range(line.y1, line.y2 + y_sign, y_sign))
        elif line.y1 == line.y2:
            y_range = [line.y1] * (abs(line.x2 - line.x1) + 1)
            x_sign = 1 if line.x2 >= line.x1 else -1
            x_range = list(range(line.x1, line.x2 + x_sign, x_sign))
        else:
            continue

        for i, x in enumerate(x_range):
            map[x][y_range[i]] += 1

    res = sum([sum(i > 1 for i in row) for row in map])
    return res


def star2(data: Iterator[Line]) -> int:
    map = [[0] * 1000 for i in range(1000)]

    for line in data:
        if line.x1 == line.x2:
            x_range = [line.x1] * (abs(line.y2 - line.y1) + 1)
        else:
            x_sign = 1 if line.x2 >= line.x1 else -1
            x_range = list(range(line.x1, line.x2 + x_sign, x_sign))

        if line.y1 == line.y2:
            y_range = [line.y1] * (abs(line.x2 - line.x1) + 1)
        else:
            y_sign = 1 if line.y2 >= line.y1 else -1
            y_range = list(range(line.y1, line.y2 + y_sign, y_sign))

        for i, x in enumerate(x_range):
            map[x][y_range[i]] += 1

    res = sum([sum(i > 1 for i in row) for row in map])
    return res


def _fmt_data(str: str) -> Line:
    p1, p2 = str.split(" -> ")
    x1, y1 = p1.split(",")
    x2, y2 = p2.split(",")

    return Line(int(x1), int(y1), int(x2), int(y2))


if __name__ == "__main__":
    res1 = star1(read_file("../inputs/day5.txt", _fmt_data))
    print(f"Star 1: {res1}")

    res2 = star2(read_file("../inputs/day5.txt", _fmt_data))
    print(f"Star 2: {res2}")
