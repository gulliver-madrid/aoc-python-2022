from typing import *
from src.utils import *
from .a import day_number, create_range

# Part 2


def solve(lines: Lines) -> int:
    c = 0
    for i, line in enumerate(lines):
        print(f"{i=}")
        # print(line)
        one, two = line.split(',')
        rx = create_range(one)
        ry = create_range(two)
        if (rx & ry):
            c += 1

    solution = c
    return solution


# print(f"{=}, {=}, {=}, {=}")
# print(f"{=}\n {=}\n {=}\n {=}")


def main() -> None:
    print('Part 2')
    lines = read_data_from_day(day_number)
    res = solve(lines)
    print_solution(res)


if __name__ == "__main__":
    main()
