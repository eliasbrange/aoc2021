from typing import Iterator
from common import read_file
from math import prod


TABLE = {
    "0": "0000",
    "1": "0001",
    "2": "0010",
    "3": "0011",
    "4": "0100",
    "5": "0101",
    "6": "0110",
    "7": "0111",
    "8": "1000",
    "9": "1001",
    "A": "1010",
    "B": "1011",
    "C": "1100",
    "D": "1101",
    "E": "1110",
    "F": "1111",
}


def binary(data: str) -> Iterator[str]:
    for ch in data:
        for bit in TABLE[ch]:
            yield bit


class Packet:
    def __init__(self, bits: Iterator[str]):
        self.version_sum = 0
        self.result = self.read_packet(bits)

    def read_packet(self, bits: Iterator[str]):
        version = self.read_int(bits, 3)
        type_id = self.read_int(bits, 3)
        self.version_sum += version

        if type_id == 4:
            literal = self.read_literal(bits)
            return literal

        length_type_bit = next(bits)

        if length_type_bit == "1":
            count = self.read_int(bits, 11)
            subpackets = self.read_subpackets_by_count(bits, count)
        else:
            n_bits = self.read_int(bits, 15)
            subpackets = self.read_subpackets_by_bits(bits, n_bits)

        if type_id == 0:
            return sum(subpackets)
        elif type_id == 1:
            return prod(subpackets)
        elif type_id == 2:
            return min(subpackets)
        elif type_id == 3:
            return max(subpackets)
        elif type_id == 5:
            return int(subpackets[0] > subpackets[1])
        elif type_id == 6:
            return int(subpackets[0] < subpackets[1])
        elif type_id == 7:
            return int(subpackets[0] == subpackets[1])

    def read_subpackets_by_bits(self, bits: Iterator[str], n_bits: int):
        bits = iter([next(bits) for _ in range(n_bits)])

        packets = []
        try:
            while True:
                packets.append(self.read_packet(bits))
        except StopIteration:
            pass

        return packets

    def read_subpackets_by_count(self, bits: Iterator[str], n: int):
        packets = []
        for i in range(n):
            packets.append(self.read_packet(bits))

        return packets

    def read_literal(self, bits: Iterator[str]) -> int:
        literal_bits = []
        while True:
            should_continue = next(bits) == "1"
            literal_bits += [next(bits) for _ in range(4)]

            if not should_continue:
                break

        return int("".join(literal_bits), 2)

    def read_int(self, bits: Iterator[str], n: int) -> int:
        return int("".join([next(bits) for i in range(n)]), 2)


def star1(data: str) -> int:
    packets = Packet(binary(data))

    return packets.version_sum


def star2(data: str) -> int:
    packets = Packet(binary(data))

    return packets.result


if __name__ == "__main__":
    data = next(read_file("../inputs/day16.txt"))

    res1 = star1(data)
    print(f"Star 1: {res1}")

    res2 = star2(data)
    print(f"Star 2: {res2}")
