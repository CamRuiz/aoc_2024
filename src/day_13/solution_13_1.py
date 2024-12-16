import numpy as np
import re

from src.utilities.timer import run_timed

EPS = 1e-8

class ClawMachine:
    a_cost: int = 3
    b_cost: int = 1

    def __init__(
        self, a_movement: tuple[int, int], b_movement: tuple[int, int], prize_location: tuple[int, int]
    ) -> None:
        self.a_movement = a_movement
        self.b_movement = b_movement
        self.prize_location = prize_location

    @classmethod
    def from_text(cls, instruction_text: str) -> "ClawMachine":

        a_line, b_line, prize_line = instruction_text.split('\n')
        a_movement_matches = re.match(r'Button A: X\+(\d+), Y\+(\d+)', a_line)
        a_movement = (int(a_movement_matches.group(1)), int(a_movement_matches.group(2)))

        b_movement_matches = re.match(r'Button B: X\+(\d+), Y\+(\d+)', b_line)
        b_movement = (int(b_movement_matches.group(1)), int(b_movement_matches.group(2)))

        prize_matches = re.match(r'Prize: X=(\d+), Y=(\d+)', prize_line)
        prize_location = (int(prize_matches.group(1)), int(prize_matches.group(2)))

        return cls(a_movement, b_movement, prize_location)

    def solve_for_num_presses(self) -> np.ndarray | None:

        move_matrix = np.array([
            [self.a_movement[0], self.b_movement[0]],
            [self.a_movement[1], self.b_movement[1]],
        ])
        solution = np.linalg.solve(move_matrix, self.prize_location)

        if np.all(np.abs(np.round(solution) - solution) < EPS) and np.all(np.abs(solution - 0) > 0):
            return np.round(solution)
        else:
            return None

    def get_cost(self) -> int:
        possible_num_presses = self.solve_for_num_presses()
        if possible_num_presses is None:
            return 0
        return int(self.a_cost * possible_num_presses[0] + self.b_cost * possible_num_presses[1])


def solution() -> None:
    with open('src/day_13/input_13_1.txt', 'r') as file:
        input_text = file.read()

    machine_input_text = input_text.split('\n\n')
    cost = 0
    for machine_instruction_text in machine_input_text:
        claw_machine = ClawMachine.from_text(machine_instruction_text)
        cost += claw_machine.get_cost()

    print(cost)


def main() -> None:
    run_timed(solution)


if __name__ == "__main__":
    main()