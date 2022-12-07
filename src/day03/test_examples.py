from typing import *
from src.utils import *

from . import a

given_input = '''vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw'''


def test_a() -> None:
    expected = 157
    process(a.solve, expected)


def process(solve: Callable[[Lines], int], expected: int) -> None:
    example = create_example(given_input, expected)
    res = solve(example.lines)
    assert res == example.expected
