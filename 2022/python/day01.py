groups = [
    sum(int(num) for num in group.split("\n") if num != "")
    for group in open("day01.txt").read().split("\n\n")
]
print(f"Part 1: {max(groups)}")
print(f"Part 2: {sum(sorted(groups)[-3:])}")
