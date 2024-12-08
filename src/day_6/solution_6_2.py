from src.day_6.solution_6_1 import PathChecker
from src.utilities.timer import run_timed


class PathBlockChecker(PathChecker):
    @property
    def starting_location(self):
        starting_location, _ = self.get_starting_location()
        return starting_location

    def get_locations_visited_with_direction(self) -> list[tuple[tuple[int, int], tuple[int, int]]]:

        starting_location, soldier_char = self.get_starting_location()

        direction = self.direction_mapping[soldier_char]
        location = starting_location
        locations_visited = [location]
        locations_visited_with_direction = [(location, direction)]
        next_location = (location[0] + direction[0], location[1] + direction[1])
        while self.is_in_bounds(next_location):
            if self.input_lines[next_location[0]][next_location[1]] == '#':
                direction = self.next_direction_mapping[direction]
            else:
                location = next_location

                if location not in locations_visited:
                    locations_visited_with_direction.append((location, direction))
                locations_visited.append(location)


            next_location = (location[0] + direction[0], location[1] + direction[1])

        return locations_visited_with_direction

    @property
    def locations_to_check(self)-> list[tuple[tuple[int, int], tuple[int, int]]]:
        locations_visited = self.get_locations_visited_with_direction()
        locations_to_check = [x for x in locations_visited if x[0] != self.starting_location]
        return locations_to_check

    def check_if_loop_possible(
        self, check_location: tuple[int, int], direction: tuple[int, int],
    ) -> bool:

        input_lines_with_new_blocker = self.input_lines.copy()
        new_row = (
            self.input_lines[check_location[0]][:check_location[1]] +
            '#' +
            self.input_lines[check_location[0]][check_location[1] + 1:]
        )
        input_lines_with_new_blocker[check_location[0]] = new_row
        check_location = (check_location[0] - direction[0], check_location[1] - direction[1])
        direction = self.next_direction_mapping[direction]
        locations_visited_in_loop = []

        loop_found = False
        continue_checking = True
        while continue_checking:
            continue_checking = False
            while self.is_in_bounds(check_location):
                if (check_location, direction) in locations_visited_in_loop:
                    loop_found = True
                    break

                if input_lines_with_new_blocker[check_location[0]][check_location[1]] == '#':
                    continue_checking = True
                    check_location = (check_location[0] - direction[0], check_location[1] - direction[1])
                    direction = self.next_direction_mapping[direction]
                    break

                locations_visited_in_loop.append((check_location, direction))
                check_location = (check_location[0] + direction[0], check_location[1] + direction[1])

        return loop_found


def solution() -> None:
    with open('src/day_6/input_6_1.txt', 'r') as file:
        input_lines = file.read().splitlines()

    path_block_checker = PathBlockChecker(input_lines)
    locations_to_check = path_block_checker.locations_to_check
    blocker_locations = []
    count = 0
    for location, direction in locations_to_check:
        loop_found = path_block_checker.check_if_loop_possible(location, direction)
        if loop_found:
            count += 1
            blocker_locations.append(location)

    print(len(set(blocker_locations)))


def main() -> None:
    run_timed(solution)


if __name__ == "__main__":
    main()