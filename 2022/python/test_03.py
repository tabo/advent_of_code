import unittest
from functools import reduce
from itertools import groupby
from aoc_helpers import input_lines, example_lines


def char_score(char: str) -> int:
    if "a" <= char <= "z":
        return ord(char) - ord("a") + 1
    if "A" <= char <= "Z":
        return ord(char) - ord("A") + 27
    return 0


def part1(lns: list[str]) -> int:
    return sum(
        char_score((set(ln[0 : len(ln) // 2]) & set(ln[len(ln) // 2 :])).pop())
        for ln in lns
    )


def part2(lns: list[str]) -> int:
    return sum(
        char_score((reduce(lambda a, b: a & b, (set(x[1]) for x in group)).pop()))
        for _, group in groupby(enumerate(lns), lambda x: x[0] // 3)
    )


class Day03(unittest.TestCase):
    def test_part1_example(self):
        self.assertEqual(157, part1(example_lines(day=3)))

    def test_part2_example(self):
        self.assertEqual(70, part2(example_lines(day=3)))

    def test_part1_solution(self):
        self.assertEqual(7824, part1(input_lines(day=3)))

    def test_part2_solution(self):
        self.assertEqual(2798, part2(input_lines(day=3)))
