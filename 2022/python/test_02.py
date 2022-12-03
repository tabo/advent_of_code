import unittest
from aoc_helpers import input_lines, example_lines


def part1(lns):
    scores: dict[str, int] = {
        # 1st col opponent play: A=rocks B=paper C=scissors
        # 2nd col out play:      X=rocks Y=paper Z=scissors
        # score = our choice score + result score
        #   choice score = X=1 Y=2 Z=3
        #   result score = victory=6 draw=3 defeat=0
        "A X": 1 + 3,
        "A Y": 2 + 6,
        "A Z": 3 + 0,
        "B X": 1 + 0,
        "B Y": 2 + 3,
        "B Z": 3 + 6,
        "C X": 1 + 6,
        "C Y": 2 + 0,
        "C Z": 3 + 3,
    }
    return sum(scores[ln] for ln in lns)


def part2(lns):
    scores: dict[str, int] = {
        # 1st col opponent play:   A=rocks B=paper C=scissors
        # 2nd col expected result: X=defeat Y=draw Z=victory
        # score = our choice score + result score
        #   choice necessary for result = rocks=1 paper=2 scissors=3
        #   result score = victory=6 draw=3 defeat=0
        "A X": 3 + 0,
        "A Y": 1 + 3,
        "A Z": 2 + 6,
        "B X": 1 + 0,
        "B Y": 2 + 3,
        "B Z": 3 + 6,
        "C X": 2 + 0,
        "C Y": 3 + 3,
        "C Z": 1 + 6,
    }
    return sum(scores[ln] for ln in lns)


class Day02(unittest.TestCase):
    def test_part1_example(self):
        self.assertEqual(part1(example_lines(day=2)), 15)

    def test_part2_example(self):
        self.assertEqual(part2(example_lines(day=2)), 12)

    def test_part1_solution(self):
        self.assertEqual(part1(input_lines(day=2)), 13221)

    def test_part2_solution(self):
        self.assertEqual(part2(input_lines(day=2)), 13131)
