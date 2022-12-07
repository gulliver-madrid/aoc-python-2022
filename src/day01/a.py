from src.utils import Lines, get_day_number, print_solution, read_data_from_day


day_number = get_day_number(__file__)


def calculate_max_elvs(lines: Lines, n: int) -> int:
    elvs = [0]
    for line in lines:
        if line:
            elvs[-1] += int(line)
        else:
            elvs.append(0)

    total = 0
    for i in range(n):
        elv = max(elvs)
        total += elv
        elvs.remove(elv)
    return total


def solve(lines: Lines) -> int:
    solution = calculate_max_elvs(lines, 1)
    return solution


def main() -> None:
    lines = read_data_from_day(day_number)
    res = solve(lines)
    print_solution(res)


if __name__ == "__main__":
    main()
