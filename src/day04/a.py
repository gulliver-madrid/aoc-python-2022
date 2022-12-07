
from typing import *
from src.utils import *

day_number = get_day_number(__file__)


def solve(lines: Lines) -> int:
    c = 0
    for i, line in enumerate(lines):
        print(f"{i=}")
        # print(line)
        one, two = line.split(',')
        rx = create_range(one)
        ry = create_range(two)
        if (rx & ry) in [rx, ry]:
            c += 1

    solution = c
    return solution


def create_range(range_str: str) -> set[int]:
    inclusive_range = [int(s) for s in range_str.split('-')]
    return set(range(inclusive_range[0], inclusive_range[1] + 1))




def main() -> None:
    lines = read_data_from_day(day_number)
    res = solve(lines)
    print_solution(res)


if __name__ == "__main__":
    main()
