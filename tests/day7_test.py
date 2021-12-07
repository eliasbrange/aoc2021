from day7 import star1, star2

TEST_DATA = [16, 1, 2, 0, 4, 2, 7, 1, 2, 14]


def test_star1():
    assert star1(TEST_DATA) == 37


def test_star2():
    assert star2(TEST_DATA) == 168
