import unittest
from collections import defaultdict

from aoc_helpers import input_lines, example_lines


FsType = dict[str, int]


def pwd_list_to_pwd(lst: list[str]) -> str:
    if len(lst) == 1:
        return "/"
    return "/".join(lst)


def build_fs(lns: list[str]) -> FsType:
    fs: FsType = defaultdict(int)
    pwd: list[str] = [""]
    for ln in lns:
        if ln == "$ ls":
            pass
        elif ln == "$ cd ..":
            pwd.pop()
        elif ln == "$ cd /":
            pwd = [""]
        elif ln.startswith("$ cd "):
            pwd.append(ln.split(" ")[2])
        elif ln.startswith("dir "):
            pass
        else:
            size_str, fname = ln.split(" ", 1)
            size: int = int(size_str)
            for pos in range(len(pwd)):
                fs[pwd_list_to_pwd(pwd[0 : pos + 1])] += size
    return fs


def part1(lns: list[str]) -> int:
    return sum(
        size for fpath, size in build_fs(lns).items() if size <= 100000 and fpath != "/"
    )


def part2(lns: list[str]) -> int:
    fs: FsType = build_fs(lns)
    used_space: int = fs["/"]
    return min(size for size in fs.values() if 40000000 + size >= used_space)


class Day07(unittest.TestCase):
    def test_part1_example(self):
        self.assertEqual(95437, part1(example_lines(day=7)))

    def test_part2_example(self):
        self.assertEqual(24933642, part2(example_lines(day=7)))

    def test_part1_solution(self):
        self.assertEqual(1517599, part1(input_lines(day=7)))

    def test_part2_solution(self):
        self.assertEqual(2481982, part2(input_lines(day=7)))
