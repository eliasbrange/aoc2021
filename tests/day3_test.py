from day3 import star1, star2

TEST_DATA = [
    "00100",
    "11110",
    "10110",
    "10111",
    "10101",
    "01111",
    "00111",
    "11100",
    "10000",
    "11001",
    "00010",
    "01010",
]


def test_star1():
    assert star1(iter(TEST_DATA)) == 198


def test_star2():
    assert star2(iter(TEST_DATA)) == 230
