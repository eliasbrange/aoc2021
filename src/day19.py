from typing import Tuple
import itertools
from collections import defaultdict

def align(scanner1, scanner2):
    res = []
    location = []
    for dim1 in range(3):
        values = [probe[dim1] for probe in scanner1]
        for (dim2, s) in itertools.product(range(3), [-1, 1]):
            values2 = [probe[dim2] * s for probe in scanner2]

            diffs = defaultdict(int)
            for v1 in values:
                for v2 in values2:
                    diffs[v2 - v1] += 1
            max_diff_key = max(diffs, key=diffs.get)

            if diffs[max_diff_key] >= 12:
                res.append([v2 - max_diff_key for v2 in values2])
                location.append(max_diff_key)
                break
        else:
            return None

    return (list(zip(res[0], res[1], res[2])), location)


def stars(scanners) -> Tuple[int, int]:
    beacons = set()

    next = [scanners[0]]
    scanner_locations = [(0, 0, 0)]

    while next:
        aligned = next.pop()
        rest = []
        for scanner in scanners:
            res = align(aligned, scanner)
            if res:
                (aligned_scanner, scanner_location) = res
                scanner_locations.append(scanner_location)
                next.append(aligned_scanner)
            else:
                rest.append(scanner)
        scanners = rest
        beacons.update(aligned)

    loc = itertools.product(scanner_locations, scanner_locations)
    manhattan = (sum(abs(a-b) for (a, b) in zip(d1, d2)) for (d1, d2) in loc)
    return len(beacons), max(manhattan)


if __name__ == "__main__":
    scanners = []
    with open("../inputs/day19.txt") as f:
        for line in f.readlines():
            line = line.strip()

            if line == "":
                continue

            if line.startswith("---"):
                scanner: list[Tuple[int, int, int]] = []
                scanners.append(scanner)
                continue

            (x, y, z) = line.split(",")
            scanner.append((int(x), int(y), int(z)))

    res1, res2 = stars(scanners)
    print(f"Star 1: {res1}")
    print(f"Star 2: {res2}")
