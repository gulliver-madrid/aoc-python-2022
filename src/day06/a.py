
import functools
import itertools
from pprint import pprint
from dataclasses import dataclass, field
from enum import Enum
from collections import defaultdict, deque
from pathlib import Path
from typing import *
from src.utils import *
from string import ascii_lowercase, ascii_uppercase


day_number = get_day_number(__file__)


def solve(lines: Lines) -> int:

    line = lines[0]
    for i in range(len(line)):
        if len(set(line[i:i + 4])) == 4:
            break
    solution = i + 4
    return solution




def main() -> None:
    lines = read_data_from_day(day_number)
    res = solve(lines)
    print_solution(res)


if __name__ == "__main__":
    main()
