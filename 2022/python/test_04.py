import unittest
from aoc_helpers import input_lines, example_lines


IntsSet = set[int]
PairOfIntsSets = tuple[IntsSet, IntsSet]


def rangeset(s: str) -> IntsSet:
    n1, n2 = s.split("-")
    return set(range(int(n1), int(n2) + 1))


def pair_of_number_sets(ln: str) -> PairOfIntsSets:
    p1, p2 = ln.split(",")
    return rangeset(p1), rangeset(p2)


def lines_to_pairs(lns: list[str]) -> list[PairOfIntsSets]:
    return [pair_of_number_sets(ln) for ln in lns]


def part1(lns: list[str]) -> int:
    return len([1 for v1, v2 in lines_to_pairs(lns) if v1 >= v2 or v2 >= v1])


def part2(lns: list[str]) -> int:
    return len([1 for v1, v2 in lines_to_pairs(lns) if v1 & v2])


class Day04(unittest.TestCase):
    def test_part1_example(self):
        self.assertEqual(2, part1(example_lines(day=4)))

    def test_part2_example(self):
        self.assertEqual(4, part2(example_lines(day=4)))

    def test_part1_solution(self):
        self.assertEqual(550, part1(input_lines(day=4)))

    def test_part2_solution(self):
        self.assertEqual(931, part2(input_lines(day=4)))
