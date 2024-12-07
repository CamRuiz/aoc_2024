import numpy as np

from src.utilities.timer import run_timed


def check_if_all_safe_level_differences(levels: np.ndarray) -> bool:

    level_differences = levels[1:] - levels[:-1]

    if np.any(level_differences == 0):
        return False

    if np.any(np.abs(level_differences) > 3):
        return False

    if not (np.all(level_differences > 0) or np.all(level_differences < 0)):
        return False

    return True


def solution() -> None:
    with open("src/day_2/input_2_1.txt", "r") as file:
        lines = file.read().splitlines()

    safe_report_count = 0
    for line in lines:
        levels = np.array([int(x) for x in line.split(" ")])

        is_safe = check_if_all_safe_level_differences(levels)
        if is_safe:
            safe_report_count += 1

    print(safe_report_count)


def main() -> None:
    run_timed(solution)


if __name__ == '__main__':
    main()