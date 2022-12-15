import re
import unittest

import z3

from aoc_helpers import input_lines, example_lines, input_text, example_text


def ln2nums(ln):
    return list(map(int, re.findall(r"-?\d+", ln)))


def manhattan(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)


def z3_manhattan(x1, y1, x2, y2):
    def z3_abs(num):
        return z3.If(num >= 0, num, -num)

    return z3_abs(x1 - x2) + z3_abs(y1 - y2)


def part1(lns, y):
    min_x = []
    max_x = []
    for ln in lns:
        sx, sy, bx, by = ln2nums(ln)
        o = manhattan(sx, sy, bx, by) - abs(sy - y)
        if o > 0:
            min_x.append(sx - o)
            max_x.append(sx + o)
    return max(max_x) - min(min_x)


def part2(lns: list[str], max_size) -> int:
    s = z3.Solver()
    x = z3.Int("x")
    y = z3.Int("y")
    s.add(x >= 0, x <= max_size, y >= 0, y <= max_size)
    for ln in lns:
        sx, sy, bx, by = ln2nums(ln)
        s.add(z3_manhattan(sx, sy, x, y) > manhattan(sx, sy, bx, by))
    s.check()
    model = s.model()
    return model[x].as_long() * 4000000 + model[y].as_long()


class Day15(unittest.TestCase):
    def test_part1_example(self):
        self.assertEqual(26, part1(example_lines(day=15), y=10))

    def test_part2_example(self):
        self.assertEqual(56000011, part2(example_lines(day=15), max_size=20))

    def test_part1_solution(self):
        self.assertEqual(5508234, part1(input_lines(day=15), y=2000000))

    def test_part2_solution(self):
        self.assertEqual(10457634860779, part2(input_lines(day=15), max_size=4000000))
