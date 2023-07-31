from typing import *
from src.utils import *
from .a import Move, day_number, extract_parts, parse_moves, get_stacks, get_upper_boxes



def impl(stacks: list[list[str]], moves: Sequence[Move]) -> str:
    for m in moves:
        n, start, end = m
        box = stacks[start][-n:]
        stacks[start] = stacks[start][:-n]
        stacks[end].extend(box)

    solution = get_upper_boxes(stacks)
    return solution


def solve(lines: Lines) -> str:
    first_input, second = extract_parts(lines)
    stacks = get_stacks('\n'.join(first_input))
    moves = parse_moves(second)
    solution = impl(stacks, moves)
    return solution



def main() -> None:
    print('Part 2')
    lines = read_data_from_day(day_number)
    res = solve(lines)
    print_solution(res)


if __name__ == "__main__":
    main()
