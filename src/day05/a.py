import string
from typing import *
from src.utils import *

day_number = get_day_number(__file__)

Stacks = list[list[str]]


def transpond(first_lines: Sequence[str]) -> list[list[str]]:
    n = len(first_lines[0])
    transp = []
    for i in range(n):
        new_line = [sa[i]for sa in first_lines]
        # Remove stack number at the end
        new_line = new_line[:-1]
        transp.append(new_line)
    return transp


def get_lines_with_letters(transp: list[list[str]]) -> list[list[str]]:
    als = []
    for li in transp:
        print(f"{li=}")
        if li[-1] in string.ascii_uppercase:
            als.append(li)
    return als


def extract(first_lines: list[str]) -> list[str]:
    n = len(first_lines[0])
    transp = transpond(first_lines)
    als = get_lines_with_letters(transp)
    ts = [''.join(reversed(t)).rstrip() for t in als]
    print(f"{ts=}")
    return ts


def get_stacks(input_str: str) -> list[list[str]]:
    return[list(s.upper()) for s in input_str.split('\n')]


def get_moves(moves_str: list[str]) -> list[tuple[int, int, int]]:
    moves: list[tuple[int, int, int]] = []
    for s in moves_str:
        start_str, end_str = s.split('from')
        n = int(start_str[4:])
        start, end = [int(s1) - 1 for s1 in end_str.split('to')]
        moves.append((n, start, end))
    return moves


def get_upper_boxes(stacks: Stacks) -> str:
    return ''.join([stack[-1] for stack in stacks])


def impl(stacks: list[list[str]], second: Lines) -> str:

    moves = get_moves(second)
    for m in moves:
        print(m)
        n, start, end = m
        for i in range(n):
            box = stacks[start].pop()
            print(f"{stacks=}")
            print(f"{end=}")
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

    solution = impl(get_stacks('\n'.join(first_input)), second)
    return solution




def main() -> None:
    lines = read_data_from_day(day_number)
    res = solve(lines)
    print_solution(res)


if __name__ == "__main__":
    main()
