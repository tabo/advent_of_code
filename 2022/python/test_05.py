import unittest
from collections import defaultdict

from aoc_helpers import input_lines_unfiltered, example_lines_unfiltered


Stack = list[str]
Move = tuple[int, str, str]


def header_to_stacks(lns: list[str]) -> dict[str:Stack]:
    data_cols: dict[str:int] = {}
    stacks: dict[str: Stack] = defaultdict(list)
    line_num: int = 0
    for line_num, ln in enumerate(lns):
        if "[" not in ln:
            for pos, char in enumerate(ln.rstrip()):
                if char != " ":
                    data_cols[char] = pos
            break
    for stack_pos in range(line_num):
        ln: str = lns[line_num - stack_pos - 1]
        for stack_num, stack_col in data_cols.items():
            val: str = ln[stack_col]
            if val != " ":
                stacks[stack_num].append(val)
    return stacks


def lns_to_moves(lns: list[str]) -> list[Move]:
    res: list[Move] = []
    actions_started: bool = False
    for ln in lns:
        if ln.strip() == "":
            actions_started = True
        elif actions_started:
            action = ln.strip().split(" ")
            res.append((int(action[1]), action[3], action[5]))
    return res


def find_top_crates(stacks):
    return "".join(stacks[str(num + 1)][-1] for num in range(len(stacks)))


def part1(lns: list[str]) -> str:
    stacks = header_to_stacks(lns)
    for num, src, target in lns_to_moves(lns):
        for _ in range(num):
            stacks[target].append(stacks[src].pop())
    return find_top_crates(stacks)


def part2(lns: list[str]) -> str:
    stacks = header_to_stacks(lns)
    for num, src, target in lns_to_moves(lns):
        pop_pos = len(stacks[src]) - num
        for _ in range(num):
            stacks[target].append(stacks[src].pop(pop_pos))
    return find_top_crates(stacks)


class Day05(unittest.TestCase):
    def test_part1_example(self):
        self.assertEqual("CMZ", part1(example_lines_unfiltered(day=5)))

    def test_part2_example(self):
        self.assertEqual("MCD", part2(example_lines_unfiltered(day=5)))

    def test_part1_solution(self):
        self.assertEqual("CNSZFDVLJ", part1(input_lines_unfiltered(day=5)))

    def test_part2_solution(self):
        self.assertEqual("QNDWLMGNS", part2(input_lines_unfiltered(day=5)))
