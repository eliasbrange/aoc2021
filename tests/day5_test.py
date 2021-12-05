from day5 import star1, star2, Line

TEST_DATA = [
    Line(0, 9, 5, 9),
    Line(8, 0, 0, 8),
    Line(9, 4, 3, 4),
    Line(2, 2, 2, 1),
    Line(7, 0, 7, 4),
    Line(6, 4, 2, 0),
    Line(0, 9, 2, 9),
    Line(3, 4, 1, 4),
    Line(0, 0, 8, 8),
    Line(5, 5, 8, 2),
]


def test_star1():
    assert star1(iter(TEST_DATA)) == 5


def test_star2():
    assert star2(iter(TEST_DATA)) == 12
