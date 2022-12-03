import unittest
from aoc_helpers import input_text


class Day01(unittest.TestCase):

    @property
    def groups(self) -> list[int]:

        return [
            sum(int(num) for num in group.split("\n") if num != "")
            for group in input_text(day=1).split("\n\n")
        ]

    def test_part1(self):
        self.assertEqual(max(self.groups), 74394)

    def test_part2(self):
        self.assertEqual(sum(sorted(self.groups)[-3:]), 212836)
