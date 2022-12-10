import unittest
from aoc_helpers import input_lines, example_lines


def lns2vals(lns: list[str]) -> list[int]:
    vals: list[int] = [1]
    for ln in lns:
        vals.append(vals[-1])
        if ln != "noop":
            vals.append(vals[-1] + int(ln.split(" ")[1]))
    return vals


def part1(lns: list[str]) -> int:
    vals: list[int] = lns2vals(lns)
    return sum(vals[num] * (num + 1) for num in range(19, len(vals), 40))


def part2(lns: list[str]) -> str:
    return "".join(
        (("#" if abs(val - (pos % 40)) < 2 else ".") + ("" if (pos + 1) % 40 else "\n"))
        for pos, val in enumerate(lns2vals(lns))
    )


class Day10(unittest.TestCase):
    def test_part1_example(self):
        self.assertEqual(13140, part1(example_lines(day=10)))

    def test_part2_example(self):
        expected = """
##..##..##..##..##..##..##..##..##..##..
###...###...###...###...###...###...###.
####....####....####....####....####....
#####.....#####.....#####.....#####.....
######......######......######......####
#######.......#######.......#######.....
.""".lstrip("\n")
        self.assertEqual(expected, part2(example_lines(day=10)))

    def test_part1_solution(self):
        self.assertEqual(14860, part1(input_lines(day=10)))

    def test_part2_solution(self):
        expected = """
###...##..####.####.#..#.#..#.###..#..#.
#..#.#..#....#.#....#..#.#..#.#..#.#.#..
#..#.#......#..###..####.#..#.#..#.##...
###..#.##..#...#....#..#.#..#.###..#.#..
#.#..#..#.#....#....#..#.#..#.#.#..#.#..
#..#..###.####.####.#..#..##..#..#.#..#.
.""".lstrip("\n")
        # this is supposed to be `RGZEHURK` 💀
        # it was impossible to read with the font I use
        self.assertEqual(expected, part2(input_lines(day=10)))
