from tabnanny import check

from src.utilities.timer import run_timed


DIAGONAL_DIRECTIONS_TO_CHECK = [
    (1, -1),
    (1, 1),
    (-1, 1),
    (-1, -1)
]

SECOND_M_DIRECTIONS_TO_CHECK = {
    (1, -1): [(1, 1), (-1, -1)],
    (1, 1): [(-1, 1), (1, -1)],
    (-1, 1): [(-1, -1), (1, 1)],
    (-1, -1): [(1, -1), (-1, 1)],
}


class MasXFinder:
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

    def search_for_m(
        self, start_ix: int, start_jx: int, directions_to_check: list[tuple[int, int]]
    ) -> tuple[bool, tuple[int, int] | None]:

        for direction in directions_to_check:
            m_found = self.search_for_letter(
                'M', start_ix, start_jx, direction[0], direction[1]
            )
            if m_found:
                return True, direction

        return False, None

    def check_for_mas_x(self, start_ix: int, start_jx: int) -> bool:

        first_m_found, first_m_direction = self.search_for_m(start_ix, start_jx, DIAGONAL_DIRECTIONS_TO_CHECK)
        if not first_m_found:
            return False

        second_m_found, second_m_direction = self.search_for_m(
            start_ix, start_jx, SECOND_M_DIRECTIONS_TO_CHECK[first_m_direction]
        )
        if not second_m_found:
            return False

        s_directions_to_check = [
            x for x in DIAGONAL_DIRECTIONS_TO_CHECK if x != second_m_direction and x != first_m_direction
        ]
        first_s_found = self.search_for_letter(
            'S', start_ix, start_jx, s_directions_to_check[0][0], s_directions_to_check[0][1]
        )
        if not first_s_found:
            return False

        second_s_found = self.search_for_letter(
            'S', start_ix, start_jx, s_directions_to_check[1][0], s_directions_to_check[1][1]
        )
        return second_s_found

    def count_all_mas_x(self):

        mas_x_count = 0
        for ix, line in enumerate(self.input_lines):
            for jx, letter in enumerate(line):
                if letter == 'A':
                    if self.check_for_mas_x(ix, jx):
                        mas_x_count += 1

        return mas_x_count


def solution() -> None:
    with open('src/day_4/input_4_1.txt', 'r') as file:
        input_lines = file.read().splitlines()

    finder = MasXFinder(input_lines)
    mas_x_count = finder.count_all_mas_x()

    print(mas_x_count)


def main() -> None:
    run_timed(solution)


if __name__ == '__main__':
    main()