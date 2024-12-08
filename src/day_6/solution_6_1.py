import re

from src.utilities.timer import run_timed


DIRECTION_MAPPING = {
    '^': (-1, 0),
    '>': (0, 1),
    'v': (1, 0),
    '<': (0, -1),
}
NEXT_SOLDIER_CHAR = {
    '^': '>',
    '>': 'v',
    'v': '<',
    '<': '^',
}


def get_starting_location(input_lines: list[str]) -> tuple[tuple[int, int], str]:

    for ix, line in enumerate(input_lines):
        for jx, soldier_char in enumerate(line):
            if soldier_char in ['^', '>', 'v', '<']:
                return (ix, jx), soldier_char

    raise ValueError('Invalid input')


def is_in_bounds(location: tuple[int, int], max_ix: int, max_jx: int) -> bool:
    ix, jx = location
    return (ix >= 0) & (ix <= max_ix) & (jx >= 0) & (jx <= max_jx)


def solution() -> None:
    with open('src/day_6/input_6_1.txt', 'r') as file:
        input_lines = file.read().splitlines()

    location, soldier_char = get_starting_location(input_lines)
    locations_visited = [location]

    max_ix = len(input_lines) - 1
    max_jx = len(input_lines[0]) - 1

    direction = DIRECTION_MAPPING[soldier_char]
    next_location = (location[0] + direction[0], location[1] + direction[1])
    while is_in_bounds(next_location, max_ix, max_jx):
        if input_lines[next_location[0]][next_location[1]] == '#':
            soldier_char = NEXT_SOLDIER_CHAR[soldier_char]
            direction = DIRECTION_MAPPING[soldier_char]
        else:
            location = next_location
            locations_visited.append(location)

        next_location = (location[0] + direction[0], location[1] + direction[1])

    print(len(set(locations_visited)))


def main() -> None:
    run_timed(solution)


if __name__ == "__main__":
    main()