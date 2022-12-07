from typing import Callable
from src.utils import create_example, Lines
from . import a, b

given_input = '''1000
2000
3000

4000

5000
6000

7000
8000
9000

10000'''



def test_a() -> None:
    expected = 24000
    process(a.solve, expected)



def test_b() -> None:
    expected = 45000
    process(b.solve, expected)


def process(solve: Callable[[Lines], int], expected: int) -> None:
    example = create_example(given_input, expected)
    res = solve(example.lines)
    assert res == example.expected
