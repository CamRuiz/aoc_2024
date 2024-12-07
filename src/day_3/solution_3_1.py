import re

from src.utilities.timer import run_timed


def solution() -> None:
    with open('src/day_3/input_3_1.txt', 'r') as file:
        input_text = file.read()

    result = 0
    mults_to_perform = (re.findall(r'mul\(\d+,\d+\)', input_text))

    for mult in mults_to_perform:
        x, y = map(int, re.findall(r'\d+', mult))
        result += x * y
    print(result)


def main() -> None:
    run_timed(solution)


if __name__ == "__main__":
    main()