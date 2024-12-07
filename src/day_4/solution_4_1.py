from src.utilities.timer import run_timed


class WordsearchFinder:
    def __init__(self, input_lines: list[str]) -> None:

        self.input_lines = input_lines
        self.max_ix = len(input_lines) - 1
        self.max_jx = len(input_lines[0]) - 1

    def search_for_letter(self, letter_to_find: str, start_ix: int, start_jx: int, ix_step: int, jx_step: int) -> bool:

        check_ix = start_ix + ix_step
        check_jx = start_jx + jx_step
        if (check_ix < 0) or (check_ix > self.max_ix) or (check_jx < 0) or (check_jx > self.max_jx):
            return False

        if self.input_lines[check_ix][check_jx] == letter_to_find:
            return True

        return False


class XmasFinder(WordsearchFinder):

    directions_to_check = [
        (0, -1),
        (1, -1),
        (1, 0),
        (1, 1),
        (0, 1),
        (-1, 1),
        (-1, 0),
        (-1, -1)
    ]

    def check_for_xmas(self, start_ix: int, start_jx: int, direction: tuple[int, int]) -> bool:
            if not self.search_for_letter('S', start_ix, start_jx, 3 * direction[0], 3 * direction[1]):
                return False
            if not self.search_for_letter('A', start_ix, start_jx, 2 * direction[0], 2 * direction[1]):
                return False
            return self.search_for_letter('M', start_ix, start_jx, direction[0], direction[1])

    def count_all_xmas(self):

        xmas_count = 0
        for ix, line in enumerate(self.input_lines):
            for jx, letter in enumerate(line):
                if letter == 'X':
                    for direction in self.directions_to_check:
                        if self.check_for_xmas(ix, jx, direction):
                            xmas_count += 1
        return xmas_count


def solution() -> None:
    with open('src/day_4/input_4_1.txt', 'r') as file:
        input_lines = file.read().splitlines()

    finder = XmasFinder(input_lines)
    xmas_count = finder.count_all_xmas()
    print(xmas_count)


def main() -> None:
    run_timed(solution)


if __name__ == '__main__':
    main()