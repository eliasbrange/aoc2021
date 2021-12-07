from typing import Iterator
from common import read_file


def get_fish_count(data: list[int], days: int) -> int:
    fishes = [0] * 9
    for n in data:
        fishes[n] += 1

    for i in range(days):
        new = fishes[0]
        for i in range(8):
            fishes[i] = fishes[i+1]

        fishes[6] += new
        fishes[8] = new

    return sum(fishes)

def star1(data: list[int]) -> int:
    return(get_fish_count(data, 80))


def star2(data: list[int]) -> int:
    return(get_fish_count(data, 256))


def _fmt_data(str: str) -> list[int]:
    return list(map(int, str.split(",")))


if __name__ == "__main__":
    data = next(read_file("../inputs/day6.txt", _fmt_data))
    res1 = star1(data)
    print(f"Star 1: {res1}")

    res2 = star2(data)
    print(f"Star 2: {res2}")
