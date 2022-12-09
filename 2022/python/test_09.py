import unittest
from collections import namedtuple

from aoc_helpers import input_lines, example_lines


Point = namedtuple("Point", "x y", defaults=[0, 0])


def move_follower(head: Point, tail: Point) -> Point:
    x, y = tail.x, tail.y
    if abs(head.x - tail.x) > 1:
        x += 1 if head.x > tail.x else -1
        if head.y != tail.y:
            y += 1 if head.y > tail.y else -1
    elif abs(head.y - tail.y) > 1:
        y += 1 if head.y > tail.y else -1
        if head.x != tail.x:
            x += 1 if head.x > tail.x else -1
    return Point(x, y)


def move_item(point: Point, direction: str) -> Point:
    if direction == "R":
        return Point(point.x + 1, point.y)
    if direction == "U":
        return Point(point.x, point.y + 1)
    if direction == "L":
        return Point(point.x - 1, point.y)
    if direction == "D":
        return Point(point.x, point.y - 1)


def part1(lns: list[str]) -> int:
    head: Point = Point(0, 0)
    tail: Point = Point(0, 0)
    visited: set[Point] = {head}
    for ln in lns:
        direction, steps = ln.split(" ")
        for _ in range(int(steps)):
            head = move_item(head, direction)
            tail = move_follower(head, tail)
            visited.add(tail)
    return len(visited)


def part2(lns: list[str]) -> int:
    points_names: list[str] = ["H", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    points: dict[str: Point] = {name: Point(0, 0) for name in points_names}
    visited: set[Point] = {points["9"]}
    for ln in lns:
        direction, steps = ln.split(" ")
        for _ in range(int(steps)):
            points["H"] = move_item(points["H"], direction)
            for i in range(len(points_names)-1):
                head = points[points_names[i]]
                tail_id = points_names[i+1]
                tail = points[tail_id]
                points[tail_id] = move_follower(head, tail)
            visited.add(points["9"])
    return len(visited)


class Day09(unittest.TestCase):
    def test_part1_example(self):
        self.assertEqual(13, part1(example_lines(day=9)))

    def test_part2_example1(self):
        self.assertEqual(1, part2(example_lines(day=9)))

    def test_part2_example2(self):
        data = """R 5
U 8
L 8
D 3
R 17
D 10
L 25
U 20""".split(
            "\n"
        )
        self.assertEqual(36, part2(data))

    def test_part1_solution(self):
        self.assertEqual(6642, part1(input_lines(day=9)))

    def test_part2_solution(self):
        self.assertEqual(2765, part2(input_lines(day=9)))
