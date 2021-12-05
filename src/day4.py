from typing import List


class Board:
    def __init__(self):
        self.cols = []
        self.rows = []
        self.is_complete = False

    def setup(self):
        self.cols = [[0] * 5 for i in range(5)]
        for j in range(5):
            for i in range(5):
                self.cols[j][i] = self.rows[i][j]

    def check_number(self, n: int):
        for i in range(5):
            if n in self.rows[i]:
                self.rows[i].remove(n)
                if len(self.rows[i]) == 0:
                    self.is_complete = True
                    return sum(sum(r) for r in self.rows) * n

            if n in self.cols[i]:
                self.cols[i].remove(n)
                if len(self.cols[i]) == 0:
                    self.is_complete = True
                    return sum(sum(r) for r in self.cols) * n

        return 0


def star1(boards: List[Board], numbers: List[int]) -> int:
    for n in numbers:
        for board in boards:
            res = board.check_number(n)
            if res > 0:
                return res

    return 0


def star2(boards: List[Board], numbers: List[int]) -> int:
    last_score = None

    for n in numbers:
        for board in boards:
            if board.is_complete:
                continue

            res = board.check_number(n)
            if res > 0:
                last_score = res

    return last_score


if __name__ == "__main__":
    numbers = None
    boards = []

    with open("../inputs/day4.txt") as f:
        numbers = map(int, f.readline().split(","))
        f.readline()

        board = Board()
        for line in f:
            if line.strip() == "":
                board.setup()
                boards.append(board)
                board = Board()
                continue

            print(line)
            board.rows.append(list(map(int, line.strip().split())))

    res1 = star1(boards, numbers)
    print(f"Star 1: {res1}")

    res2 = star2(boards, numbers)
    print(f"Star 2: {res2}")
