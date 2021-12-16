from day12 import star1, star2

TEST_DATA = [
    ("start", "A"),
    ("start", "b"),
    ("A", "c"),
    ("A", "b"),
    ("b", "d"),
    ("A", "end"),
    ("b", "end"),
]


def test_star1():
    assert star1(iter(TEST_DATA)) == 10


def test_star2():
    assert star2(iter(TEST_DATA)) == 36
