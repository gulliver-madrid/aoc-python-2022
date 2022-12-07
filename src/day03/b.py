from collections import defaultdict
from typing import *
from src.utils import *

from .a import day_number, all_arts


def solve(lines: Lines) -> int:
    total = 0
    n = len(lines)
    d = defaultdict(list)
    for i, line in enumerate(lines):
        d[i // 3].append(set(line))
    assert len(d) == (n / 3) == (n // 3), (n, len(d))
    for g in d.values():
        x, y, z = g
        for art in x:
            if art in y and art in z:
                pr = all_arts.index(art) + 1
                total += pr
                break


    solution = total
    return solution


def main() -> None:
    print('Part 2')
    lines = read_data_from_day(day_number)
    res = solve(lines)
    print_solution(res)


if __name__ == "__main__":
    main()
