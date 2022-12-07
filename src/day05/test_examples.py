from typing import *
from src.utils import *

from . import a, b


given_input = read_from_folder(__file__, 'example.txt')


first_input = '''zn
mcd
p'''

second = '''move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2'''


def test_impl_a() -> None:
    result = a.impl(a.get_stacks(first_input), second.split('\n'))
    expected = 'CMZ'
    assert result == expected


def test_impl_b() -> None:
    result = b.impl(a.get_stacks(first_input), second.split('\n'))
    expected = 'MCD'
    assert result == expected


T = TypeVar('T', int, str)


def process(solve: Callable[[Lines], T], expected: T) -> None:
    example = create_example(given_input, expected)
    res = solve(example.lines)
    assert res == example.expected


def test_extract() -> None:
    lines = read_data_from_day(a.day_number)
    first_input, second = a.extract_parts(lines)
    expected = '''GFVHPS
GJFBVDZM
GMLJN
NGZVDWP
VRCB
VRSMPWLZ
THP
QRSNCHZV
FLGPVQJ'''.split('\n')
    assert first_input == expected



def test_a() -> None:
    expected = 'CMZ'
    example = create_example(given_input, expected)
    res = a.solve(example.lines)
    assert res == example.expected



def test_b() -> None:
    expected = 'MCD'
    process(b.solve, expected)
