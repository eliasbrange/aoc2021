from typing import Iterator, List, Tuple
from common import read_file


def star1(data: Iterator) -> int:
    counts: List[int] = []

    for line in data:
        if not counts:
            counts = [0] * len(line)

        for i, x in enumerate(line):
            if x == "1":
                counts[i] += 1
            else:
                counts[i] -= 1

    gamma = int("".join(["1" if x > 0 else "0" for x in counts]), 2)
    epsilon = int("".join(["0" if x > 0 else "1" for x in counts]), 2)

    return gamma * epsilon


def _get_ratings(data: List[str], index: int = 0) -> Tuple[int, int]:
    if len(data) == 1:
        res = int(data[0], 2)
        return res, res

    ones = []
    zeroes = []

    for line in data:
        if line[index] == "1":
            ones.append(line)
        else:
            zeroes.append(line)

    if len(ones) >= len(zeroes):
        most, _ = _get_ratings(ones, index + 1)
        _, least = _get_ratings(zeroes, index + 1)
    else:
        most, _ = _get_ratings(zeroes, index + 1)
        _, least = _get_ratings(ones, index + 1)

    return most, least


def star2(data):
    ox, co = _get_ratings(list(data))
    return ox * co


def _fmt_data(str):
    return str


if __name__ == "__main__":
    res1 = star1(read_file("../inputs/day3.txt", _fmt_data))
    print(f"Star 1: {res1}")

    res2 = star2(read_file("../inputs/day3.txt", _fmt_data))
    print(f"Star 2: {res2}")
