from day6 import star1, star2

TEST_DATA = [3, 4, 3, 1, 2]


def test_star1():
    assert star1(TEST_DATA) == 5934


def test_star2():
    assert star2(TEST_DATA) == 26984457539
