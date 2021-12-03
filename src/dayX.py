from typing import Iterator
from common import read_file


def star1(data: Iterator) -> int:
    return 0

def star2(data: Iterator) -> int:
    return 0

def _fmt_data(str: str) -> str:
    return str

if __name__ == "__main__":
    res1 = star1(read_file("../inputs/day4.txt", _fmt_data))
    print(f"Star 1: {res1}")

    res2 = star2(read_file("../inputs/day4.txt", _fmt_data))
    print(f"Star 2: {res2}")
