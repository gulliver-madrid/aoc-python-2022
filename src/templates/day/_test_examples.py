import pytest
from typing import *
from src.utils import *

from . import a, b

given_input = ''''''


@pytest.mark.skip(reason="Not implemented")
def test_a() -> None:
    expected = 0
    process(a.solve, expected)


@pytest.mark.skip(reason="Not implemented")
def test_b() -> None:
    expected = 0
    process(b.solve, expected)


@pytest.mark.skip(reason="Not implemented")
def test_func_int() -> None:
    result = a.func_int()
    expected = 0
    assert result == expected


@pytest.mark.skip(reason="Not implemented")
def test_func_str() -> None:
    result = a.func_str()
    expected = ''
    assert result == expected


T = TypeVar('T', int, str)


def process(solve: Callable[[Lines], T], expected: T) -> None:
    example = create_example(given_input, expected)
    res = solve(example.lines)
    assert res == example.expected


# def test_examples() -> None:
#     res = a.solve(example.lines)
#     assert res == example.expected


# def test_a() -> None:
#     expected = 0
#     example = create_example(given_input, expected)
#     res = a.solve(example.lines)
#     assert res == example.expected


# def test_b() -> None:
#     expected = 0
#     example = create_example(given_input, expected)
#     res = b.solve(example.lines)
#     assert res == example.expected
