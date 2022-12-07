from typing import *
from src.utils import *

day_number = get_day_number(__file__)



def solve(lines: Lines) -> int:
    total = 0
    for line in lines:
        a_str, b_str = line.split(' ')
        they = int('ABC'.index(a_str))
        me = int('XYZ'.index(b_str))
        result = (me - they + 1) % 3
        points = me + 1 + (result * 3)
        total += points

    solution = total
    return solution
# def solve(lines: Lines) -> int:
#     p = 0
#     for line in lines:
#         a_str, b_str = line.split(' ')
#         they = int('ABC'.index(a_str))
#         me = int('XYZ'.index(b_str))
#         if (me - they) % 3 == 1:
#             g = 6
#         elif (me - they) == 0:
#             g = 3
#         else:
#             g = 0
#         p += me + 1 + g

#     solution = p
#     return solution


def main() -> None:
    lines = read_data_from_day(day_number)
    res = solve(lines)
    print_solution(res)


if __name__ == "__main__":
    main()
