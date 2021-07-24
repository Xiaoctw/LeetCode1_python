from typing import *
from typing import List


class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return
        m, n = len(matrix), len(matrix[0])
        self._sum = [[0] * (n + 1) for _ in range(1 + m)]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                self._sum[i][j] = self._sum[i][j - 1] + matrix[i - 1][j - 1]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                self._sum[i][j] = self._sum[i - 1][j] + self._sum[i][j]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        x1, y1 = row1 - 1, col1 - 1
        x2, y2 = row2, col2
        return self._sum[x2 + 1][y2 + 1] + self._sum[x1 + 1][y1 + 1] - self._sum[x2 + 1][y1 + 1] - self._sum[x1 + 1][
            y2 + 1]


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)

if __name__ == '__main__':
    matrix = [
        [3, 0, 1, 4, 2],
        [5, 6, 3, 2, 1],
        [1, 2, 0, 1, 5],
        [4, 1, 0, 1, 7],
        [1, 0, 3, 0, 5]
    ]
    mat = NumMatrix(matrix)
    print(mat.sumRegion(2, 1, 4, 3))
