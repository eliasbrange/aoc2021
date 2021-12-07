from common import read_file
from typing import DefaultDict
from collections import defaultdict


def star1(data: list[int]) -> int:
    crabs: DefaultDict[int, int] = defaultdict(int)
    end = 0

    for n in data:
        end = max(n, end)
        crabs[n] += 1

    return min([
        sum([abs(k-pos) * v for k, v in crabs.items()])
        for pos in range(end)
    ])


def _cost(n):
    return int(n * (n + 1) / 2)


def star2(data: list[int]) -> int:
    crabs: DefaultDict[int, int] = defaultdict(int)
    end = 0

    for n in data:
        end = max(n, end)
        crabs[n] += 1

    return min([
        sum([_cost(abs(k-pos)) * v for k, v in crabs.items()])
        for pos in range(end)
    ])


def _fmt_data(str: str) -> list[int]:
    return list(map(int, str.split(",")))


if __name__ == "__main__":
    data = next(read_file("../inputs/day7.txt", _fmt_data))

    res1 = star1(data)
    print(f"Star 1: {res1}")

    res2 = star2(data)
    print(f"Star 2: {res2}")
