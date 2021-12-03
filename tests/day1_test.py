from day1 import star1, star2

TEST_DATA = [
    199,
    200,
    208,
    210,
    200,
    207,
    240,
    269,
    260,
    263,
]


def _data():
    for i in TEST_DATA:
        yield i


def test_star1():
    assert star1(iter(TEST_DATA)) == 7


def test_star2():
    assert star2(iter(TEST_DATA)) == 5
