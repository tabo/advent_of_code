import unittest
from aoc_helpers import input_lines, example_lines


def part1(lns: list[str]) -> int:
    return len(lns)


def part2(lns: list[str]) -> int:
    return len(lns)


class Day19(unittest.TestCase):
    def test_part1_example(self):
        self.assertEqual(0, part1(example_lines(day=19)))

    def test_part2_example(self):
        self.assertEqual(0, part2(example_lines(day=19)))

    def test_part1_solution(self):
        self.assertEqual(0, part1(input_lines(day=19)))

    def test_part2_solution(self):
        self.assertEqual(0, part2(input_lines(day=19)))
