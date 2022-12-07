from typing import *
from src.utils import *
from .a import *

given_input = """
"""
expected = 0
example = Example(given_input.split("\n"), expected)


def prueba() -> None:
    res = solve(example.lines)
    print_solution(res)

    if res == example.expected:
        print("ok")
    else:
        print("no ok")


if __name__ == "__main__":
    prueba()
