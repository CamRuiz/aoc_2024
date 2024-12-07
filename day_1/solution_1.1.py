import numpy as np


if __name__ == '__main__':
    data = np.loadtxt('input_1.1.txt').astype(int)
    value_difference = np.abs(np.sort(data[:, 0]) - np.sort(data[:, 1]))
    total_difference = np.sum(value_difference)
    print(total_difference)
