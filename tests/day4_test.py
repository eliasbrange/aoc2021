import pytest
from day4 import star1, star2, Board

TEST_NUMBERS = [
    7,
    4,
    9,
    5,
    11,
    17,
    23,
    2,
    0,
    14,
    21,
    24,
    10,
    16,
    13,
    6,
    15,
    25,
    12,
    22,
    18,
    20,
    8,
    19,
    3,
    26,
    1,
]


@pytest.fixture
def test_boards():
    boards = []

    board1 = Board()
    board1.rows = [
        [22, 13, 17, 11, 0],
        [8, 2, 23, 4, 24],
        [21, 9, 14, 16, 7],
        [6, 10, 3, 18, 5],
        [1, 12, 20, 15, 19],
    ]
    board1.setup()
    boards.append(board1)

    board2 = Board()
    board2.rows = [
        [3, 15, 0, 2, 22],
        [9, 18, 13, 17, 5],
        [19, 8, 7, 25, 23],
        [20, 11, 10, 24, 4],
        [14, 21, 16, 12, 6],
    ]
    board2.setup()
    boards.append(board2)

    board3 = Board()
    board3.rows = [
        [14, 21, 17, 24, 4],
        [10, 16, 15, 9, 19],
        [18, 8, 23, 26, 20],
        [22, 11, 13, 6, 5],
        [2, 0, 12, 3, 7],
    ]
    board3.setup()
    boards.append(board3)

    return boards


def test_star1(test_boards):
    assert star1(test_boards, TEST_NUMBERS) == 4512


def test_star2(test_boards):
    assert star2(test_boards, TEST_NUMBERS) == 1924
