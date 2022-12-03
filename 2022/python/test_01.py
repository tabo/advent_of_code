import unittest
from aoc_helpers import input_text, example_text


def groups(txt: str) -> list[int]:
    return [
        sum(int(num) for num in group.split("\n") if num != "")
        for group in txt.split("\n\n")
    ]


def part1(txt: str):
    return max(groups(txt))


def part2(txt: str):
    return sum(sorted(groups(txt))[-3:])


class Day01(unittest.TestCase):
    def test_part1_example(self):
        self.assertEqual(part1(example_text(day=1)), 24000)

    def test_part2_example(self):
        self.assertEqual(part2(example_text(day=1)), 45000)

    def test_part1_solution(self):
        self.assertEqual(part1(input_text(day=1)), 74394)

    def test_part2_solution(self):
        self.assertEqual(part2(input_text(day=1)), 212836)
