from typing import DefaultDict
from collections import defaultdict
from math import ceil


def solve2(polymer: str, pairs: dict[str, str], steps: int) -> int:
    pair_counts: DefaultDict[str, int] = defaultdict(int)
    for i in range(len(polymer) - 1):
        pair = polymer[i:i+2]
        pair_counts[pair] += 1

    for _ in range(steps):
        for key, value in list(pair_counts.items()):
            if value > 0 and key in pairs:
                pair_counts[key[0] + pairs[key]] += value
                pair_counts[pairs[key] + key[1]] += value
                pair_counts[key] -= value

    sums: DefaultDict[str, int] = defaultdict(int)
    for key, value in pair_counts.items():
        sums[key[0]] += value
        sums[key[1]] += value

    sum_values = sums.values()
    return ceil(max(sum_values) / 2) - ceil(min(sum_values) / 2)


def star1(polymer: str, pairs: dict[str, str]) -> int:
    return solve2(polymer, pairs, 10)


def star2(polymer: str, pairs: dict[str, str]) -> int:
    return solve2(polymer, pairs, 40)


if __name__ == "__main__":
    with open("../inputs/day14.txt") as f:
        polymer = f.readline().strip()

        pairs: dict[str, str] = {}

        for line in f.readlines():
            line = line.strip()
            if line != "":
                p1, p2 = line.split(" -> ")
                pairs[p1] = p2

        res1 = star1(polymer, pairs)
        print(f"Star 1: {res1}")

        res2 = star2(polymer, pairs)
        print(f"Star 2: {res2}")
