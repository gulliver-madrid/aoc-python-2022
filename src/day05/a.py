import string
from typing import *
from src.utils import *

day_number = get_day_number(__file__)

Stacks = list[list[str]]
Move = tuple[int, int, int]


def transpond(first_lines: Sequence[str]) -> list[list[str]]:
    n = len(first_lines[0])
    transp = []
    for i in range(n):
        new_line = [line[i] for line in first_lines]
        # Remove stack number at the end
        new_line.pop()
        transp.append(new_line)
    return transp


def get_lines_with_letters(transp: list[list[str]]) -> list[list[str]]:
    output = []
    for row in transp:
        if row[-1] in string.ascii_uppercase:
            output.append(row)
    return output


def extract(first_lines: list[str]) -> list[str]:
    n = len(first_lines[0])
    transp = transpond(first_lines)
    als = get_lines_with_letters(transp)
    ts = [''.join(reversed(t)).rstrip() for t in als]
    return ts


def get_stacks(input_str: str) -> list[list[str]]:
    return[list(s.upper()) for s in input_str.split('\n')]


def parse_moves(moves_str: list[str]) -> list[Move]:
    moves: list[tuple[int, int, int]] = []
    for s in moves_str:
        start_str, end_str = s.split('from')
        n = int(start_str[4:])
        start, end = [int(s1) - 1 for s1 in end_str.split('to')]
        moves.append((n, start, end))
    return moves


def get_upper_boxes(stacks: Stacks) -> str:
    return ''.join(stack[-1] for stack in stacks)


def impl(stacks: list[list[str]], moves: Sequence[Move]) -> str:
    for m in moves:
        n, start, end = m
        for _ in range(n):
            box = stacks[start].pop()
            stacks[end].append(box)
    solution = get_upper_boxes(stacks)
    return solution


def extract_parts(lines: Lines) -> tuple[list[str], list[str]]:
    first = []
    for i, line in enumerate(lines):
        if not line:
            first = lines[: i]
            break
    second = lines[i + 1:]
    return extract(first), second


def solve(lines: Lines) -> str:
    first_input, second = extract_parts(lines)
    stacks = get_stacks('\n'.join(first_input))
    moves = parse_moves(second)
    solution = impl(stacks, moves)
    return solution




def main() -> None:
    lines = read_data_from_day(day_number)
    res = solve(lines)
    print_solution(res)


if __name__ == "__main__":
    main()
