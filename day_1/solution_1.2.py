import numpy as np


if __name__ == '__main__':
    data = np.loadtxt('input_1.1.txt').astype(int)
    left_values = data[:, 0]
    right_values = data[:, 1]
    equality_comparison = data[np.newaxis, :, 0] == data[:, np.newaxis, 1]
    similarity_score = (equality_comparison @ data[:, 0]).sum()
    print(similarity_score)
