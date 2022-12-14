import unittest

from aoc_helpers import input_lines, example_lines


def lns2cave(lns: list[str]) -> set[tuple[int, int]]:
    return {
        (x, y)
        for parts in [
            [[*map(int, p.split(","))] for p in ln.split(" -> ")] for ln in lns
        ]
        for (x1, y1), (x2, y2) in zip(parts, parts[1:])
        for x in range(min(x1, x2), max(x1, x2) + 1)
        for y in range(min(y1, y2), max(y1, y2) + 1)
    }


def sand_manager(cave: set, max_y: int) -> bool:
    x, y = 500, 0
    while (x, y) not in cave:
        if y > max_y:
            return False
        for nx, ny in [(x, y + 1), (x - 1, y + 1), (x + 1, y + 1)]:
            if (nx, ny) not in cave:
                x, y = nx, ny
                break
        else:
            cave.add((x, y))
            return True


def part1(lns: list[str]) -> int:
    cave = lns2cave(lns)
    res = 0
    while sand_manager(cave, max(x[1] for x in cave)):
        res += 1
    return res


def part2(lns: list[str]) -> int:
    cave = lns2cave(lns)
    floor = max(pos[1] for pos in cave) + 2
    cave |= {(x, floor) for x in range(500 - (floor + 10), 500 + (floor + 10))}
    res = 0
    while (500, 0) not in cave and sand_manager(cave, floor):
        res += 1
    return res


class Day14(unittest.TestCase):
    def test_part1_example(self):
        self.assertEqual(24, part1(example_lines(day=14)))

    def test_part2_example(self):
        self.assertEqual(93, part2(example_lines(day=14)))

    def test_part1_solution(self):
        self.assertEqual(1061, part1(input_lines(day=14)))

    def test_part2_solution(self):
        self.assertEqual(25055, part2(input_lines(day=14)))
