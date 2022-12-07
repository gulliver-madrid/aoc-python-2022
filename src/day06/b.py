import functools
import itertools
from pprint import pprint
from dataclasses import dataclass, field
from enum import Enum
from collections import defaultdict, deque
from pathlib import Path
from typing import *
from src.utils import *
from .a import day_number
from string import ascii_lowercase, ascii_uppercase

# Part 2


def solve(lines: Lines) -> int:

    line = lines[0]
    for i in range(len(line)):
        if len(set(line[i:i + 14])) == 14:
            break
    solution = i + 14
    return solution


def main() -> None:
    print('Part 2')
    lines = read_data_from_day(day_number)
    res = solve(lines)
    print_solution(res)


if __name__ == "__main__":
    main()
