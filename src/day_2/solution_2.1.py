import numpy as np

from src.utilities.timer import run_timed


def solution() -> None:
    with open("src/day_2/input_2.1.txt", "r") as file:
        lines = file.read().splitlines()

    safe_report_count = 0
    for line in lines:
        levels = np.array([int(x) for x in line.split(" ")])

        level_differences = levels[1:] - levels[:-1]

        if np.any(level_differences == 0):
            continue

        if np.any(np.abs(level_differences) > 3):
            continue

        if not (np.all(level_differences > 0) or np.all(level_differences < 0)):
            continue

        safe_report_count += 1

    print(safe_report_count)


def main() -> None:
    run_timed(solution)


if __name__ == '__main__':
    main()