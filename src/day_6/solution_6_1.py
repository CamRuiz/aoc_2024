from src.utilities.timer import run_timed


class PathChecker:
    direction_mapping = {
        '^': (-1, 0),
        '>': (0, 1),
        'v': (1, 0),
        '<': (0, -1),
    }
    next_direction_mapping = {
        (-1, 0): (0, 1),
        (0, 1): (1, 0),
        (1, 0): (0, -1),
        (0, -1): (-1, 0),
    }
    def __init__(self, input_lines: list[str]) -> None:

        self.input_lines = input_lines
        self.max_ix = len(input_lines) - 1
        self.max_jx = len(input_lines[0]) - 1

    def get_starting_location(self) -> tuple[tuple[int, int], str]:

        for ix, line in enumerate(self.input_lines):
            for jx, soldier_char in enumerate(line):
                if soldier_char in ['^', '>', 'v', '<']:
                    return (ix, jx), soldier_char

        raise ValueError('Invalid input')

    def is_in_bounds(self, location: tuple[int, int]) -> bool:
        ix, jx = location
        return (ix >= 0) & (ix <= self.max_ix) & (jx >= 0) & (jx <= self.max_jx)

    def get_locations_visited(self) -> list[tuple[int, int]]:

        location, soldier_char = self.get_starting_location()
        locations_visited = [location]

        direction = self.direction_mapping[soldier_char]
        next_location = (location[0] + direction[0], location[1] + direction[1])
        while self.is_in_bounds(next_location):
            if self.input_lines[next_location[0]][next_location[1]] == '#':
                direction = self.next_direction_mapping[direction]
            else:
                location = next_location
                locations_visited.append(location)

            next_location = (location[0] + direction[0], location[1] + direction[1])

        return list(set(locations_visited))


def solution() -> None:
    with open('src/day_6/input_6_1.txt', 'r') as file:
        input_lines = file.read().splitlines()

    path_checker = PathChecker(input_lines)
    locations_visited = path_checker.get_locations_visited()
    print(len(set(locations_visited)))


def main() -> None:
    run_timed(solution)


if __name__ == "__main__":
    main()