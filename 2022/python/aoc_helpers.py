from pathlib import Path


def input_text(day: int) -> str:
    return Path(f"../input/day{day:02}.txt").read_text()


def input_lines(day: int) -> list[str]:
    return [ln for ln in input_text(day).split("\n") if ln]
