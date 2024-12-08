from src.utilities.timer import run_timed


def check_equation(target: int, current_value: int, values_to_use: list[int]) -> list[bool]:

    addition_value = current_value + values_to_use[0]
    multiplication_value = current_value * values_to_use[0]

    if len(values_to_use) == 1:
        return [addition_value == target, multiplication_value == target]

    return_value = (
        check_equation(target, addition_value, values_to_use[1:]) +
        check_equation(target, multiplication_value, values_to_use[1:])
    )

    return return_value


def solution() -> None:
    with open('src/day_7/input_7_1.txt', 'r') as file:
        input_lines = file.read().splitlines()

    calibration_result = 0
    for line in input_lines:
        target, equation_values = line.split(': ')
        target = int(target)
        equation_values = [int(x) for x in equation_values.split(' ')]
        equation_checks = check_equation(target, equation_values[0], equation_values[1:])

        if any(equation_checks):
            calibration_result += target

    print(calibration_result)

def main() -> None:
    run_timed(solution)


if __name__ == "__main__":
    main()