import math
import unittest
from aoc_helpers import input_lines, example_lines


class Monkey:
    def __init__(self):
        self.inventory = []
        self.func = None
        self.divisible_by = None
        self.throw_if_true = None
        self.throw_if_false = None
        self.inspections = 0


def monkey_op(oper: str, num: str) -> callable:
    def f(old):
        return {"*": math.prod, "+": sum}[oper](
            [old, (old if num == "old" else int(num))]
        )
    return f


def get_monkeys(lns: list[str]) -> list[Monkey]:
    monkeys = []
    for ln in lns:
        if ln.startswith("Monkey "):
            monkey = Monkey()
            monkeys.append(monkey)
        elif "Starting items:" in ln:
            monkey.inventory = [
                int(x) for x in ln.split(":")[1].replace(" ", "").split(",")
            ]
        elif "Operation: new = old " in ln:
            oper, num = ln.split(":")[1].lstrip(" ").split(" ")[3:]
            monkey.func = monkey_op(oper, num)
        else:
            num = int(ln.split(" ")[-1])
            if "Test: divisible by " in ln:
                monkey.divisible_by = num
            elif "If true: " in ln:
                monkey.throw_if_true = num
            elif "If false: " in ln:
                monkey.throw_if_false = num
            else:
                raise f"Unknown line: {ln}"
    return monkeys


def solver(lns: list[str], max_rounds: int, worry_divisor: int) -> int:
    monkeys = get_monkeys(lns)
    for round_num in range(max_rounds):
        for monkey_id, monkey in enumerate(monkeys):
            while monkey.inventory:
                monkey.inspections += 1
                val = (
                    monkey.func(monkey.inventory.pop(0))
                    % math.lcm(*[x.divisible_by for x in monkeys])
                ) // worry_divisor
                monkeys[
                    (
                        monkey.throw_if_true
                        if not val % monkey.divisible_by
                        else monkey.throw_if_false
                    )
                ].inventory.append(val)
    return math.prod(sorted(list([monkey.inspections for monkey in monkeys]))[-2:])


def part1(lns: list[str]) -> int:
    return solver(lns, 20, 3)


def part2(lns: list[str]) -> int:
    return solver(lns, 10000, 1)


class Day11(unittest.TestCase):
    def test_part1_example(self):
        self.assertEqual(10605, part1(example_lines(day=11)))

    def test_part2_example(self):
        self.assertEqual(2713310158, part2(example_lines(day=11)))

    def test_part1_solution(self):
        self.assertEqual(107822, part1(input_lines(day=11)))

    def test_part2_solution(self):
        self.assertEqual(27267163742, part2(input_lines(day=11)))
