import unittest
from aoc_helpers import input_lines, example_lines

import numpy
import networkx


def create_graph(lns):
    grid = numpy.array([[*ln] for ln in lns])
    start = tuple(*(numpy.argwhere(grid == "S")))
    end = tuple(*(numpy.argwhere(grid == "E")))
    # the square marked S that counts as being at elevation a
    grid[start] = "a"
    grid[end] = "z"
    grid_graph = networkx.grid_2d_graph(*grid.shape)
    di_graph = networkx.DiGraph()
    for pos in numpy.ndindex(*grid.shape):
        for neighbor in grid_graph.neighbors(pos):
            if ord(grid[neighbor]) - ord(grid[pos]) < 2:
                di_graph.add_edge(pos, neighbor)
    return start, grid, networkx.shortest_path_length(di_graph, target=end)


def part1(lns: list[str]) -> int:
    start, _, paths = create_graph(lns)
    return paths[start]


def part2(lns: list[str]) -> int:
    _, grid, paths = create_graph(lns)
    return min(paths[a] for a in paths if grid[a] == "a")


class Day12(unittest.TestCase):
    def test_part1_example(self):
        self.assertEqual(31, part1(example_lines(day=12)))

    def test_part2_example(self):
        self.assertEqual(29, part2(example_lines(day=12)))

    def test_part1_solution(self):
        self.assertEqual(420, part1(input_lines(day=12)))

    def test_part2_solution(self):
        self.assertEqual(414, part2(input_lines(day=12)))
