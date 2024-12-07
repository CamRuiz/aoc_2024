import numpy as np

from src.utilities.timer import run_timed


def solution() -> None:
    data = np.loadtxt('src/day_1/input_1.1.txt').astype(int)
    value_difference = np.abs(np.sort(data[:, 0]) - np.sort(data[:, 1]))
    total_difference = np.sum(value_difference)
    print(total_difference)


def main() -> None:
    run_timed(solution)

if __name__ == '__main__':
    main()