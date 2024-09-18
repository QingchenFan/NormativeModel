import numpy as np

# 创建一个 3x4 的整型矩阵
matrix = np.array([[1, 2, 3, 4],
                   [5, 6, 7, 8],
                   [9, 10, 11, 12]])

print("Original matrix:")
print(matrix)

# 计算矩阵行之和
row_sums = np.sum(matrix, axis=0)

print("\nMatrix row sums:")
print(row_sums)