import numpy as np

from src.utilities.timer import run_timed


def solution() -> None:
    data = np.loadtxt('src/day_1/input_1.1.txt').astype(int)
    equality_comparison = data[np.newaxis, :, 0] == data[:, np.newaxis, 1]
    similarity_score = (equality_comparison @ data[:, 0]).sum()
    print(similarity_score)


def main() -> None:
    run_timed(solution)


if __name__ == '__main__':
    main()
