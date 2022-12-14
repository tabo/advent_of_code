import unittest
from aoc_helpers import input_text, example_text


def groups(txt: str) -> list[int]:
    return [
        sum(int(num) for num in group.split("\n") if num != "")
        for group in txt.split("\n\n")
    ]


def part1(txt: str) -> int:
    return max(groups(txt))


def part2(txt: str) -> int:
    return sum(sorted(groups(txt))[-3:])


class Day01(unittest.TestCase):
    def test_part1_example(self):
        self.assertEqual(24000, part1(example_text(day=1)))

    def test_part2_example(self):
        self.assertEqual(45000, part2(example_text(day=1)))

    def test_part1_solution(self):
        self.assertEqual(74394, part1(input_text(day=1)))

    def test_part2_solution(self):
        self.assertEqual(212836, part2(input_text(day=1)))
