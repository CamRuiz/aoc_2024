"""
This solution is horrible, because I committed to doing it with numpy and calculating the differences all at once.
A much nicer solution could be found by just iterating over the list and checking at each step.
"""
import numpy as np

from src.day_2.solution_2_1 import check_if_all_safe_level_differences
from src.utilities.timer import run_timed


def check_case_of_one_bad_difference(levels: np.ndarray, bad_differences: np.ndarray) -> bool:
    """
    If there is one bad difference we need to check that the new differences are valid after removing the level on
    either side of the bad difference.
    """
    mask_level_before = []
    mask_level_after = []
    for is_bad_difference in bad_differences:
        if is_bad_difference:
            mask_level_before += [False, True]
            mask_level_after += [True, False]
        else:
            mask_level_before.append(True)
            mask_level_after.append(True)

    if check_if_all_safe_level_differences(levels[mask_level_before]):
        return True
    if check_if_all_safe_level_differences(levels[mask_level_after]):
        return True

    return False


def check_case_of_two_bad_differences(levels: np.ndarray, bad_differences: np.ndarray) -> bool:
    """
    If there are 2 bad differences in a row, we need to check that the levels are safe after removing the level in the
    middle.
    """
    mask = []
    reached_bad_difference = False
    ix = 0
    while not reached_bad_difference:
        if bad_differences[ix]:
            mask += [True, False, True]
            reached_bad_difference = True
            ix += 3
        else:
            mask.append(True)
            ix += 1

    mask += [True] * (len(levels) - ix)
    is_safe = check_if_all_safe_level_differences(levels[mask])
    if is_safe:
        return True

    return False


def check_if_safe_level_differences(levels: np.ndarray) -> bool:

    level_differences = levels[1:] - levels[:-1]

    large_differences = np.abs(level_differences) > 3

    positive_differences = level_differences > 0
    positive_difference_count = np.sum(positive_differences)
    negative_differences = level_differences < 0
    negative_difference_count = np.sum(negative_differences)

    len_level_differences = len(level_differences)
    if positive_difference_count >= (len_level_differences - 1):
        non_monotonic_differences = ~positive_differences
    elif negative_difference_count >= (len_level_differences - 1):
        non_monotonic_differences = ~negative_differences
    else:
        return False

    bad_differences = non_monotonic_differences | large_differences
    bad_difference_count = np.sum(bad_differences)

    if bad_difference_count == 0:
        return True

    if bad_difference_count > 2:
        return False

    if bad_difference_count == 1:
        return check_case_of_one_bad_difference(levels, bad_differences)

    if bad_difference_count == 2:
        # This should really only be done if the bad differences are consecutive
        return check_case_of_two_bad_differences(levels, bad_differences)

    return False


def solution() -> None:
    with open("src/day_2/input_2_1.txt", "r") as file:
        lines = file.read().splitlines()

    safe_report_count = 0
    for line in lines:
        levels = np.array([int(x) for x in line.split(" ")])

        is_safe = check_if_safe_level_differences(levels)
        if is_safe:
            safe_report_count += 1

    print(safe_report_count)


def main() -> None:
    run_timed(solution)


if __name__ == '__main__':
    main()