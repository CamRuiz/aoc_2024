import numpy as np
import re

from src.day_13.solution_13_1 import ClawMachine, EPS
from src.utilities.timer import run_timed


class ShiftedClawMachine(ClawMachine):
    amount_to_add = 10000000000000

    @classmethod
    def from_text(cls, instruction_text: str) -> "ClawMachine":

        a_line, b_line, prize_line = instruction_text.split('\n')
        a_movement_matches = re.match(r'Button A: X\+(\d+), Y\+(\d+)', a_line)
        a_movement = (int(a_movement_matches.group(1)), int(a_movement_matches.group(2)))

        b_movement_matches = re.match(r'Button B: X\+(\d+), Y\+(\d+)', b_line)
        b_movement = (int(b_movement_matches.group(1)), int(b_movement_matches.group(2)))

        prize_matches = re.match(r'Prize: X=(\d+), Y=(\d+)', prize_line)
        prize_location = (
            cls.amount_to_add + int(prize_matches.group(1)),
            cls.amount_to_add + int(prize_matches.group(2))
        )

        return cls(a_movement, b_movement, prize_location)

    def solve_for_num_presses(self) -> np.ndarray | None:

        unnormalised_inverse_matrix = np.array([
            [self.b_movement[1], -self.b_movement[0]],
            [-self.a_movement[1], self.a_movement[0]],
        ], dtype=np.int64)
        determinant = self.a_movement[0] * self.b_movement[1] - self.a_movement[1] * self.b_movement[0]
        mult_result = unnormalised_inverse_matrix @ np.array(self.prize_location, dtype=np.int64)

        float_solution = mult_result / determinant
        int_solution = mult_result // determinant

        if np.all(np.abs(float_solution - int_solution) < EPS) and np.all(np.abs(float_solution - 0) > EPS):
            return np.round(int_solution)
        else:
            return None


def solution() -> None:
    with open('src/day_13/input_13_1.txt', 'r') as file:
        input_text = file.read()

    machine_input_text = input_text.split('\n\n')
    cost = 0
    for machine_instruction_text in machine_input_text:
        claw_machine = ShiftedClawMachine.from_text(machine_instruction_text)
        cost += claw_machine.get_cost()

    print(cost)


def main() -> None:
    run_timed(solution)


if __name__ == "__main__":
    main()