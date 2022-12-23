from src.utils import Lines, print_solution, read_data_from_day

from .a import build_calories_per_elf, day_number



def get_total_n_elvs_with_most_calories(calories_per_elf: list[int], n: int) -> int:
    '''Returns the sum of the calories of the n elvs carrying the most Calories'''
    total = 0
    for i in range(n):
        elf = max(calories_per_elf)
        total += elf
        calories_per_elf.remove(elf)
    return total


def solve(lines: Lines) -> int:
    calories_per_elf = build_calories_per_elf(lines)
    solution = get_total_n_elvs_with_most_calories(calories_per_elf, 3)
    return solution


def main() -> None:
    print('Part 2')
    lines = read_data_from_day(day_number)
    res = solve(lines)
    print_solution(res)


if __name__ == "__main__":
    main()
