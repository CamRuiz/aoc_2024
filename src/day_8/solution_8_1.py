from collections import defaultdict
import itertools
import numpy as np

from src.utilities.timer import run_timed


def check_is_in_bounds(location: tuple[float, float], max_ix: int, max_jx: int) -> bool:
    ix, jx = location
    return (ix >= 0) & (ix <= max_ix) & (jx >= 0) & (jx <= max_jx)


def check_is_valid_antinode_location(location: tuple[float, float], max_ix: int, max_jx: int) -> bool:

    is_integer_location = location[0] == round(location[0]) and location[1] == round(location[1])
    is_in_bounds = check_is_in_bounds(location, max_ix, max_jx)
    return is_integer_location and is_in_bounds


def get_antinode_locations(antenna1_location: np.ndarray, antenna2_location: np.ndarray) -> list[tuple[float, float]]:

    relative_location = antenna2_location - antenna1_location
    relative_antinode_locations = [
        -relative_location,
        2 * relative_location,
        relative_location / 3,
        2 * relative_location / 3,
    ]
    antinode_locations = [tuple(x + antenna1_location) for x in relative_antinode_locations]
    return antinode_locations


def solution() -> None:
    with open('src/day_8/input_8_1.txt', 'r') as file:
        input_lines = file.read().splitlines()

    antenna_locations = defaultdict(list)
    for ix, line in enumerate(input_lines):
        for jx, char in enumerate(line):
            if char != '.':
                antenna_locations[char].append(np.array([ix, jx]))

    antinode_locations = []
    for frequency, antennas in antenna_locations.items():
        antenna_pairs = itertools.combinations(antennas, 2)
        for pair in antenna_pairs:
            antinode_locations += get_antinode_locations(pair[0], pair[1])

    antinode_locations = list(set(antinode_locations))

    max_ix = len(input_lines) - 1
    max_jx = len(input_lines[0]) - 1
    antinode_locations = [x for x in antinode_locations if check_is_valid_antinode_location(x, max_ix, max_jx)]

    print(len(antinode_locations))

def main() -> None:
    run_timed(solution)


if __name__ == "__main__":
    main()