from day14 import star1, star2

TEST_DATA = {
    "CH": "B",
    "HH": "N",
    "CB": "H",
    "NH": "C",
    "HB": "C",
    "HC": "B",
    "HN": "C",
    "NN": "C",
    "BH": "H",
    "NC": "B",
    "NB": "B",
    "BN": "B",
    "BB": "N",
    "BC": "B",
    "CC": "N",
    "CN": "C",
}


TEST_POLYMER = "NNCB"


def test_star1():
    assert star1(TEST_POLYMER, TEST_DATA) == 1588


def test_star2():
    assert star2(TEST_POLYMER, TEST_DATA) == 2188189693529
