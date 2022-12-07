from typing import *
from src.utils import *

from string import ascii_lowercase, ascii_uppercase

day_number = get_day_number(__file__)


all_arts = ascii_lowercase + ascii_uppercase
assert len(all_arts) == 52


def solve(lines: Lines) -> int:
    total = 0
    for i, line in enumerate(lines):
        n = len(line)
        one, two = set(line[:(n // 2)]), set(line[(n // 2):])
        # print(one, two)
        found = None
        for x in one:
            if x in two:
                # assert not found, (found, x, i)
                found = x
                # break
        assert found
        # print(found)
        priority = all_arts.index(found) + 1
        # print(f"{priority=}")
        # print(f"{total=}")
        total += priority

    solution = total
    return solution




def main() -> None:
    lines = read_data_from_day(day_number)
    res = solve(lines)
    print_solution(res)


if __name__ == "__main__":
    main()
