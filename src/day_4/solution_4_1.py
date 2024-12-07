from src.utilities.timer import run_timed


DIRECTIONS_TO_CHECK = (
    (0, -1),
    (1, -1),
    (1, 0),
    (1, 1),
    (0, 1),
    (-1, 1),
    (-1, 0),
    (-1, -1)
)


def solution() -> None:
    with open('src/day_4/input_4_1.txt', 'r') as file:
        input_lines = file.read().splitlines()

    max_ix = len(input_lines) - 1
    max_jx = len(input_lines[0]) - 1

    def search_for_letter(letter_to_find: str, start_ix: int, start_jx: int, ix_step: int, jx_step: int) -> bool:

        check_ix = start_ix + ix_step
        check_jx = start_jx + jx_step
        if (check_ix < 0) or (check_ix > max_ix) or (check_jx < 0) or (check_jx > max_jx):
            return False

        if input_lines[check_ix][check_jx] == letter_to_find:
            return True

        return False

    xmas_count = 0
    for ix, line in enumerate(input_lines):
        for jx, letter in enumerate(line):
            if letter == 'X':
                for direction in DIRECTIONS_TO_CHECK:
                    if not search_for_letter('S', ix, jx, 3 * direction[0], 3 * direction[1]):
                        continue
                    if not search_for_letter('A', ix, jx, 2 * direction[0], 2 * direction[1]):
                        continue
                    if not search_for_letter('M', ix, jx, direction[0], direction[1]):
                        continue
                    xmas_count += 1

    print(xmas_count)


def main() -> None:
    run_timed(solution)


if __name__ == '__main__':
    main()