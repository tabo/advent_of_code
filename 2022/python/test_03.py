import unittest
from functools import reduce
from itertools import groupby

from aoc_helpers import input_lines


class Day03(unittest.TestCase):
    def char_score(self, char: str) -> int:
        ascii_chr = ord(char)
        if ord("a") <= ascii_chr <= ord("z"):
            return ascii_chr - ord("a") + 1
        if ord("A") <= ascii_chr <= ord("Z"):
            return ascii_chr - ord("A") + 27
        return 0

    def part1(self, lns: list[str]) -> int:
        return sum(
            self.char_score((set(ln[0 : len(ln) // 2]) & set(ln[len(ln) // 2 :])).pop())
            for ln in lns
        )

    def part2(self, lns: list[str]) -> int:
        return sum(
            self.char_score(
                (reduce(lambda a, b: a & b, (set(x[1]) for x in group)).pop())
            )
            for _, group in groupby(enumerate(lns), lambda x: x[0] // 3)
        )

    def test_part1(self):
        self.assertEqual(self.part1(input_lines(day=3)), 7824)

    def test_part2(self):
        self.assertEqual(self.part2(input_lines(day=3)), 2798)
