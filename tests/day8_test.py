from day8 import star1, star2

TEST_DATA = [
    (["be", "cfbegad", "cbdgef", "fgaecd", "cgeb", "fdcge", "agebfd", "fecdb", "fabcd", "edb"], ["fdgacbe", "cefdb", "cefbgd", "gcbe"]),  # noqa
    (["edbfga", "begcd", "cbg", "gc", "gcadebf", "fbgde", "acbgfd", "abcde", "gfcbed", "gfec"], ["fcgedb", "cgb", "dgebacf", "gc"]),  # noqa
]


def test_star1():
    assert star1(iter(TEST_DATA)) == 5


def test_star2():
    assert star2(iter(TEST_DATA)) == 18175
