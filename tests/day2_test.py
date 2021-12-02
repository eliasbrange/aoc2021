from day2 import star1, star2

TEST_DATA = [
    ("forward", 5),
    ("down", 5),
    ("forward", 8),
    ("up", 3),
    ("down", 8),
    ("forward", 2),
]


def test_star1():
    assert star1(iter(TEST_DATA)) == 150


def test_star2():
    assert star2(iter(TEST_DATA)) == 900


