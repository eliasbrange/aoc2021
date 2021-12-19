import pytest
from day16 import star1, star2

TEST_DATA = [
]


@pytest.mark.parametrize("data,exp", [
    ("8A004A801A8002F478", 16),
    ("620080001611562C8802118E34", 12),
    ("C0015000016115A2E0802F182340", 23),
    ("A0016C880162017C3686B18A3D4780", 31),
])
def test_star1(data, exp):
    assert star1(data) == exp


@pytest.mark.parametrize("data,exp", [
    ("C200B40A82", 3),
    ("04005AC33890", 54),
    ("880086C3E88112", 7),
    ("CE00C43D881120", 9),
    ("D8005AC2A8F0", 1),
    ("F600BC2D8F", 0),
    ("9C005AC2F8F0", 0),
    ("9C0141080250320F1802104A08", 1),
])
def test_star2(data, exp):
    assert star2(data) == exp
