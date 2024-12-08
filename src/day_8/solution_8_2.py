import itertools
import numpy as np

from src.day_8.solution_8_1 import check_is_valid_antinode_location, get_antenna_locations
from src.utilities.timer import run_timed


def get_in_line_antinode_locations(
    antenna1_location: np.ndarray, antenna2_location: np.ndarray, steps_to_check: int
) -> list[tuple[float, float]]:

    relative_location = antenna2_location - antenna1_location
    relative_antinode_locations = [relative_location * i for i in range(-steps_to_check, steps_to_check + 1)]
    antinode_locations = [tuple(x + antenna1_location) for x in relative_antinode_locations]
    return antinode_locations


def solution() -> None:
    with open('src/day_8/input_8_1.txt', 'r') as file:
        input_lines = file.read().splitlines()

    max_ix = len(input_lines) - 1
    max_jx = len(input_lines[0]) - 1
    antenna_locations = get_antenna_locations(input_lines)

    steps_to_check = max(max_ix, max_jx)
    antinode_locations = []
    for frequency, antennas in antenna_locations.items():
        antenna_pairs = itertools.combinations(antennas, 2)
        for pair in antenna_pairs:
            antinode_locations += get_in_line_antinode_locations(pair[0], pair[1], steps_to_check)

    antinode_locations = list(set(antinode_locations))
    antinode_locations = [x for x in antinode_locations if check_is_valid_antinode_location(x, max_ix, max_jx)]

    print(len(antinode_locations))


def main() -> None:
    run_timed(solution)


if __name__ == "__main__":
    main()