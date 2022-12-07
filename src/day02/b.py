from typing import *
from src.utils import *

from .a import day_number


# Part 2


def solve(lines: Lines) -> int:
    total = 0
    for line in lines:
        a_str, b_str = line.split(' ')
        they = int('ABC'.index(a_str))
        result = int('XYZ'.index(b_str))
        me = (they + 2 + result) % 3
        points = me + 1 + (result * 3)
        total += points


    solution = total
    return solution


def main() -> None:
    print('Part 2')
    lines = read_data_from_day(day_number)
    res = solve(lines)
    print_solution(res)


if __name__ == "__main__":
    main()
