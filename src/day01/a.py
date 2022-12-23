from src.utils import Lines, get_day_number, print_solution, read_data_from_day


day_number = get_day_number(__file__)


def build_calories_per_elf(lines: Lines) -> list[int]:
    '''Returns a list with the Calories that each elf takes'''
    calories_per_elf = [0]
    for line in lines:
        if line:
            calories_per_elf[-1] += int(line)
        else:
            calories_per_elf.append(0)
    return calories_per_elf


def solve(lines: Lines) -> int:
    calories_per_elf = build_calories_per_elf(lines)
    solution = max(calories_per_elf)
    return solution


def main() -> None:
    lines = read_data_from_day(day_number)
    res = solve(lines)
    print_solution(res)


if __name__ == "__main__":
    main()
