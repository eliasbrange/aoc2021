from collections import defaultdict
from typing import DefaultDict, NamedTuple, Tuple
from common import read_file
from heapq import heappop, heappush


class Edge(NamedTuple):
    a: Tuple[int, int]
    b: Tuple[int, int]
    cost: int


def dijkstra(
    graph: list[Edge],
    source: Tuple[int, int],
    target: Tuple[int, int],
) -> int:
    edges = defaultdict(list)
    for edge in graph:
        edges[edge.a].append((edge.cost, edge.b))

    dist: DefaultDict[Tuple[int, int], int] = defaultdict(int)
    dist[source] = 0

    queue = [(0, source)]  # prio, coords
    while queue:
        cost, (x, y) = heappop(queue)
        if cost != dist[(x, y)]:
            # instead of decrease key
            continue

        for e_cost, e_coord in edges[(x, y)]:
            new_cost = dist[(x, y)] + e_cost
            if e_coord not in dist or new_cost < dist[(e_coord)]:
                dist[e_coord] = new_cost
                heappush(queue, (new_cost, e_coord))

    return dist[target]


def create_graph(data: list[list[int]], repeat=1) -> list[Edge]:
    height = len(data)
    width = len(data[0])

    edges: list[Edge] = []

    for y in range(height):
        for x in range(width):
            if x < width - 1:
                edges.append(Edge((x, y), (x + 1, y), data[y][x + 1]))
                edges.append(Edge((x + 1, y), (x, y), data[y][x]))

            if y < height - 1:
                edges.append(Edge((x, y), (x, y + 1), data[y + 1][x]))
                edges.append(Edge((x, y + 1), (x, y), data[y][x]))

    return edges


def extend_data(data: list[list[int]], n: int = 5) -> list[list[int]]:
    height = len(data)
    width = len(data[0])
    extended_data = [[0] * n * width for _ in range(n * height)]

    for y in range(n * width):
        for x in range(n * height):
            orig = data[y % height][x % width]
            value = (y // height + x // width + orig)
            value = value % 9 if value > 9 else value
            extended_data[y][x] = value

    return extended_data


def star1(data: list[list[int]]) -> int:
    height = len(data)
    width = len(data[0])
    graph = create_graph(data)

    return dijkstra(graph, (0, 0), (width - 1, height - 1))


def star2(data: list[list[int]]) -> int:
    height = len(data) * 5
    width = len(data[0]) * 5
    graph = create_graph(extend_data(data))

    return dijkstra(graph, (0, 0), (width - 1, height - 1))


def _fmt_data(data: str) -> list[int]:
    return list(map(int, list(data)))


if __name__ == "__main__":
    graph = []
    for line in read_file("../inputs/day15.txt", _fmt_data):
        graph.append(line)

    res1 = star1(graph)
    print(f"Star 1: {res1}")

    res2 = star2(graph)
    print(f"Star 2: {res2}")
