from typing import Iterator, NamedTuple
from common import read_file

class ClosingChar(NamedTuple):
    exp: str
    score: int

CLOSING_CHARS = {
    ")": ClosingChar(exp="(", score=3),
    "]": ClosingChar(exp="[", score=57),
    "}": ClosingChar(exp="{", score=1197),
    ">": ClosingChar(exp="<", score=25137),
}

def star1(data: Iterator) -> int:
    score = 0

    for line in data:
        stack: list[str] = []
        for char in line:
            if char in CLOSING_CHARS:
                c = CLOSING_CHARS[char]
                if stack.pop() != c.exp:
                    score += c.score
                    break
            else:
                stack.append(char)

    return score


def completion_score(string: str) -> int:
    CHAR_SCORE = {
        "(": 1,
        "[": 2,
        "{": 3,
        "<": 4,
    }

    score = 0
    for char in string:
        score *= 5
        score += CHAR_SCORE[char]

    return score


def star2(data: Iterator) -> int:
    scores = []

    for line in data:
        stack: list[str] = []
        for char in line:
            if char in CLOSING_CHARS:
                c = CLOSING_CHARS[char]
                if stack.pop() != c.exp:
                    # Corrupted
                    break
            else:
                stack.append(char)
        else:
            scores.append(completion_score("".join(stack[::-1])))

    scores = sorted(scores)
    middle_idx = (len(scores) - 1) // 2
    return scores[middle_idx]


if __name__ == "__main__":
    res1 = star1(read_file("../inputs/day10.txt"))
    print(f"Star 1: {res1}")

    res2 = star2(read_file("../inputs/day10.txt"))
    print(f"Star 2: {res2}")
