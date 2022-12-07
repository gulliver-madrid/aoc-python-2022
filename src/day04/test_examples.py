from typing import *
from src.utils import *

from . import a, b


given_input = '''2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8'''


def test_a() -> None:
    expected = 2
    process(a.solve, expected)


def test_b() -> None:
    expected = 4
    process(b.solve, expected)



def process(solve: Callable[[Lines], int], expected: int) -> None:
    example = create_example(given_input, expected)
    res = solve(example.lines)
    assert res == example.expected
