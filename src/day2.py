from common import read_file


def star1(data):
    x = 0
    y = 0

    for direction, amount in data:
        if direction == "forward":
            x += amount
        elif direction == "up":
            y -= amount
        elif direction == "down":
            y += amount

    return x * y


def star2(data):
    x = 0
    y = 0
    aim = 0

    for direction, amount in data:
        if direction == "forward":
            x += amount
            y += aim * amount
        elif direction == "up":
            aim -= amount
        elif direction == "down":
            aim += amount

    return x * y


def _fmt_data(str):
    direction, amount = str.split()
    return direction, int(amount)


if __name__ == '__main__':
    res1 = star1(read_file('../inputs/day2.txt', _fmt_data))
    print(f"Star 1: {res1}")

    res2 = star2(read_file('../inputs/day2.txt', _fmt_data))
    print(f"Star 2: {res2}")
