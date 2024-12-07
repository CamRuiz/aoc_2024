import re

from src.utilities.timer import run_timed


def solution() -> None:
    with open('src/day_3/input_3_1.txt', 'r') as file:
        input_text = file.read()

    instructions = (re.findall(r"mul\(\d+,\d+\)|do\(\)|don\'t\(\)", input_text))

    result = 0
    enabled = True
    for instruction in instructions:
        if instruction[:3] == 'do(':
            enabled = True
        elif instruction[:3] == 'don':
            enabled = False
        else:
            if enabled:
                x, y = map(int, re.findall(r'\d+', instruction))
                result += x * y
    print(result)


def main() -> None:
    run_timed(solution)


if __name__ == "__main__":
    main()