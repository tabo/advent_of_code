import unittest
import math
from collections import defaultdict

from aoc_helpers import input_lines, example_lines


Grid = dict[tuple[int, int] : int]


def is_visible(grid: Grid, width: int, height: int, col: int, row: int) -> bool:
    if row == 0 or col == 0 or row + 1 == height or col + 1 == width:
        # at the border
        return True
    l: list[int] = []
    tree_height: int = grid[(col, row)]
    c_col: int = col
    for c_row in range(height):
        if c_row < row:
            l.append(grid[(c_col, c_row)])
        elif c_row == row:
            if max(l) < tree_height:
                return True
            l = []
        else:
            l.append(grid[(c_col, c_row)])
    if max(l) < tree_height:
        return True

    l: list[int] = []
    tree_height: int = grid[(col, row)]
    c_row: int = row
    for c_col in range(width):
        if c_col < col:
            l.append(grid[(c_col, c_row)])
        elif c_col == col:
            if max(l) < tree_height:
                return True
            l = []
        else:
            l.append(grid[(c_col, c_row)])
    if max(l) < tree_height:
        return True
    return False


def scenic_score(grid: Grid, width: int, height: int, col: int, row: int) -> int:
    found: list[int] = []
    tree_height: int = grid[(col, row)]
    # up
    val: int = 0
    # print("UP")
    for irow in range(row - 1, 0 - 1, -1):
        val += 1
        if grid[(col, irow)] >= tree_height:
            break
    found.append(val)
    # down
    val = 0
    for irow in range(row + 1, height):
        val += 1
        if grid[(col, irow)] >= tree_height:
            break
    found.append(val)
    # left
    val = 0
    for icol in range(col - 1, 0 - 1, -1):
        val += 1
        if grid[(icol, row)] >= tree_height:
            break
    found.append(val)
    # right
    val = 0
    for icol in range(col + 1, width):
        val += 1
        if grid[(icol, row)] >= tree_height:
            break
    found.append(val)
    res = math.prod(found)
    return res


def get_grid(lns):
    grid: Grid = defaultdict(int)
    width: int = 0
    height: int = 0
    for row, ln in enumerate(lns):
        height = row + 1
        for col, num_str in enumerate(ln):
            if col + 1 > width:
                width = col + 1
            grid[(col, row)] = int(num_str)
    return grid, width, height


def part1(lns: list[str]) -> int:
    grid, width, height = get_grid(lns)
    return sum(
        1 for col, row in grid.keys() if is_visible(grid, width, height, col, row)
    )


def part2(lns: list[str]) -> int:
    grid, width, height = get_grid(lns)
    return max(scenic_score(grid, width, height, col, row) for col, row in grid.keys())


class Day08(unittest.TestCase):
    def test_part1_example(self):
        self.assertEqual(21, part1(example_lines(day=8)))

    def test_part2_example(self):
        self.assertEqual(8, part2(example_lines(day=8)))

    def test_part1_solution(self):
        self.assertEqual(1787, part1(input_lines(day=8)))

    def test_part2_solution(self):
        self.assertEqual(440640, part2(input_lines(day=8)))
