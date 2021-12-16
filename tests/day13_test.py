from day13 import star1
from collections import defaultdict

TEST_COORDS = defaultdict(int, {
    (6, 10): 1,
    (0, 14): 1,
    (9, 10): 1,
    (0, 3): 1,
    (10, 4): 1,
    (4, 11): 1,
    (6, 0): 1,
    (6, 12): 1,
    (4, 1): 1,
    (0, 13): 1,
    (10, 12): 1,
    (3, 4): 1,
    (3, 0): 1,
    (8, 4): 1,
    (1, 10): 1,
    (2, 14): 1,
    (8, 10): 1,
    (9, 0): 1,
})

TEST_FOLDS = [
    ("y", 7),
    ("x", 5),
]


def test_solve():
    assert star1(TEST_COORDS.copy(), TEST_FOLDS[:1]) == 17
