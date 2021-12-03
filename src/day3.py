from typing import Iterator, List
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


def _get_ratings(data: List[str], ox: bool, index: int = 0) -> int:
    if len(data) == 1:
        return int(data[0], 2)

    ones = []
    zeroes = []

    for line in data:
        if line[index] == "1":
            ones.append(line)
        else:
            zeroes.append(line)

    if ox:
        if len(ones) >= len(zeroes):
            return _get_ratings(ones, ox=True, index=index + 1)
        else:
            return _get_ratings(zeroes, ox=True, index=index + 1)
    else:
        if len(ones) >= len(zeroes):
            return _get_ratings(zeroes, ox=False, index=index + 1)
        else:
            return _get_ratings(ones, ox=False, index=index + 1)


def star2(data):
    data = list(data)

    ox = _get_ratings(data, ox=True)
    co = _get_ratings(data, ox=False)

    return ox * co


def _fmt_data(str):
    return str


if __name__ == "__main__":
    res1 = star1(read_file("../inputs/day3.txt", _fmt_data))
    print(f"Star 1: {res1}")

    res2 = star2(read_file("../inputs/day3.txt", _fmt_data))
    print(f"Star 2: {res2}")
