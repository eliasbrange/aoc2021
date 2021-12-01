from common import read_file


def star1(data):
    cur = next(data)
    count = 0

    for measurement in data:
        if measurement > cur:
            count += 1
        cur = measurement

    return count


def star2(data):
    x1 = next(data)
    x2 = next(data)
    x3 = next(data)

    count = 0

    for measurement in data:
        if x2 + x3 + measurement > x1 + x2 + x3:
            count += 1

        x1, x2, x3 = x2, x3, measurement

    return count


if __name__ == '__main__':
    res1 = star1(read_file('../inputs/day1.txt', int))
    print(f"Star 1: {res1}")

    res2 = star2(read_file('../inputs/day1.txt', int))
    print(f"Star 2: {res2}")
