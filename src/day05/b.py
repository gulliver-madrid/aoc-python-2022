from typing import *
from src.utils import *
from .a import day_number, extract_parts, get_moves, get_stacks, get_upper_boxes



def impl(stacks: list[list[str]], second: Lines) -> str:
    moves = get_moves(second)

    for m in moves:
        print(m)
        n, start, end = m
        box = stacks[start][-n:]
        stacks[start] = stacks[start][:-n]
        stacks[end].extend(box)

    solution = get_upper_boxes(stacks)
    return solution


def solve(lines: Lines) -> str:
    first_input, second = extract_parts(lines)
    solution = impl(get_stacks('\n'.join(first_input)), second)
    return solution



def main() -> None:
    print('Part 2')
    lines = read_data_from_day(day_number)
    res = solve(lines)
    print_solution(res)


if __name__ == "__main__":
    main()
