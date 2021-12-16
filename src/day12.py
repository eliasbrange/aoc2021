from typing import Iterator, Tuple, DefaultDict
from common import read_file
from collections import defaultdict


def star1(data: Iterator) -> int:
    edges: DefaultDict[str, list[str]] = defaultdict(list)

    for e1, e2 in data:
        edges[e1].append(e2)
        edges[e2].append(e1)

    def count(path: list[str], node) -> int:
        path.append(node)

        if node == "end":
            return 1

        counts = 0
        for nxt in edges[node]:
            if nxt.islower() and nxt in path:
                continue
            counts += count(path.copy(), nxt)

        return counts

    counts = sum([count(["start"], node) for node in edges["start"]])
    return counts


def star2(data: Iterator) -> int:
    edges: DefaultDict[str, list[str]] = defaultdict(list)

    for e1, e2 in data:
        if e2 != "start":
            edges[e1].append(e2)

        if e1 != "start":
            edges[e2].append(e1)

    def count(path: list[str], node, small_visited=False) -> int:
        path.append(node)
        if node == "end":
            return 1

        counts = 0
        for nxt in edges[node]:
            if nxt.islower() and nxt in path:
                if small_visited:
                    continue
                else:
                    counts += count(path.copy(), nxt, True)
            else:
                counts += count(path.copy(), nxt, small_visited)

        return counts

    counts = sum([count(["start"], node, False) for node in edges["start"]])
    return counts


def _fmt_data(data: str) -> Tuple[str, str]:
    parts = data.split("-")
    return parts[0], parts[1]


if __name__ == "__main__":
    res1 = star1(read_file("../inputs/day12.txt", _fmt_data))
    print(f"Star 1: {res1}")

    res2 = star2(read_file("../inputs/day12.txt", _fmt_data))
    print(f"Star 2: {res2}")
