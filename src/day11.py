from typing import Iterator, Set, Tuple
from common import read_file


class OctoMap:
    def __init__(self, data: list[list[int]]):
        self.octomap = data
        self.h = len(self.octomap)
        self.w = len(self.octomap[0])
        self.flashed: Set[Tuple[int, int]] = set()
        self.flashes = 0

    def synchronized(self) -> bool:
        return len(self.flashed) == 100

    def step(self):
        self.flashed.clear()

        for i in range(self.h):
            for j in range(self.w):
                self.increase(i, j)

    def increase(self, i, j):
        if i < 0 or i > self.h - 1 or j < 0 or j > self.w - 1:
            return

        if (i, j) in self.flashed:
            return

        self.octomap[i][j] += 1
        if self.octomap[i][j] > 9:
            self.flash(i, j)

    def flash(self, i, j):
        self.flashed.add((i, j))
        self.octomap[i][j] = 0
        self.flashes += 1

        self.increase(i-1, j-1)
        self.increase(i-1, j)
        self.increase(i-1, j+1)

        self.increase(i, j-1)
        self.increase(i, j+1)

        self.increase(i+1, j-1)
        self.increase(i+1, j)
        self.increase(i+1, j+1)


def star1(data: Iterator) -> int:
    rows = []
    for row in data:
        rows.append(row.copy())

    octomap = OctoMap(rows)

    for i in range(100):
        octomap.step()

    return octomap.flashes


def star2(data: Iterator) -> int:
    rows = []
    for row in data:
        rows.append(row.copy())

    octomap = OctoMap(rows)

    steps = 0
    while not octomap.synchronized():
        steps += 1
        octomap.step()

    return steps


def _fmt_data(data: str) -> list[int]:
    return list(map(int, list(data)))


if __name__ == "__main__":
    res1 = star1(read_file("../inputs/day11.txt", _fmt_data))
    print(f"Star 1: {res1}")

    res2 = star2(read_file("../inputs/day11.txt", _fmt_data))
    print(f"Star 2: {res2}")
