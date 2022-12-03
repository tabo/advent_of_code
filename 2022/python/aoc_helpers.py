from pathlib import Path


def get_file_text(prefix: str, day: int) -> str:
    return Path(f"../input/{prefix}{day:02}.txt").read_text()


def example_text(day: int) -> str:
    return get_file_text("example", day)


def input_text(day: int) -> str:
    return get_file_text("input", day)


def example_lines(day: int) -> list[str]:
    return [ln for ln in example_text(day).split("\n") if ln]


def input_lines(day: int) -> list[str]:
    return [ln for ln in input_text(day).split("\n") if ln]
