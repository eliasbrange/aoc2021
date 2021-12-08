from typing import Iterator, Tuple
from common import read_file


def star1(data: Iterator) -> int:
    count = 0

    for _, outputs in data:
        for out in outputs:
            if len(out) in [2, 4, 3, 7]:
                count += 1

    return count


def _diff(a: str, b: str) -> set[str]:
    return set(a).symmetric_difference(set(b))


def solve_output(signals: list[str], outputs: list[str]) -> int:
    d_to_s = {}
    s_to_d = {}

    # Set known
    for sig in signals:
        sig = "".join(sorted(sig))
        if len(sig) == 2:
            d_to_s[1] = sig
            s_to_d[sig] = 1
        elif len(sig) == 4:
            d_to_s[4] = sig
            s_to_d[sig] = 4
        elif len(sig) == 3:
            d_to_s[7] = sig
            s_to_d[sig] = 7
        elif len(sig) == 7:
            d_to_s[8] = sig
            s_to_d[sig] = 8
        else:
            s_to_d[sig] = -1

    # 3 is the only digit with 5 segments that inclues the entire 1 segment
    for key in s_to_d:
        if len(key) != 5:
            continue

        if all(x in key for x in d_to_s[1]):
            s_to_d[key] = 3
            d_to_s[3] = key
            break

    # 9 has 6 segments and shares all but one with 3
    for key in s_to_d:
        if len(key) == 6 and len(_diff(key, d_to_s[3])) == 1:
            s_to_d[key] = 9
            d_to_s[9] = key
            break

    # 0 is the only 6 segment left that includes all segments from 1
    for key, v in s_to_d.items():
        if v == -1 and len(key) == 6 and all(x in key for x in d_to_s[1]):
            s_to_d[key] = 0
            d_to_s[0] = key
            break

    # 6 is the remaining 6 segment left
    for key, v in s_to_d.items():
        if v == -1 and len(key) == 6:
            s_to_d[key] = 6
            d_to_s[6] = key
            break

    # 5 has 5 segments and should only have one segment difference with 6
    for key in s_to_d:
        if len(key) == 5 and len(_diff(key, d_to_s[6])) == 1:
            s_to_d[key] = 5
            d_to_s[5] = key
            break

    # 2 is the last segment
    for key, v in s_to_d.items():
        if v == -1:
            s_to_d[key] = 2
            d_to_s[2] = key
            break

    numbers = [s_to_d["".join(sorted(output))] for output in outputs]
    res = int("".join(map(str, numbers)))
    return res


def star2(data: Iterator) -> int:
    res = 0
    for signals, outputs in data:
        res += solve_output(signals, outputs)

    return res


def _fmt_data(input: str) -> Tuple[list[str], list[str]]:
    signals, output = input.split("|")
    return signals.split(), output.split()


if __name__ == "__main__":
    res1 = star1(read_file("../inputs/day8.txt", _fmt_data))
    print(f"Star 1: {res1}")

    res2 = star2(read_file("../inputs/day8.txt", _fmt_data))
    print(f"Star 2: {res2}")
