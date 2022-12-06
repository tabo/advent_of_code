import unittest
from aoc_helpers import input_text


def solver(ln: str, num: int) -> int:
    for pos in range(len(ln) - num - 1):
        if len(set(ln[pos : pos + num])) == num:
            return pos + num
    return -1


def part1(ln: str) -> int:
    return solver(ln, 4)


def part2(ln: str) -> int:
    return solver(ln, 14)


class Day06(unittest.TestCase):
    def test_part1_example1(self):
        self.assertEqual(7, part1("mjqjpqmgbljsphdztnvjfqwrcgsmlb"))

    def test_part1_example2(self):
        self.assertEqual(5, part1("bvwbjplbgvbhsrlpgdmjqwftvncz"))

    def test_part1_example3(self):
        self.assertEqual(6, part1("nppdvjthqldpwncqszvftbrmjlhg"))

    def test_part1_example4(self):
        self.assertEqual(10, part1("nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg"))

    def test_part1_example5(self):
        self.assertEqual(11, part1("zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw"))

    def test_part2_example1(self):
        self.assertEqual(19, part2("mjqjpqmgbljsphdztnvjfqwrcgsmlb"))

    def test_part2_example2(self):
        self.assertEqual(23, part2("bvwbjplbgvbhsrlpgdmjqwftvncz"))

    def test_part2_example3(self):
        self.assertEqual(23, part2("nppdvjthqldpwncqszvftbrmjlhg"))

    def test_part2_example4(self):
        self.assertEqual(29, part2("nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg"))

    def test_part2_example5(self):
        self.assertEqual(26, part2("zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw"))

    def test_part1_solution(self):
        self.assertEqual(1531, part1(input_text(day=6)))

    def test_part2_solution(self):
        self.assertEqual(2518, part2(input_text(day=6)))
