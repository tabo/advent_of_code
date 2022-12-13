from functools import cmp_to_key
import json
import math
import unittest
from aoc_helpers import input_text, example_text


def cmp(lft, rgt) -> int:
    if isinstance(lft, int) and isinstance(rgt, int):
        return 0 if lft == rgt else (1 if lft < rgt else -1)
    if isinstance(lft, list) and isinstance(rgt, list):
        for pair in zip(lft, rgt):
            k = cmp(*pair)
            if k != 0:
                return k
        return cmp(len(lft), len(rgt))
    if isinstance(lft, list) and isinstance(rgt, int):
        return cmp(lft, [rgt])
    if isinstance(lft, int) and isinstance(rgt, list):
        return cmp([lft], rgt)
    raise NotImplementedError


def get_jsoned_pairs(buf: str):
    return (
        tuple(json.loads(item) for item in pair.split("\n"))
        for pair in buf.strip("\n").split("\n\n")
    )


def part1(buf: str) -> int:
    return sum(
        pos
        for pos, (lft, rgt) in enumerate(get_jsoned_pairs(buf), 1)
        if cmp(lft, rgt) > 0
    )


def part2(buf: str) -> int:
    return math.prod(
        pos
        for pos, packet in enumerate(
            reversed(
                sorted(
                    [[[2]], [[6]]]
                    + [
                        item
                        for lft, rgt in get_jsoned_pairs(buf)
                        for item in (lft, rgt)
                    ],
                    key=cmp_to_key(cmp),
                )
            ),
            1,
        )
        if packet in ([[2]], [[6]])
    )


class Day13(unittest.TestCase):
    def test_part1_example(self):
        self.assertEqual(13, part1(example_text(day=13)))

    def test_part2_example(self):
        self.assertEqual(140, part2(example_text(day=13)))

    def test_part1_solution(self):
        self.assertEqual(5340, part1(input_text(day=13)))

    def test_part2_solution(self):
        self.assertEqual(21276, part2(input_text(day=13)))
