from typing import Iterator, Set, Tuple
from common import read_file


def star1(data: Iterator) -> int:
    heightmap = []
    for row in data:
        heightmap.append(row)

    res = 0

    for i, row in enumerate(heightmap):
        for j in range(len(heightmap[i])):
            if i != 0 and row[j] >= heightmap[i-1][j]:
                continue

            if j != 0 and row[j] >= row[j-1]:
                continue

            if i != len(heightmap) - 1 and row[j] >= heightmap[i+1][j]:
                continue

            if j != len(row) - 1 and row[j] >= row[j+1]:
                continue

            res += row[j] + 1

    return res


class DFS:
    def __init__(self, heightmap: list[list[int]]):
        self.hm = heightmap
        self.h = len(self.hm)
        self.w = len(self.hm[0])
        self.visited: Set[Tuple[int, int]] = set()

    def solve(self, i: int, j: int):
        if i < 0 or i > self.h - 1 or j < 0 or j > self.w - 1:
            return 0

        if (i, j) in self.visited or self.hm[i][j] == 9:
            return 0

        self.visited.add((i, j))

        adj = [
            self.solve(i-1, j),
            self.solve(i+1, j),
            self.solve(i, j-1),
            self.solve(i, j+1),
        ]

        return 1 + sum(adj)


def star2(data: Iterator) -> int:
    heightmap = []
    for row in data:
        heightmap.append(row)

    dfs = DFS(heightmap)
    res = []

    for i, row in enumerate(heightmap):
        for j in range(len(heightmap[i])):
            if i != 0 and row[j] >= heightmap[i-1][j]:
                continue

            if j != 0 and row[j] >= row[j-1]:
                continue

            if i != len(heightmap) - 1 and row[j] >= heightmap[i+1][j]:
                continue

            if j != len(row) - 1 and row[j] >= row[j+1]:
                continue

            res.append(dfs.solve(i, j))

    res = sorted(res, reverse=True)
    return res[0] * res[1] * res[2]


def _fmt_data(data: str) -> list[int]:
    return list(map(int, data))


if __name__ == "__main__":
    res1 = star1(read_file("../inputs/day9.txt", _fmt_data))
    print(f"Star 1: {res1}")

    res2 = star2(read_file("../inputs/day9.txt", _fmt_data))
    print(f"Star 2: {res2}")
