from src.utils import Lines, print_solution, read_data_from_day

from .a import calculate_max_elvs, day_number




def solve(lines: Lines) -> int:
    solution = calculate_max_elvs(lines, 3)
    return solution


def main() -> None:
    print('Part 2')
    lines = read_data_from_day(day_number)
    res = solve(lines)
    print_solution(res)


if __name__ == "__main__":
    main()
